"""
Tests for main.py CLI
======================
Tests for command line interface and CivilisationHub class.
"""

from unittest.mock import patch

import pytest

from main import (
    CivilisationHub,
    create_argument_parser,
    main,
)


class TestCivilisationHub:
    """Tests for CivilisationHub class."""

    def test_init(self):
        """Test CivilisationHub initialization."""
        hub = CivilisationHub()
        assert hub.VERSION == "1.0.0"
        assert hub.NAME == "Civilisation Hub"
        assert hub._verbose is False

    def test_init_verbose(self):
        """Test CivilisationHub with verbose mode."""
        hub = CivilisationHub(verbose=True)
        assert hub._verbose is True

    def test_meta_equilibrium_property(self):
        """Test meta_equilibrium property."""
        hub = CivilisationHub()
        assert hub.meta_equilibrium is not None

    def test_domains_property_before_init(self):
        """Test domains property before initialization."""
        hub = CivilisationHub()
        assert hub.domains == []

    def test_initialize(self):
        """Test system initialization."""
        hub = CivilisationHub()
        hub.initialize()
        assert len(hub.domains) == 5

    def test_initialize_verbose(self):
        """Test system initialization with verbose mode."""
        hub = CivilisationHub(verbose=True)
        hub.initialize()
        assert len(hub.domains) == 5

    def test_get_meta_balance(self):
        """Test get_meta_balance method."""
        hub = CivilisationHub()
        balance = hub.get_meta_balance()
        assert balance["positive"] == 50.0
        assert balance["negative"] == 50.0
        assert balance["balanced"] is True

    def test_get_operational_ratio(self):
        """Test get_operational_ratio method."""
        hub = CivilisationHub()
        ratio = hub.get_operational_ratio()
        assert ratio["structure"] == 52.0
        assert ratio["flexibility"] == 48.0
        assert abs(ratio["ratio"] - 52 / 48) < 0.001

    def test_is_meta_balanced(self):
        """Test is_meta_balanced method."""
        hub = CivilisationHub()
        assert hub.is_meta_balanced() is True

    def test_validate_system(self):
        """Test validate_system method."""
        hub = CivilisationHub()
        hub.initialize()
        assert hub.validate_system() is True

    def test_get_system_stats(self):
        """Test get_system_stats method."""
        hub = CivilisationHub()
        hub.initialize()
        stats = hub.get_system_stats()
        assert stats["system"] == "Civilisation Hub"
        assert stats["version"] == "1.0.0"
        assert stats["meta_balanced"] is True
        assert stats["domains"]["count"] == 5
        assert stats["total_concepts"] > 0
        assert stats["system_valid"] is True

    def test_prove_meta_meaning(self):
        """Test prove_meta_meaning method."""
        hub = CivilisationHub()
        hub.initialize()
        proof = hub.prove_meta_meaning()
        assert "proofs" in proof
        assert "all_valid" in proof
        assert "conclusion" in proof
        assert proof["all_valid"] is True

    def test_get_domain(self):
        """Test get_domain method."""
        hub = CivilisationHub()
        hub.initialize()

        # Test existing domains
        assert hub.get_domain("mathematics") is not None
        assert hub.get_domain("PHYSICS") is not None
        assert hub.get_domain("Code") is not None

        # Test non-existing domain
        assert hub.get_domain("nonexistent") is None

    def test_display_status(self):
        """Test display_status method."""
        hub = CivilisationHub()
        hub.initialize()
        # Should not raise
        hub.display_status()

    def test_display_proof(self):
        """Test display_proof method."""
        hub = CivilisationHub()
        hub.initialize()
        # Should not raise
        hub.display_proof()

    def test_run_demo(self):
        """Test run_demo method."""
        hub = CivilisationHub()
        hub.initialize()
        # Should not raise
        hub.run_demo()


class TestCivilisationHubPersistence:
    """Tests for CivilisationHub persistence methods."""

    @pytest.fixture
    def hub(self):
        """Create initialized hub with in-memory database."""
        from database.engine import reset_engine
        from database.session import reset_session_manager

        reset_engine()
        reset_session_manager()

        hub = CivilisationHub()
        hub.initialize()
        return hub

    def test_persistence_property(self, hub):
        """Test persistence property lazy initialization."""
        # Access persistence property
        service = hub.persistence
        assert service is not None
        # Should return same instance
        assert hub.persistence is service

    def test_save_domains(self, hub):
        """Test save_domains method."""
        saved = hub.save_domains()
        assert len(saved) == 5
        assert "Mathematics" in saved
        assert "Physics" in saved

    def test_save_domain(self, hub):
        """Test save_domain method."""
        assert hub.save_domain("mathematics") is True
        assert hub.save_domain("nonexistent") is False

    def test_list_saved_domains(self, hub):
        """Test list_saved_domains method."""
        hub.save_domains()
        domains = hub.list_saved_domains()
        assert len(domains) == 5
        names = [d["name"] for d in domains]
        assert "Mathematics" in names

    def test_get_persistence_stats(self, hub):
        """Test get_persistence_stats method."""
        hub.save_domains()
        stats = hub.get_persistence_stats()
        assert stats["total_domains"] == 5
        assert stats["total_concepts"] > 0
        assert stats["compliance_rate"] == 100.0


class TestArgumentParser:
    """Tests for argument parser."""

    def test_create_parser(self):
        """Test parser creation."""
        parser = create_argument_parser()
        assert parser is not None

    def test_default_args(self):
        """Test default arguments."""
        parser = create_argument_parser()
        args = parser.parse_args([])
        assert args.demo is False
        assert args.prove is False
        assert args.status is False
        assert args.domain is None
        assert args.verbose is False
        assert args.save is False
        assert args.list_saved is False
        assert args.db_stats is False

    def test_demo_arg(self):
        """Test --demo argument."""
        parser = create_argument_parser()
        args = parser.parse_args(["--demo"])
        assert args.demo is True

    def test_prove_arg(self):
        """Test --prove argument."""
        parser = create_argument_parser()
        args = parser.parse_args(["--prove"])
        assert args.prove is True

    def test_status_arg(self):
        """Test --status argument."""
        parser = create_argument_parser()
        args = parser.parse_args(["--status"])
        assert args.status is True

    def test_domain_arg(self):
        """Test --domain argument."""
        parser = create_argument_parser()
        args = parser.parse_args(["--domain", "mathematics"])
        assert args.domain == "mathematics"

    def test_domain_arg_choices(self):
        """Test --domain argument choices."""
        parser = create_argument_parser()
        for domain in ["mathematics", "physics", "code", "biology", "philosophy"]:
            args = parser.parse_args(["--domain", domain])
            assert args.domain == domain

    def test_verbose_arg(self):
        """Test --verbose argument."""
        parser = create_argument_parser()
        args = parser.parse_args(["--verbose"])
        assert args.verbose is True

    def test_verbose_short_arg(self):
        """Test -v argument."""
        parser = create_argument_parser()
        args = parser.parse_args(["-v"])
        assert args.verbose is True

    def test_save_arg(self):
        """Test --save argument."""
        parser = create_argument_parser()
        args = parser.parse_args(["--save"])
        assert args.save is True

    def test_save_domain_arg(self):
        """Test --save-domain argument."""
        parser = create_argument_parser()
        args = parser.parse_args(["--save-domain", "mathematics"])
        assert args.save_domain == "mathematics"

    def test_list_saved_arg(self):
        """Test --list-saved argument."""
        parser = create_argument_parser()
        args = parser.parse_args(["--list-saved"])
        assert args.list_saved is True

    def test_db_stats_arg(self):
        """Test --db-stats argument."""
        parser = create_argument_parser()
        args = parser.parse_args(["--db-stats"])
        assert args.db_stats is True


class TestMainFunction:
    """Tests for main() function."""

    @pytest.fixture(autouse=True)
    def reset_db(self):
        """Reset database before each test."""
        from database.engine import get_engine, reset_engine
        from database.session import reset_session_manager

        reset_engine()
        reset_session_manager()
        # Use in-memory database for tests
        engine = get_engine(in_memory=True, reset=True)
        engine.create_all_tables()
        yield
        engine.drop_all_tables()

    def test_main_default(self):
        """Test main with no arguments (default status)."""
        with patch("sys.argv", ["main.py"]):
            result = main()
            assert result == 0

    def test_main_status(self):
        """Test main with --status."""
        with patch("sys.argv", ["main.py", "--status"]):
            result = main()
            assert result == 0

    def test_main_demo(self):
        """Test main with --demo."""
        with patch("sys.argv", ["main.py", "--demo"]):
            result = main()
            assert result == 0

    def test_main_prove(self):
        """Test main with --prove."""
        with patch("sys.argv", ["main.py", "--prove"]):
            result = main()
            assert result == 0

    def test_main_domain(self):
        """Test main with --domain."""
        with patch("sys.argv", ["main.py", "--domain", "mathematics"]):
            result = main()
            assert result == 0

    def test_main_domain_not_found(self):
        """Test main with invalid domain."""
        with patch("sys.argv", ["main.py"]):
            hub = CivilisationHub()
            hub.initialize()
            # Manually test the domain not found path
            assert hub.get_domain("invalid") is None

    def test_main_verbose(self):
        """Test main with --verbose."""
        with patch("sys.argv", ["main.py", "-v"]):
            result = main()
            assert result == 0

    def test_main_save(self, capsys):
        """Test main with --save."""
        with patch("sys.argv", ["main.py", "--save"]):
            result = main()
            assert result == 0
            captured = capsys.readouterr()
            assert "Saved 5 domains" in captured.out

    def test_main_save_domain(self, capsys):
        """Test main with --save-domain."""
        with patch("sys.argv", ["main.py", "--save-domain", "mathematics"]):
            result = main()
            assert result == 0
            captured = capsys.readouterr()
            assert "Saved domain" in captured.out

    def test_main_save_domain_not_found(self, capsys):
        """Test main with --save-domain for non-existent domain."""
        with patch("sys.argv", ["main.py", "--save-domain", "invalid"]):
            result = main()
            assert result == 1
            captured = capsys.readouterr()
            assert "not found" in captured.out

    def test_main_list_saved_empty(self, capsys):
        """Test main with --list-saved when no domains saved."""
        with patch("sys.argv", ["main.py", "--list-saved"]):
            result = main()
            assert result == 0
            captured = capsys.readouterr()
            assert "No domains saved" in captured.out

    def test_main_list_saved(self, capsys):
        """Test main with --list-saved after saving."""
        # First save
        with patch("sys.argv", ["main.py", "--save"]):
            main()
        # Then list
        with patch("sys.argv", ["main.py", "--list-saved"]):
            result = main()
            assert result == 0
            captured = capsys.readouterr()
            assert "Saved domains" in captured.out

    def test_main_db_stats(self, capsys):
        """Test main with --db-stats."""
        with patch("sys.argv", ["main.py", "--db-stats"]):
            result = main()
            assert result == 0
            captured = capsys.readouterr()
            assert "Database Statistics" in captured.out


class TestMainIntegration:
    """Integration tests for main module."""

    @pytest.fixture(autouse=True)
    def reset_db(self):
        """Reset database before each test."""
        from database.engine import get_engine, reset_engine
        from database.session import reset_session_manager

        reset_engine()
        reset_session_manager()
        # Use in-memory database for tests
        engine = get_engine(in_memory=True, reset=True)
        engine.create_all_tables()
        yield
        engine.drop_all_tables()

    def test_full_workflow(self, capsys):
        """Test a full workflow: init, save, list, stats."""
        # Initialize and save
        with patch("sys.argv", ["main.py", "--save"]):
            result = main()
            assert result == 0

        # List saved
        with patch("sys.argv", ["main.py", "--list-saved"]):
            result = main()
            assert result == 0
            captured = capsys.readouterr()
            assert "Mathematics" in captured.out

        # Check stats
        with patch("sys.argv", ["main.py", "--db-stats"]):
            result = main()
            assert result == 0
            captured = capsys.readouterr()
            assert "Total domains: 5" in captured.out

    def test_hub_meta_compliance(self):
        """Test that all hub operations maintain META compliance."""
        hub = CivilisationHub()
        hub.initialize()

        # Verify META balance
        assert hub.is_meta_balanced()

        # Verify all domains are balanced
        for domain in hub.domains:
            assert domain.validate_balance()

        # Verify system validation
        assert hub.validate_system()

        # Verify proof
        proof = hub.prove_meta_meaning()
        assert proof["all_valid"]

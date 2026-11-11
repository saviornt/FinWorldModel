"""Command-line entry point for the initial Alpaca historical dataset."""

from __future__ import annotations

import argparse
import logging
import sys
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from fin_data.providers.alpaca.ingestor import create_ingestor_from_environment, default_end_date  # noqa: E402


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Backfill the initial 36-instrument Alpaca daily dataset.")
    parser.add_argument("--start", type=date.fromisoformat, default=date(2016, 1, 1))
    parser.add_argument("--end", type=date.fromisoformat, default=default_end_date())
    parser.add_argument("--feed", choices=("iex",), default="iex")
    parser.add_argument("--store", type=Path, default=None)
    parser.add_argument(
        "--no-resume",
        action="store_true",
        help="Ignore the local completion manifest and re-fetch all symbols.",
    )
    parser.add_argument(
        "--no-corporate-actions",
        action="store_true",
        help="Skip the separate corporate-actions request.",
    )
    parser.add_argument("--log-level", choices=("DEBUG", "INFO", "WARNING", "ERROR"), default="INFO")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    try:
        ingestor = create_ingestor_from_environment(
            store_path=args.store,
            start=args.start,
            end=args.end,
            feed=args.feed,
        )
        ingestor.run(
            resume=not args.no_resume,
            include_corporate_actions=not args.no_corporate_actions,
        )
    except Exception:
        logging.getLogger(__name__).exception("Alpaca ingestion failed.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

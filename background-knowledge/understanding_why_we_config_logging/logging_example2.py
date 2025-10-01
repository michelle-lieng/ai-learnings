import logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(levelname)s] %(message)s")
print("--- WITH basicConfig ---")
logging.info("✅ Connected (INFO)")
logging.warning("⚠️ Connected (WARNING)")

"""
now we can see info is shown!

$ python background-knowledge/logging_example2.py
--- WITH basicConfig ---
2025-10-01 22:08:39,013 [INFO] ✅ Connected (INFO)
2025-10-01 22:08:39,013 [WARNING] ⚠️ Connected (WARNING)
"""
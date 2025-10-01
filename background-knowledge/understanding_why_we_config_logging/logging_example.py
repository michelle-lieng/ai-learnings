import logging
print("--- WITHOUT basicConfig ---")
logging.info("✅ Connected (INFO)")
logging.warning("⚠️ Connected (WARNING)")

"""
can see here that info isn't shown

$ python background-knowledge/logging_example.py 
--- WITHOUT basicConfig ---
WARNING:root:⚠️ Connected (WARNING)
"""
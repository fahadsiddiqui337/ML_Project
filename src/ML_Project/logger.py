import logging
import os
from datetime import datetime

# Create logs directory if not exists
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s %(levelname)s %(message)s",
    level=logging.INFO,
)

# Optional: also log to console (stdout)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter("[%(asctime)s] %(lineno)d %(name)s %(levelname)s %(message)s")
console_handler.setFormatter(formatter)
logging.getLogger().addHandler(console_handler)

# Example correct logging usage:

numerical_columns = ['writing_score', 'reading_score']
categorical_columns = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']

# Using f-string (safe and recommended)
logging.info(f"Numerical Columns: {numerical_columns}")
logging.info(f"Categorical Columns: {categorical_columns}")

# Or using % formatting with arguments (alternative)
logging.info("Numerical Columns: %s", numerical_columns)
logging.info("Categorical Columns: %s", categorical_columns)

# Simple log message without formatting placeholders
logging.info("Starting data ingestion process")
logging.info("Data ingestion completed successfully")

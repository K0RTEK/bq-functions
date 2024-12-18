import os
import shutil

# Define source and destination directories
src_dir = 'D:/BQ_functions/mangaseya_analytics/sql'
dst_dir = 'D:/BQ_functions/mangaseya_analytics/python'

# Iterate through files in source directory
for filename in os.listdir(src_dir):
    if filename.endswith('.sql'):
        # Copy file to destination directory with new extension
        src_file = os.path.join(src_dir, filename)
        dst_file = os.path.join(dst_dir, filename.replace('.sql', '.py'))
        shutil.copy2(src_file, dst_file)
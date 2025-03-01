#!/bin/bash

# Script to create a clean deployment ZIP file for Elastic Beanstalk
# Excludes development files, git files, and macOS metadata files

# Default output filename
OUTPUT_FILE="eb-deploy.zip"

# Parse command line arguments
if [ $# -gt 0 ]; then
    OUTPUT_FILE="$1"
fi

# Check if the output file already exists
if [ -f "$OUTPUT_FILE" ]; then
    echo "Warning: $OUTPUT_FILE already exists. Overwriting..."
    rm "$OUTPUT_FILE"
fi

echo "Creating deployment package: $OUTPUT_FILE"
echo "Excluding unnecessary files..."

# Create ZIP file, excluding unnecessary files
zip -r "$OUTPUT_FILE" . \
    -x "*.DS_Store" \
    -x "__MACOSX/*" \
    -x "._*" \
    -x ".git/*" \
    -x ".gitignore" \
    -x "__pycache__/*" \
    -x "*.pyc" \
    -x "$OUTPUT_FILE" \
    -x "create-deploy-zip.sh"

# Check if the zip command was successful
if [ $? -eq 0 ]; then
    echo "✅ Deployment package created successfully: $OUTPUT_FILE"
    echo "You can now deploy this package to Elastic Beanstalk."
else
    echo "❌ Error creating deployment package."
    exit 1
fi

# Show the file size
FILE_SIZE=$(du -h "$OUTPUT_FILE" | cut -f1)
echo "Package size: $FILE_SIZE" 
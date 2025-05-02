#!/bin/bash

# Linux, macOS, WSL

if [ ! -f "extensions.txt" ]; then
    echo "❌ Error: 'extensions.txt' not found!"
    exit 1
fi

echo "⚙️ Starting VS Code extensions installation..."

while read -r line; do
    # Skips empty lines and comments
    if [[ -z "$line" || "$line" =~ ^# ]]; then
        continue
    fi

    # Extracts extension IDs, removes inline comments and trim whitespaces
    ext_id=$(echo "$line" | sed 's/#.*//' | xargs)

    echo "🔧 Installing: $ext_id"
    
    # Installs extensions and filters unwanted VS Code CLI messages
    code --install-extension "$ext_id" 2>&1 | sed -E \
        -e '/Installing extensions?/d' \
    
    # Checks exit status and shows error if anything has failed
    if [ ${PIPESTATUS[0]} -ne 0 ]; then
        echo "❌ Failed: $ext_id"
    fi
done < "extensions.txt"

echo "✅ Done! Check above for any errors."

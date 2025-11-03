# The SentenceSplitter attempts to split text while respecting the boundaries of sentences.

import json
import pprint
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import SimpleDirectoryReader

# Load the lion.md file
lionMD= SimpleDirectoryReader(input_files=["lion.md"]).load_data()

# measure by tokens
splitter = SentenceSplitter(
    chunk_size=400,
    chunk_overlap=20,
)
nodes = splitter.get_nodes_from_documents(lionMD)



# Write each node with only important properties to file
with open("chunked_lion.md", "w", encoding="utf-8") as f:
    for i, node in enumerate(nodes, 1):
        f.write(f"\n{'='*80}\n")
        f.write(f"NODE {i}\n")
        f.write(f"{'='*80}\n")
        
        # Get important properties
        node_info = {
            'node_id': getattr(node, 'node_id', None),
            'text': getattr(node, 'text', None),
            'metadata': getattr(node, 'metadata', None),
        }
        
        # Add any start/end char indexes if available
        if hasattr(node, 'start_char_idx'):
            node_info['start_char_idx'] = node.start_char_idx
        if hasattr(node, 'end_char_idx'):
            node_info['end_char_idx'] = node.end_char_idx
        
        # Write formatted output
        for key, value in node_info.items():
            f.write(f"\n{key}:\n")
            if isinstance(value, dict):
                f.write(json.dumps(value, indent=2))
            else:
                f.write(str(value))
            f.write("\n")
        
        f.write(f"{'='*80}\n")

print(f"Chunked results saved to chunked_lion.md ({len(nodes)} chunks)")
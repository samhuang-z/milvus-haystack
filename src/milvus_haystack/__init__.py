# SPDX-FileCopyrightText: 2023-present deepset GmbH <info@deepset.ai>
#
# SPDX-License-Identifier: Apache-2.0
from .document_store import MilvusDocumentStore
from .milvus_embedding_retriever import MilvusEmbeddingRetriever

__all__ = [
    "MilvusDocumentStore",
    "MilvusEmbeddingRetriever"
]

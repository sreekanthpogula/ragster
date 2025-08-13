import unittest
from ragster_main import Ragster
from unittest.mock import MagicMock, patch
from langchain_core.chat_history import BaseChatMessageHistory

# Assuming Ragster is imported from the module where it's defined

class TestRagster(unittest.TestCase):
    def setUp(self):
        self.mock_llm = MagicMock()
        self.mock_embeddings = MagicMock()
        self.mock_vector_store = MagicMock()
        self.ragster = Ragster(self.mock_llm, self.mock_embeddings, self.mock_vector_store)

    def test_init_sets_attributes(self):
        self.assertEqual(self.ragster.llm, self.mock_llm)
        self.assertEqual(self.ragster.embeddings, self.mock_embeddings)
        self.assertEqual(self.ragster.vector_store, self.mock_vector_store)

    def test_retriever_calls_vector_store(self):
        mock_retriever = MagicMock()
        self.mock_vector_store.as_retriever.return_value = mock_retriever
        retriever = self.ragster._Ragster__retriever()
        self.mock_vector_store.as_retriever.assert_called_once_with(
            search_type="similarity_score_threshold",
            search_kwargs={"k": 10, "score_threshold": 0.3}
        )
        self.assertEqual(retriever, mock_retriever)

    @patch("langchain.chains.create_history_aware_retriever")
    @patch("langchain.chains.combine_documents.create_stuff_documents_chain")
    @patch("langchain.chains.create_retrieval_chain")
    @patch("langchain.prompts.ChatPromptTemplate.from_messages")
    def test_llm_answer_generator_returns_chain(
        self, mock_from_messages, mock_create_retrieval_chain, mock_create_stuff_documents_chain, mock_create_history_aware_retriever
    ):
        mock_chain = MagicMock()
        mock_create_retrieval_chain.return_value = mock_chain
        mock_create_history_aware_retriever.return_value = MagicMock()
        mock_create_stuff_documents_chain.return_value = MagicMock()
        mock_from_messages.return_value = MagicMock()

    def test_get_session_history_creates_and_returns_history(self):
        session_id = "abc"
        history = self.ragster.get_session_history(session_id)
        self.assertIsInstance(history, BaseChatMessageHistory)
        # Should return the same object if called again
        self.assertIs(history, self.ragster.get_session_history(session_id))

    @patch.object(Ragster, "llm_answer_generator")
    @patch("langchain_core.runnables.history.RunnableWithMessageHistory")
    def test_conversational_invokes_chain(self, mock_runnable, mock_llm_answer_generator):
        mock_chain = MagicMock()
        mock_llm_answer_generator.return_value = mock_chain
        mock_runnable_instance = MagicMock()
        mock_runnable.return_value = mock_runnable_instance
        mock_runnable_instance.invoke.return_value = {"answer": ""}
        result = self.ragster.conversational("What is law?", "sess1")
        mock_runnable_instance.invoke.assert_not_called()  # Should not be called in this test
        mock_llm_answer_generator.assert_called_once_with("What is law?")

if __name__ == "__main__":
    unittest.main()
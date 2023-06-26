import tempfile
from unittest.mock import patch
import pandas as pd

from django.test import SimpleTestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


UPLOAD_FILE_URL = reverse("core:upload-file")


@patch("core.views.process_and_save_data")
@patch("pandas.read_csv")
@patch("pandas.read_excel")
class FileManagerTest(SimpleTestCase):

    def setUp(self):
        self.client = APIClient()

    def _send_file_request(self, payload):
        return self.client.post(
                UPLOAD_FILE_URL,
                payload,
                format="multipart"
            )

    def test_load_file_only_supports_csv_or_excel(
            self, mock_csv, mock_excel, mock_save):
        """Test the accepted format files are just csv and excel"""
        mock_csv.return_value = pd.DataFrame()
        mock_excel.return_value = pd.DataFrame()
        mock_save.return_value = None

        with tempfile.NamedTemporaryFile(suffix=".jpg") as image_file:
            payload = {"file": image_file}
            result = self._send_file_request(payload)
            self.assertEqual(
                result.status_code,
                status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
            )

        with tempfile.NamedTemporaryFile(suffix=".csv") as csv_file:
            payload = {"file": csv_file}
            result = result = self._send_file_request(payload)
            self.assertEqual(result.status_code, status.HTTP_201_CREATED)

        with tempfile.NamedTemporaryFile(suffix=".xlsx") as excel_file:
            payload = {"file": excel_file}
            result = result = self._send_file_request(payload)
            self.assertEqual(result.status_code, status.HTTP_201_CREATED)

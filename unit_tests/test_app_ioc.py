import pytest
from unittest.mock import Mock, patch
from app_ioc import AppIoc
from process_link_service import ProcessLinkService

def test_download_youtube_videos_and_convert_as_mp3_valid_urls():
    process_link_mock_service: Mock = Mock(spec=ProcessLinkService)
    valid_urls = ["https://www.youtube.com/watch?v=example1", "https://www.youtube.com/watch?v=example2"]
    app_ioc = AppIoc(process_link_mock_service, valid_urls)
    
    app_ioc.download_youtube_videos_and_convert_as_mp3()
    
    assert process_link_mock_service.download_youtube_as_mp3.call_count == 2

def test_download_youtube_videos_and_convert_as_mp3_invalid_url():
    process_link_mock_service = Mock(spec=ProcessLinkService)
    invalid_urls = ["invalid_url"]
    app_ioc = AppIoc(process_link_mock_service, invalid_urls)
    
    with pytest.raises(ValueError, match="URL is not valid. Please provide a valid Youtube URL"):
        app_ioc.download_youtube_videos_and_convert_as_mp3()
        
def test_download_youtube_videos_and_convert_as_mp3_mixed_urls():
    mock_service = Mock(spec=ProcessLinkService)
    mixed_urls = ["https://www.youtube.com/watch?v=example1", "invalid_url"]
    app_ioc = AppIoc(mock_service, mixed_urls)
    
    with pytest.raises(ValueError, match="URL is not valid. Please provide a valid Youtube URL"):
        app_ioc.download_youtube_videos_and_convert_as_mp3()
        
def test_download_youtube_videos_and_convert_as_mp3_empty_url():
    mock_service = Mock(spec=ProcessLinkService)
    mixed_urls = ["https://www.youtube.com/watch?v=example1", ""]
    app_ioc = AppIoc(mock_service, mixed_urls)
    
    with pytest.raises(ValueError, match="URL is not valid. Please provide a valid Youtube URL"):
        app_ioc.download_youtube_videos_and_convert_as_mp3()
        
def test_download_youtube_videos_and_convert_as_mp3_empty_whitspace_url():
    mock_service = Mock(spec=ProcessLinkService)
    mixed_urls = ["https://www.youtube.com/watch?v=example1", " "]
    app_ioc = AppIoc(mock_service, mixed_urls)
    
    with pytest.raises(ValueError, match="URL is not valid. Please provide a valid Youtube URL"):
        app_ioc.download_youtube_videos_and_convert_as_mp3()

def test_download_youtube_videos_and_convert_as_mp3_urls_with_none_values():
    mock_service = Mock(spec=ProcessLinkService)
    urls_with_none = ["https://www.youtube.com/watch?v=example1", None, "https://www.youtube.com/watch?v=example2"]
    app_ioc = AppIoc(mock_service, urls_with_none)
    
    with pytest.raises(ValueError, match="URL is not valid. Please provide a valid Youtube URL"):
        app_ioc.download_youtube_videos_and_convert_as_mp3()

def test_download_youtube_videos_and_convert_as_mp3_empty_url_list():
    process_link_mock_service = Mock(spec=ProcessLinkService)
    
    with pytest.raises(ValueError, match="URL list is empty. Please add at least 1 valid URL"):
        AppIoc(process_link_mock_service, [])

def test_download_youtube_videos_and_convert_as_mp3_none_service():
    with pytest.raises(ValueError, match="ProcessLinkService is not provided. Please initialize an instance for it"):
        AppIoc(None, ["https://www.youtube.com/watch?v=example1"])

def test_download_youtube_videos_and_convert_as_mp3_download_failure():
    process_link_mock_service: Mock = Mock(spec=ProcessLinkService)
    process_link_mock_service.download_youtube_as_mp3.side_effect = Exception("Download failed")
    valid_urls = ["https://www.youtube.com/watch?v=example1"]
    app_ioc = AppIoc(process_link_mock_service, valid_urls)
    
    with patch('builtins.print') as mocked_print:
        app_ioc.download_youtube_videos_and_convert_as_mp3()
        mocked_print.assert_called_with("Failed to download or convert https://www.youtube.com/watch?v=example1: Download failed")
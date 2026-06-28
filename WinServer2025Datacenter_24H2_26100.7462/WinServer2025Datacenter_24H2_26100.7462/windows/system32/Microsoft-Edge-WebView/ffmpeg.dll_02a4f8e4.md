# Binary Specification: ffmpeg.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\Microsoft-Edge-WebView\ffmpeg.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `02a4f8e4a7eef04f58874ffaf0e1f1a65898ca338be18f784ba107adf08c4eb1`
* **Total Exported Functions:** 51

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 37 | `avcodec_find_decoder` | `0x5EA90` | 123 | UnwindData |  |
| 41 | `avcodec_open2` | `0x61150` | 1,434 | UnwindData |  |
| 38 | `avcodec_flush_buffers` | `0x61700` | 170 | UnwindData |  |
| 43 | `avcodec_receive_frame` | `0x62090` | 88 | UnwindData |  |
| 35 | `avcodec_descriptor_get` | `0x62DB0` | 104 | UnwindData |  |
| 36 | `avcodec_descriptor_next` | `0x62E30` | 1,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `avcodec_parameters_to_context` | `0x63420` | 583 | UnwindData |  |
| 44 | `avcodec_send_packet` | `0x65670` | 224 | UnwindData |  |
| 34 | `avcodec_alloc_context3` | `0x16E760` | 403 | UnwindData |  |
| 39 | `avcodec_free_context` | `0x16E900` | 130 | UnwindData |  |
| 16 | `av_init_packet` | `0x16F410` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `av_packet_alloc` | `0x16F460` | 90 | UnwindData |  |
| 23 | `av_packet_free` | `0x16F4C0` | 198 | UnwindData |  |
| 25 | `av_packet_unref` | `0x16F590` | 155 | UnwindData |  |
| 20 | `av_new_packet` | `0x16F630` | 223 | UnwindData |  |
| 24 | `av_packet_get_side_data` | `0x16F9D0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `av_packet_copy_props` | `0x16FBA0` | 406 | UnwindData |  |
| 33 | `avcodec_align_dimensions` | `0x172360` | 183 | UnwindData |  |
| 40 | `avcodec_get_name` | `0x172430` | 78 | UnwindData |  |
| 45 | `avformat_alloc_context` | `0x17B120` | 135 | UnwindData |  |
| 31 | `av_stream_get_first_dts` | `0x17BA20` | 3,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `avformat_free_context` | `0x17C610` | 543 | UnwindData |  |
| 51 | `avio_close` | `0x17DB00` | 146 | UnwindData |  |
| 50 | `avio_alloc_context` | `0x17DCC0` | 284 | UnwindData |  |
| 49 | `avformat_open_input` | `0x180350` | 1,507 | UnwindData |  |
| 46 | `avformat_close_input` | `0x180940` | 192 | UnwindData |  |
| 26 | `av_read_frame` | `0x1812B0` | 579 | UnwindData |  |
| 47 | `avformat_find_stream_info` | `0x182700` | 7,148 | UnwindData |  |
| 29 | `av_seek_frame` | `0x1AB8B0` | 1,102 | UnwindData |  |
| 7 | `av_force_cpu_flags` | `0x1AEA70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `av_get_cpu_flags` | `0x1AEA90` | 31 | UnwindData |  |
| 15 | `av_image_check_size` | `0x1AF490` | 107 | UnwindData |  |
| 1 | `av_buffer_create` | `0x1BBF20` | 134 | UnwindData |  |
| 2 | `av_buffer_get_opaque` | `0x1BC160` | 12,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `av_dict_count` | `0x1BF060` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `av_dict_get` | `0x1BF0A0` | 409 | UnwindData |  |
| 6 | `av_dict_set` | `0x1BF240` | 791 | UnwindData |  |
| 4 | `av_dict_free` | `0x1BF6C0` | 93 | UnwindData |  |
| 32 | `av_strerror` | `0x1C0110` | 96 | UnwindData |  |
| 8 | `av_frame_alloc` | `0x1C35D0` | 132 | UnwindData |  |
| 10 | `av_frame_free` | `0x1C3660` | 45 | UnwindData |  |
| 11 | `av_frame_unref` | `0x1C3690` | 376 | UnwindData |  |
| 9 | `av_frame_clone` | `0x1C4740` | 251 | UnwindData |  |
| 17 | `av_log_set_level` | `0x1C5FC0` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `av_rescale_q` | `0x1C62F0` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `av_max_alloc` | `0x1C6740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `av_malloc` | `0x1C6750` | 75 | UnwindData |  |
| 12 | `av_free` | `0x1C6820` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `av_strdup` | `0x1C6A90` | 95 | UnwindData |  |
| 13 | `av_get_bytes_per_sample` | `0x1CC2B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `av_samples_get_buffer_size` | `0x1CC2F0` | 227 | UnwindData |  |

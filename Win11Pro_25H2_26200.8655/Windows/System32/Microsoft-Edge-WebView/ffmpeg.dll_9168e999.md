# Binary Specification: ffmpeg.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Microsoft-Edge-WebView\ffmpeg.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `9168e9999a85e75bfb271c11d8e3623bc9c49852744ad9b291c201b178e3b41a`
* **Total Exported Functions:** 52

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 38 | `avcodec_find_decoder` | `0x616C0` | 123 | UnwindData |  |
| 42 | `avcodec_open2` | `0x63C20` | 1,435 | UnwindData |  |
| 39 | `avcodec_flush_buffers` | `0x641D0` | 167 | UnwindData |  |
| 44 | `avcodec_receive_frame` | `0x64B60` | 91 | UnwindData |  |
| 36 | `avcodec_descriptor_get` | `0x65830` | 104 | UnwindData |  |
| 37 | `avcodec_descriptor_next` | `0x658B0` | 1,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `avcodec_parameters_to_context` | `0x65EB0` | 609 | UnwindData |  |
| 45 | `avcodec_send_packet` | `0x68110` | 227 | UnwindData |  |
| 35 | `avcodec_alloc_context3` | `0x16D110` | 403 | UnwindData |  |
| 40 | `avcodec_free_context` | `0x16D2B0` | 130 | UnwindData |  |
| 16 | `av_init_packet` | `0x16DE10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `av_packet_alloc` | `0x16DE60` | 90 | UnwindData |  |
| 23 | `av_packet_free` | `0x16DEC0` | 198 | UnwindData |  |
| 25 | `av_packet_unref` | `0x16DF90` | 155 | UnwindData |  |
| 20 | `av_new_packet` | `0x16E030` | 223 | UnwindData |  |
| 24 | `av_packet_get_side_data` | `0x16E3D0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `av_packet_copy_props` | `0x16E5A0` | 387 | UnwindData |  |
| 34 | `avcodec_align_dimensions2` | `0x170D80` | 535 | UnwindData |  |
| 33 | `avcodec_align_dimensions` | `0x170FA0` | 179 | UnwindData |  |
| 41 | `avcodec_get_name` | `0x171070` | 78 | UnwindData |  |
| 46 | `avformat_alloc_context` | `0x17A9D0` | 127 | UnwindData |  |
| 31 | `av_stream_get_first_dts` | `0x17B2D0` | 3,072 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `avformat_free_context` | `0x17BED0` | 555 | UnwindData |  |
| 52 | `avio_close` | `0x17D3A0` | 146 | UnwindData |  |
| 51 | `avio_alloc_context` | `0x17D560` | 284 | UnwindData |  |
| 50 | `avformat_open_input` | `0x17FB70` | 1,283 | UnwindData |  |
| 47 | `avformat_close_input` | `0x180170` | 192 | UnwindData |  |
| 26 | `av_read_frame` | `0x180AE0` | 578 | UnwindData |  |
| 48 | `avformat_find_stream_info` | `0x181F60` | 7,179 | UnwindData |  |
| 29 | `av_seek_frame` | `0x1ABC70` | 1,102 | UnwindData |  |
| 7 | `av_force_cpu_flags` | `0x1AEF10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `av_get_cpu_flags` | `0x1AEF30` | 31 | UnwindData |  |
| 15 | `av_image_check_size` | `0x1B0650` | 107 | UnwindData |  |
| 1 | `av_buffer_create` | `0x1BD030` | 134 | UnwindData |  |
| 2 | `av_buffer_get_opaque` | `0x1BD270` | 10,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `av_dict_count` | `0x1BFB50` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `av_dict_get` | `0x1BFB90` | 409 | UnwindData |  |
| 6 | `av_dict_set` | `0x1BFD30` | 792 | UnwindData |  |
| 4 | `av_dict_free` | `0x1C01B0` | 93 | UnwindData |  |
| 32 | `av_strerror` | `0x1C0C00` | 93 | UnwindData |  |
| 8 | `av_frame_alloc` | `0x1C4090` | 141 | UnwindData |  |
| 10 | `av_frame_free` | `0x1C4120` | 45 | UnwindData |  |
| 11 | `av_frame_unref` | `0x1C4150` | 385 | UnwindData |  |
| 9 | `av_frame_clone` | `0x1C52D0` | 250 | UnwindData |  |
| 17 | `av_log_set_level` | `0x1C6CE0` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `av_rescale_q` | `0x1C7010` | 1,104 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `av_max_alloc` | `0x1C7460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `av_malloc` | `0x1C7470` | 75 | UnwindData |  |
| 12 | `av_free` | `0x1C7540` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `av_strdup` | `0x1C77B0` | 95 | UnwindData |  |
| 13 | `av_get_bytes_per_sample` | `0x1CCF80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `av_samples_get_buffer_size` | `0x1CCFC0` | 227 | UnwindData |  |

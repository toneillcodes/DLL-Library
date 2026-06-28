# Binary Specification: wpcap.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wpcap.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `25cd11d21d713db7ca5334937b212700d3f34b3cdacafef26133c80d5d72c689`
* **Total Exported Functions:** 119

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `bpf_dump` | `0x1010` | 252 | UnwindData |  |
| 2 | `bpf_filter` | `0x1170` | 23 | UnwindData |  |
| 4 | `bpf_validate` | `0x1190` | 23 | UnwindData |  |
| 3 | `bpf_image` | `0x1C40` | 1,726 | UnwindData |  |
| 70 | `pcap_next_etherent` | `0x2360` | 589 | UnwindData |  |
| 11 | `pcap_compile` | `0x12C50` | 931 | UnwindData |  |
| 12 | `pcap_compile_nopcap` | `0x13000` | 116 | UnwindData |  |
| 40 | `pcap_freecode` | `0x13080` | 43 | UnwindData |  |
| 65 | `pcap_nametonetaddr` | `0x14120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `pcap_wsockinit` | `0x14120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `pcap_ether_aton` | `0x14130` | 175 | UnwindData |  |
| 32 | `pcap_ether_hostton` | `0x141E0` | 223 | UnwindData |  |
| 61 | `pcap_nametoaddr` | `0x142C0` | 20 | UnwindData |  |
| 62 | `pcap_nametoaddrinfo` | `0x14330` | 133 | UnwindData |  |
| 63 | `pcap_nametoeproto` | `0x143C0` | 91 | UnwindData |  |
| 64 | `pcap_nametollc` | `0x14420` | 91 | UnwindData |  |
| 66 | `pcap_nametoport` | `0x14480` | 609 | UnwindData |  |
| 67 | `pcap_nametoportrange` | `0x146F0` | 48 | UnwindData |  |
| 68 | `pcap_nametoproto` | `0x147A0` | 34 | UnwindData |  |
| 6 | `pcap_activate` | `0x18940` | 60 | UnwindData |  |
| 7 | `pcap_breakloop` | `0x18AB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `pcap_bufsize` | `0x18AD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `pcap_can_set_rfmon` | `0x18AF0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `pcap_close` | `0x18B30` | 35 | UnwindData |  |
| 13 | `pcap_create` | `0x18B60` | 61 | UnwindData |  |
| 14 | `pcap_createsrcstr` | `0x18CB0` | 39 | UnwindData |  |
| 15 | `pcap_datalink` | `0x18CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `pcap_datalink_ext` | `0x18D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `pcap_datalink_name_to_val` | `0x18D20` | 224 | UnwindData |  |
| 18 | `pcap_datalink_val_to_description` | `0x18E00` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `pcap_datalink_val_to_description_or_dlt` | `0x18E50` | 105 | UnwindData |  |
| 20 | `pcap_datalink_val_to_name` | `0x18EF0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `pcap_dispatch` | `0x18F40` | 18 | UnwindData |  |
| 33 | `pcap_file` | `0x18F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `pcap_fileno` | `0x18F70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `pcap_findalldevs` | `0x18F90` | 455 | UnwindData |  |
| 37 | `pcap_free_datalinks` | `0x19160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `pcap_free_tstamp_types` | `0x19160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `pcap_freealldevs` | `0x19170` | 14 | UnwindData |  |
| 41 | `pcap_get_airpcap_handle` | `0x19230` | 72 | UnwindData |  |
| 42 | `pcap_get_tstamp_precision` | `0x192C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `pcap_geterr` | `0x192D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `pcap_getevent` | `0x192E0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `pcap_getnonblock` | `0x19360` | 86 | UnwindData |  |
| 48 | `pcap_init` | `0x19430` | 143 | UnwindData |  |
| 49 | `pcap_inject` | `0x194C0` | 136 | UnwindData |  |
| 50 | `pcap_is_swapped` | `0x19580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `pcap_list_datalinks` | `0x195A0` | 206 | UnwindData |  |
| 53 | `pcap_list_tstamp_types` | `0x19670` | 179 | UnwindData |  |
| 54 | `pcap_live_dump` | `0x19730` | 22 | UnwindData |  |
| 55 | `pcap_live_dump_ended` | `0x19780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `pcap_loop` | `0x19790` | 125 | UnwindData |  |
| 59 | `pcap_major_version` | `0x19810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `pcap_minor_version` | `0x19830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `pcap_next` | `0x19850` | 77 | UnwindData |  |
| 71 | `pcap_next_ex` | `0x198A0` | 87 | UnwindData |  |
| 72 | `pcap_offline_filter` | `0x19900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `pcap_oid_get_request` | `0x19920` | 22 | UnwindData |  |
| 74 | `pcap_oid_set_request` | `0x19970` | 22 | UnwindData |  |
| 76 | `pcap_open_dead` | `0x199C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `pcap_open_dead_with_tstamp_precision` | `0x199D0` | 559 | UnwindData |  |
| 78 | `pcap_open_live` | `0x19C00` | 1,167 | UnwindData |  |
| 81 | `pcap_parsesrcstr` | `0x1A4B0` | 476 | UnwindData |  |
| 82 | `pcap_perror` | `0x1A790` | 61 | UnwindData |  |
| 88 | `pcap_sendpacket` | `0x1A800` | 87 | UnwindData |  |
| 89 | `pcap_sendqueue_alloc` | `0x1A860` | 90 | UnwindData |  |
| 90 | `pcap_sendqueue_destroy` | `0x1A8C0` | 31 | UnwindData |  |
| 91 | `pcap_sendqueue_queue` | `0x1A8E0` | 109 | UnwindData |  |
| 92 | `pcap_sendqueue_transmit` | `0x1A950` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `pcap_set_buffer_size` | `0x1A990` | 64 | UnwindData |  |
| 94 | `pcap_set_datalink` | `0x1A9D0` | 309 | UnwindData |  |
| 95 | `pcap_set_immediate_mode` | `0x1AB40` | 60 | UnwindData |  |
| 96 | `pcap_set_promisc` | `0x1AB80` | 60 | UnwindData |  |
| 97 | `pcap_set_rfmon` | `0x1ABC0` | 60 | UnwindData |  |
| 98 | `pcap_set_snaplen` | `0x1AC00` | 57 | UnwindData |  |
| 99 | `pcap_set_timeout` | `0x1AC40` | 60 | UnwindData |  |
| 100 | `pcap_set_tstamp_precision` | `0x1AC80` | 136 | UnwindData |  |
| 101 | `pcap_set_tstamp_type` | `0x1AD10` | 136 | UnwindData |  |
| 102 | `pcap_setbuff` | `0x1ADA0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `pcap_setdirection` | `0x1ADE0` | 120 | UnwindData |  |
| 104 | `pcap_setfilter` | `0x1AE90` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `pcap_setmintocopy` | `0x1AED0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `pcap_setmode` | `0x1AF10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `pcap_setnonblock` | `0x1AF50` | 86 | UnwindData |  |
| 109 | `pcap_setuserbuffer` | `0x1AFC0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `pcap_snapshot` | `0x1B000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `pcap_stats` | `0x1B020` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `pcap_stats_ex` | `0x1B060` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `pcap_statustostr` | `0x1B0A0` | 254 | UnwindData |  |
| 114 | `pcap_strerror` | `0x1B210` | 90 | UnwindData |  |
| 115 | `pcap_tstamp_type_name_to_val` | `0x1B270` | 224 | UnwindData |  |
| 116 | `pcap_tstamp_type_val_to_description` | `0x1B350` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `pcap_tstamp_type_val_to_name` | `0x1B3A0` | 3,632 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `pcap_hopen_offline` | `0x1C1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `pcap_hopen_offline_with_tstamp_precision` | `0x1C1E0` | 179 | UnwindData |  |
| 79 | `pcap_open_offline` | `0x1C2A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `pcap_open_offline_with_tstamp_precision` | `0x1C2B0` | 68 | UnwindData |  |
| 22 | `pcap_dump` | `0x1DF70` | 136 | UnwindData |  |
| 23 | `pcap_dump_close` | `0x1E000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `pcap_dump_file` | `0x1E010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `pcap_dump_flush` | `0x1E020` | 25 | UnwindData |  |
| 26 | `pcap_dump_ftell` | `0x1E040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `pcap_dump_ftell64` | `0x1E050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `pcap_dump_hopen` | `0x1E060` | 87 | UnwindData |  |
| 29 | `pcap_dump_open` | `0x1E170` | 68 | UnwindData |  |
| 30 | `pcap_dump_open_append` | `0x1E2C0` | 174 | UnwindData |  |
| 51 | `pcap_lib_version` | `0x1FF90` | 16 | UnwindData |  |
| 56 | `pcap_lookupdev` | `0x20050` | 43 | UnwindData |  |
| 57 | `pcap_lookupnet` | `0x202B0` | 186 | UnwindData |  |
| 36 | `pcap_findalldevs_ex` | `0x220E0` | 128 | UnwindData |  |
| 75 | `pcap_open` | `0x225C0` | 559 | UnwindData |  |
| 108 | `pcap_setsampling` | `0x227F0` | 5,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `pcap_remoteact_accept` | `0x23F20` | 42 | UnwindData |  |
| 84 | `pcap_remoteact_accept_ex` | `0x23F50` | 940 | UnwindData |  |
| 85 | `pcap_remoteact_cleanup` | `0x24300` | 36 | UnwindData |  |
| 86 | `pcap_remoteact_close` | `0x24330` | 394 | UnwindData |  |
| 87 | `pcap_remoteact_list` | `0x244C0` | 286 | UnwindData |  |
| 5 | `eproto_db` | `0x74000` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `pcap_version` | `0x74150` | 0 | Indeterminate |  |

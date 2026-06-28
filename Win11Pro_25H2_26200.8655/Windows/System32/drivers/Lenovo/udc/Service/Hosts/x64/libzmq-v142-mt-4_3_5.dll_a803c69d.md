# Binary Specification: libzmq-v142-mt-4_3_5.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\Service\Hosts\x64\libzmq-v142-mt-4_3_5.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a803c69d10047f4a4978c85230dae3a0d010c7227e95c3f36c2533067de864f7`
* **Total Exported Functions:** 96

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 19 | `zmq_curve_keypair` | `0x15980` | 26 | UnwindData |  |
| 20 | `zmq_curve_public` | `0x15980` | 26 | UnwindData |  |
| 61 | `zmq_ppoll` | `0x15980` | 26 | UnwindData |  |
| 3 | `zmq_atomic_counter_inc` | `0x1BF90` | 108,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `zmq_msg_set` | `0x365E0` | 26 | UnwindData |  |
| 7 | `zmq_bind` | `0x45B70` | 79 | UnwindData |  |
| 8 | `zmq_close` | `0x45BC0` | 62 | UnwindData |  |
| 9 | `zmq_connect` | `0x45C00` | 79 | UnwindData |  |
| 10 | `zmq_connect_peer` | `0x45C50` | 145 | UnwindData |  |
| 11 | `zmq_ctx_destroy` | `0x45CF0` | 26 | UnwindData |  |
| 18 | `zmq_ctx_term` | `0x45CF0` | 26 | UnwindData |  |
| 82 | `zmq_term` | `0x45CF0` | 26 | UnwindData |  |
| 12 | `zmq_ctx_get` | `0x45D60` | 77 | UnwindData |  |
| 13 | `zmq_ctx_get_ext` | `0x45DB0` | 101 | UnwindData |  |
| 14 | `zmq_ctx_new` | `0x45E20` | 27 | UnwindData |  |
| 15 | `zmq_ctx_set` | `0x45EA0` | 94 | UnwindData |  |
| 16 | `zmq_ctx_set_ext` | `0x45F00` | 101 | UnwindData |  |
| 17 | `zmq_ctx_shutdown` | `0x45F70` | 59 | UnwindData |  |
| 21 | `zmq_device` | `0x45FB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `zmq_disconnect` | `0x45FD0` | 79 | UnwindData |  |
| 93 | `zmq_unbind` | `0x45FD0` | 79 | UnwindData |  |
| 23 | `zmq_errno` | `0x46020` | 17 | UnwindData |  |
| 24 | `zmq_getsockopt` | `0x46040` | 101 | UnwindData |  |
| 25 | `zmq_has` | `0x460B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `zmq_init` | `0x46120` | 12 | UnwindData |  |
| 27 | `zmq_join` | `0x461B0` | 79 | UnwindData |  |
| 28 | `zmq_leave` | `0x46200` | 79 | UnwindData |  |
| 29 | `zmq_msg_close` | `0x46250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `zmq_msg_copy` | `0x46260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `zmq_msg_data` | `0x46270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `zmq_msg_get` | `0x46280` | 133 | UnwindData |  |
| 33 | `zmq_msg_gets` | `0x46310` | 230 | UnwindData |  |
| 34 | `zmq_msg_group` | `0x46400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `zmq_msg_init` | `0x46410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `zmq_msg_init_buffer` | `0x46420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `zmq_msg_init_data` | `0x46430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `zmq_msg_init_size` | `0x46440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `zmq_msg_more` | `0x46450` | 17 | UnwindData |  |
| 40 | `zmq_msg_move` | `0x46470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `zmq_msg_recv` | `0x46480` | 152 | UnwindData |  |
| 42 | `zmq_msg_routing_id` | `0x46520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `zmq_msg_send` | `0x46530` | 103 | UnwindData |  |
| 45 | `zmq_msg_set_group` | `0x465A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `zmq_msg_set_routing_id` | `0x465B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `zmq_msg_size` | `0x465C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `zmq_poll` | `0x465D0` | 236 | UnwindData |  |
| 49 | `zmq_poller_add` | `0x46AC0` | 157 | UnwindData |  |
| 50 | `zmq_poller_add_fd` | `0x46B60` | 146 | UnwindData |  |
| 51 | `zmq_poller_destroy` | `0x46C00` | 107 | UnwindData |  |
| 52 | `zmq_poller_fd` | `0x46C70` | 79 | UnwindData |  |
| 53 | `zmq_poller_modify` | `0x46CC0` | 154 | UnwindData |  |
| 54 | `zmq_poller_modify_fd` | `0x46D60` | 143 | UnwindData |  |
| 55 | `zmq_poller_new` | `0x46DF0` | 73 | UnwindData |  |
| 56 | `zmq_poller_remove` | `0x46E40` | 124 | UnwindData |  |
| 57 | `zmq_poller_remove_fd` | `0x46EC0` | 110 | UnwindData |  |
| 58 | `zmq_poller_size` | `0x46F30` | 64 | UnwindData |  |
| 59 | `zmq_poller_wait` | `0x46F70` | 160 | UnwindData |  |
| 60 | `zmq_poller_wait_all` | `0x47010` | 126 | UnwindData |  |
| 62 | `zmq_proxy` | `0x47090` | 45 | UnwindData |  |
| 63 | `zmq_proxy_steerable` | `0x470C0` | 45 | UnwindData |  |
| 64 | `zmq_recv` | `0x470F0` | 67 | UnwindData |  |
| 65 | `zmq_recviov` | `0x47320` | 69 | UnwindData |  |
| 66 | `zmq_recvmsg` | `0x47630` | 149 | UnwindData |  |
| 67 | `zmq_send` | `0x476D0` | 300 | UnwindData |  |
| 68 | `zmq_send_const` | `0x47800` | 312 | UnwindData |  |
| 69 | `zmq_sendiov` | `0x47940` | 81 | UnwindData |  |
| 70 | `zmq_sendmsg` | `0x47B00` | 100 | UnwindData |  |
| 71 | `zmq_setsockopt` | `0x47B70` | 101 | UnwindData |  |
| 73 | `zmq_socket` | `0x47BE0` | 74 | UnwindData |  |
| 74 | `zmq_socket_get_peer_state` | `0x47C30` | 105 | UnwindData |  |
| 75 | `zmq_socket_monitor` | `0x47CA0` | 115 | UnwindData |  |
| 76 | `zmq_socket_monitor_pipes_stats` | `0x47D20` | 59 | UnwindData |  |
| 77 | `zmq_socket_monitor_versioned` | `0x47D60` | 111 | UnwindData |  |
| 81 | `zmq_strerror` | `0x47DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `zmq_timers_add` | `0x47DE0` | 103 | UnwindData |  |
| 86 | `zmq_timers_cancel` | `0x47E50` | 77 | UnwindData |  |
| 87 | `zmq_timers_destroy` | `0x47EA0` | 102 | UnwindData |  |
| 88 | `zmq_timers_execute` | `0x47F10` | 59 | UnwindData |  |
| 89 | `zmq_timers_new` | `0x47F50` | 132 | UnwindData |  |
| 90 | `zmq_timers_reset` | `0x47FE0` | 77 | UnwindData |  |
| 91 | `zmq_timers_set_interval` | `0x48030` | 98 | UnwindData |  |
| 92 | `zmq_timers_timeout` | `0x480A0` | 59 | UnwindData |  |
| 94 | `zmq_version` | `0x480E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `zmq_atomic_counter_dec` | `0x48100` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `zmq_atomic_counter_destroy` | `0x48120` | 35 | UnwindData |  |
| 4 | `zmq_atomic_counter_new` | `0x48150` | 115 | UnwindData |  |
| 5 | `zmq_atomic_counter_set` | `0x481D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `zmq_atomic_counter_value` | `0x481E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `zmq_sleep` | `0x481F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `zmq_stopwatch_intermediate` | `0x48200` | 22 | UnwindData |  |
| 79 | `zmq_stopwatch_start` | `0x48220` | 107 | UnwindData |  |
| 80 | `zmq_stopwatch_stop` | `0x48290` | 58 | UnwindData |  |
| 83 | `zmq_threadclose` | `0x482D0` | 23 | UnwindData |  |
| 84 | `zmq_threadstart` | `0x48360` | 226 | UnwindData |  |
| 95 | `zmq_z85_decode` | `0x48450` | 281 | UnwindData |  |
| 96 | `zmq_z85_encode` | `0x48570` | 77 | UnwindData |  |

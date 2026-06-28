# Binary Specification: libcrypto.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\libcrypto.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4bfc7ae52d06359d3d69dc7cf2582c82b4253072fe96938dadb186266bda9d70`
* **Total Exported Functions:** 3712

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 11 | `AES_encrypt` | `0x1460` | 1,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `AES_decrypt` | `0x1A10` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `AES_set_encrypt_key` | `0x1AF0` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `AES_set_decrypt_key` | `0x1DE0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `AES_cbc_encrypt` | `0x2020` | 50,272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 780 | `Camellia_cbc_encrypt` | `0xE480` | 7,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2236 | `RC4` | `0x10380` | 1,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2237 | `RC4_set_key` | `0x10A20` | 30,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1127 | `ERR_load_CRYPTO_strings` | `0x18170` | 57 | UnwindData |  |
| 655 | `CRYPTO_THREADID_cmp` | `0x181B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 656 | `CRYPTO_THREADID_cpy` | `0x181C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 657 | `CRYPTO_THREADID_current` | `0x181D0` | 30 | UnwindData |  |
| 658 | `CRYPTO_THREADID_get_callback` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 682 | `CRYPTO_dbg_get_options` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 703 | `CRYPTO_get_dynlock_create_callback` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 704 | `CRYPTO_get_dynlock_destroy_callback` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 705 | `CRYPTO_get_dynlock_lock_callback` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 706 | `CRYPTO_get_dynlock_value` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 709 | `CRYPTO_get_id_callback` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 715 | `CRYPTO_get_mem_debug_options` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 718 | `CRYPTO_get_new_dynlockid` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 719 | `CRYPTO_get_new_lockid` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 721 | `CRYPTO_is_mem_check_on` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 725 | `CRYPTO_mem_ctrl` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 736 | `CRYPTO_pop_info` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 737 | `CRYPTO_push_info_` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 741 | `CRYPTO_remove_all_info` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 748 | `CRYPTO_set_locked_mem_ex_functions` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 749 | `CRYPTO_set_locked_mem_functions` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 751 | `CRYPTO_set_mem_debug_functions` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 753 | `CRYPTO_set_mem_ex_functions` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 754 | `CRYPTO_set_mem_functions` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 975 | `EC_GROUP_get_basis_type` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 984 | `EC_GROUP_have_precompute_mult` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1088 | `ENGINE_by_id` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1090 | `ENGINE_ctrl_cmd` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1091 | `ENGINE_ctrl_cmd_string` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1092 | `ENGINE_finish` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1093 | `ENGINE_free` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1094 | `ENGINE_get_default_RSA` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1097 | `ENGINE_init` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1101 | `ENGINE_load_private_key` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1102 | `ENGINE_load_public_key` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1103 | `ENGINE_new` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1104 | `ENGINE_register_all_complete` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1105 | `ENGINE_set_default` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1106 | `ENGINE_set_default_RSA` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1599 | `FIPS_mode` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2216 | `RAND_SSLeay` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2221 | `RAND_get_rand_method` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3418 | `getuid` | `0x181F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `ASN1_PCTX_get_cert_flags` | `0x18200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 659 | `CRYPTO_THREADID_hash` | `0x18200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1221 | `EVP_CIPHER_key_length` | `0x18200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `ASN1_time_tm_clamp_notafter` | `0x18210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 660 | `CRYPTO_THREADID_set_callback` | `0x18210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 731 | `CRYPTO_num_locks` | `0x18210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 990 | `EC_GROUP_precompute_mult` | `0x18210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2223 | `RAND_poll` | `0x18210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2226 | `RAND_set_rand_method` | `0x18210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2227 | `RAND_status` | `0x18210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2666 | `X509V3_add_standard_extensions` | `0x18210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 353 | `BIO_sock_cleanup` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 661 | `CRYPTO_THREADID_set_numeric` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 662 | `CRYPTO_THREADID_set_pointer` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 681 | `CRYPTO_dbg_free` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 683 | `CRYPTO_dbg_malloc` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 684 | `CRYPTO_dbg_realloc` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 685 | `CRYPTO_dbg_set_options` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 686 | `CRYPTO_destroy_dynlockid` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 743 | `CRYPTO_set_dynlock_create_callback` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 744 | `CRYPTO_set_dynlock_destroy_callback` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 745 | `CRYPTO_set_dynlock_lock_callback` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 747 | `CRYPTO_set_id_callback` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 752 | `CRYPTO_set_mem_debug_options` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1089 | `ENGINE_cleanup` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1098 | `ENGINE_load_builtin_engines` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1099 | `ENGINE_load_dynamic` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1100 | `ENGINE_load_openssl` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1895 | `OPENSSL_init` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2038 | `PKCS12_PBE_add` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2096 | `PKCS5_PBE_add` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2217 | `RAND_add` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2219 | `RAND_cleanup` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2225 | `RAND_seed` | `0x18220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 702 | `CRYPTO_get_add_lock_callback` | `0x18230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 710 | `CRYPTO_get_lock_name` | `0x18240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1095 | `ENGINE_get_id` | `0x18240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1096 | `ENGINE_get_name` | `0x18240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 713 | `CRYPTO_get_locking_callback` | `0x18250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 729 | `CRYPTO_memcmp` | `0x18260` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 742 | `CRYPTO_set_add_lock_callback` | `0x18320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 750 | `CRYPTO_set_locking_callback` | `0x18330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 756 | `CRYPTO_thread_id` | `0x18340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1893 | `OPENSSL_cpu_caps` | `0x18350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1894 | `OPENSSL_cpuid_setup` | `0x18360` | 40 | UnwindData |  |
| 1906 | `OpenSSLDie` | `0x183E0` | 81 | UnwindData |  |
| 1891 | `OPENSSL_cleanup` | `0x18440` | 64 | UnwindData |  |
| 1896 | `OPENSSL_init_crypto` | `0x18480` | 162 | UnwindData |  |
| 1909 | `OpenSSL_version` | `0x18580` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1910 | `OpenSSL_version_num` | `0x185F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2413 | `SSLeay` | `0x185F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2414 | `SSLeay_version` | `0x18600` | 2,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 678 | `CRYPTO_cleanup_all_ex_data` | `0x18E70` | 104 | UnwindData |  |
| 687 | `CRYPTO_dup_ex_data` | `0x18EE0` | 142 | UnwindData |  |
| 689 | `CRYPTO_free_ex_data` | `0x18F70` | 142 | UnwindData |  |
| 707 | `CRYPTO_get_ex_data` | `0x19000` | 68 | UnwindData |  |
| 708 | `CRYPTO_get_ex_new_index` | `0x19050` | 176 | UnwindData |  |
| 730 | `CRYPTO_new_ex_data` | `0x19100` | 142 | UnwindData |  |
| 746 | `CRYPTO_set_ex_data` | `0x19190` | 101 | UnwindData |  |
| 84 | `ASN1_PCTX_free` | `0x192A0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 289 | `BIO_meth_free` | `0x192A0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 688 | `CRYPTO_free` | `0x192A0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 690 | `CRYPTO_free_locked` | `0x192A0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1223 | `EVP_CIPHER_meth_free` | `0x192A0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1265 | `EVP_ENCODE_CTX_free` | `0x192A0` | 352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `ASN1_PCTX_get_flags` | `0x19400` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `ASN1_STRING_length` | `0x19400` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 543 | `CMS_RecipientInfo_type` | `0x19400` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1044 | `EC_METHOD_get_field_type` | `0x19400` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1234 | `EVP_CIPHER_nid` | `0x19400` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1312 | `EVP_MD_type` | `0x19400` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1398 | `EVP_PKEY_id` | `0x19400` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2361 | `SCT_get_version` | `0x19400` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2835 | `X509_OBJECT_get_type` | `0x19400` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2859 | `X509_PURPOSE_get_id` | `0x19400` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3006 | `X509_TRUST_get_trust` | `0x19400` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 711 | `CRYPTO_get_locked_mem_ex_functions` | `0x19480` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 712 | `CRYPTO_get_locked_mem_functions` | `0x194A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 714 | `CRYPTO_get_mem_debug_functions` | `0x194C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 716 | `CRYPTO_get_mem_ex_functions` | `0x19500` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 717 | `CRYPTO_get_mem_functions` | `0x19530` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 723 | `CRYPTO_malloc` | `0x19560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 724 | `CRYPTO_malloc_locked` | `0x19560` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 738 | `CRYPTO_realloc` | `0x19580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 739 | `CRYPTO_realloc_clean` | `0x195A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 740 | `CRYPTO_remalloc` | `0x195D0` | 27 | UnwindData |  |
| 755 | `CRYPTO_strdup` | `0x195F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1890 | `OPENSSL_cleanse` | `0x19600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 726 | `CRYPTO_mem_leaks` | `0x19610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 727 | `CRYPTO_mem_leaks_cb` | `0x19610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 728 | `CRYPTO_mem_leaks_fp` | `0x19610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1600 | `FIPS_mode_set` | `0x19620` | 61 | UnwindData |  |
| 1899 | `OPENSSL_strcasecmp` | `0x19660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1900 | `OPENSSL_strncasecmp` | `0x19670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `AES_cfb128_encrypt` | `0x19680` | 57 | UnwindData |  |
| 6 | `AES_cfb1_encrypt` | `0x196C0` | 57 | UnwindData |  |
| 7 | `AES_cfb8_encrypt` | `0x19700` | 57 | UnwindData |  |
| 8 | `AES_ctr128_encrypt` | `0x19740` | 59 | UnwindData |  |
| 10 | `AES_ecb_encrypt` | `0x19780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `AES_ige_encrypt` | `0x19790` | 65 | UnwindData |  |
| 13 | `AES_ofb128_encrypt` | `0x19AC0` | 46 | UnwindData |  |
| 16 | `AES_unwrap_key` | `0x19AF0` | 68 | UnwindData |  |
| 17 | `AES_wrap_key` | `0x19C60` | 65 | UnwindData |  |
| 28 | `ASN1_BIT_STRING_free` | `0x19DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `ASN1_BIT_STRING_get_bit` | `0x19DB0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `ASN1_BIT_STRING_new` | `0x19E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `ASN1_BIT_STRING_set` | `0x19E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `ASN1_OCTET_STRING_set` | `0x19E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `ASN1_BIT_STRING_set_bit` | `0x19E30` | 272 | UnwindData |  |
| 3228 | `d2i_ASN1_BIT_STRING` | `0x1A0B0` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3432 | `i2d_ASN1_BIT_STRING` | `0x1A240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `ASN1_ENUMERATED_free` | `0x1A250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `ASN1_ENUMERATED_get` | `0x1A260` | 25 | UnwindData |  |
| 39 | `ASN1_ENUMERATED_get_int64` | `0x1A330` | 169 | UnwindData |  |
| 41 | `ASN1_ENUMERATED_new` | `0x1A3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `ASN1_ENUMERATED_set` | `0x1A3F0` | 96 | UnwindData |  |
| 43 | `ASN1_ENUMERATED_set_int64` | `0x1A450` | 97 | UnwindData |  |
| 44 | `ASN1_ENUMERATED_to_BN` | `0x1A4C0` | 121 | UnwindData |  |
| 477 | `BN_to_ASN1_ENUMERATED` | `0x1A540` | 312 | UnwindData |  |
| 3208 | `a2i_ASN1_ENUMERATED` | `0x1A680` | 550 | UnwindData |  |
| 3230 | `d2i_ASN1_ENUMERATED` | `0x1A930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3421 | `i2a_ASN1_ENUMERATED` | `0x1A940` | 35 | UnwindData |  |
| 3434 | `i2d_ASN1_ENUMERATED` | `0x1AA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `ASN1_INTEGER_cmp` | `0x1AA70` | 60 | UnwindData |  |
| 60 | `ASN1_INTEGER_dup` | `0x1AAB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `ASN1_INTEGER_free` | `0x1AAD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `ASN1_INTEGER_get` | `0x1AAE0` | 25 | UnwindData |  |
| 63 | `ASN1_INTEGER_get_int64` | `0x1AC90` | 92 | UnwindData |  |
| 64 | `ASN1_INTEGER_get_uint64` | `0x1AE40` | 189 | UnwindData |  |
| 66 | `ASN1_INTEGER_new` | `0x1AF00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `ASN1_INTEGER_set` | `0x1AF10` | 96 | UnwindData |  |
| 68 | `ASN1_INTEGER_set_int64` | `0x1AF70` | 97 | UnwindData |  |
| 69 | `ASN1_INTEGER_set_uint64` | `0x1AFE0` | 82 | UnwindData |  |
| 70 | `ASN1_INTEGER_to_BN` | `0x1B040` | 27 | UnwindData |  |
| 478 | `BN_to_ASN1_INTEGER` | `0x1B0D0` | 316 | UnwindData |  |
| 3209 | `a2i_ASN1_INTEGER` | `0x1B210` | 551 | UnwindData |  |
| 3234 | `d2i_ASN1_INTEGER` | `0x1BA10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3245 | `d2i_ASN1_UINTEGER` | `0x1BA20` | 370 | UnwindData |  |
| 3422 | `i2a_ASN1_INTEGER` | `0x1BBA0` | 51 | UnwindData |  |
| 3438 | `i2d_ASN1_INTEGER` | `0x1BF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `ASN1_mbstring_copy` | `0x1BF60` | 32 | UnwindData |  |
| 208 | `ASN1_mbstring_ncopy` | `0x1BF80` | 754 | UnwindData |  |
| 74 | `ASN1_OBJECT_create` | `0x1C750` | 59 | UnwindData |  |
| 75 | `ASN1_OBJECT_free` | `0x1C790` | 10 | UnwindData |  |
| 77 | `ASN1_OBJECT_new` | `0x1C800` | 79 | UnwindData |  |
| 3207 | `a2d_ASN1_OBJECT` | `0x1CAE0` | 282 | UnwindData |  |
| 3236 | `d2i_ASN1_OBJECT` | `0x1CFE0` | 11 | UnwindData |  |
| 3423 | `i2a_ASN1_OBJECT` | `0x1D180` | 72 | UnwindData |  |
| 3440 | `i2d_ASN1_OBJECT` | `0x1D300` | 39 | UnwindData |  |
| 3631 | `i2t_ASN1_OBJECT` | `0x1D3A0` | 181 | UnwindData |  |
| 78 | `ASN1_OCTET_STRING_cmp` | `0x1D920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `ASN1_OCTET_STRING_dup` | `0x1D930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `ASN1_OCTET_STRING_free` | `0x1D940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `ASN1_OCTET_STRING_new` | `0x1D950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3237 | `d2i_ASN1_OCTET_STRING` | `0x1D960` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3441 | `i2d_ASN1_OCTET_STRING` | `0x1D970` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3253 | `d2i_AutoPrivateKey` | `0x1D980` | 236 | UnwindData |  |
| 3357 | `d2i_PrivateKey` | `0x1DBA0` | 330 | UnwindData |  |
| 3565 | `i2d_PrivateKey` | `0x1DCF0` | 49 | UnwindData |  |
| 102 | `ASN1_PRINTABLE_type` | `0x1DD80` | 43 | UnwindData |  |
| 162 | `ASN1_UNIVERSALSTRING_to_string` | `0x1DE40` | 107 | UnwindData |  |
| 3360 | `d2i_PublicKey` | `0x1DFB0` | 346 | UnwindData |  |
| 3568 | `i2d_PublicKey` | `0x1E110` | 108 | UnwindData |  |
| 120 | `ASN1_STRING_print_ex` | `0x1E180` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `ASN1_STRING_print_ex_fp` | `0x1E1A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2829 | `X509_NAME_print_ex` | `0x1E1C0` | 49 | UnwindData |  |
| 2830 | `X509_NAME_print_ex_fp` | `0x1E200` | 23 | UnwindData |  |
| 109 | `ASN1_STRING_cmp` | `0x1EEA0` | 92 | UnwindData |  |
| 110 | `ASN1_STRING_copy` | `0x1EF00` | 76 | UnwindData |  |
| 111 | `ASN1_STRING_data` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `ASN1_STRING_get0_data` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `BIO_get_callback` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 373 | `BN_GENCB_get_arg` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 633 | `CONF_imodule_get_name` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 772 | `CT_POLICY_EVAL_CTX_get0_issuer` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 843 | `DH_get0_p` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 902 | `DSA_get0_p` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 943 | `ECDSA_SIG_get0_s` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 972 | `EC_GROUP_get0_generator` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1634 | `GOST_KEY_get0_public_key` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1877 | `OCSP_resp_get0_tbs_sigalg` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2279 | `RSA_get_method` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2293 | `RSA_meth_get_pub_enc` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2427 | `TS_ACCURACY_get_millis` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2454 | `TS_MSG_IMPRINT_get_msg` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2474 | `TS_REQ_get_msg_imprint` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2510 | `TS_RESP_get_token` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2524 | `TS_STATUS_INFO_get0_text` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2545 | `TS_TST_INFO_get_policy_id` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2909 | `X509_REVOKED_get0_revocationDate` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3023 | `X509_VERIFY_PARAM_get_time` | `0x1F010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `ASN1_STRING_dup` | `0x1F020` | 90 | UnwindData |  |
| 113 | `ASN1_STRING_free` | `0x1F190` | 17 | UnwindData |  |
| 92 | `ASN1_PCTX_set_flags` | `0x1F1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `ASN1_STRING_length_set` | `0x1F1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `ASN1_STRING_new` | `0x1F1F0` | 79 | UnwindData |  |
| 119 | `ASN1_STRING_print` | `0x1F240` | 218 | UnwindData |  |
| 122 | `ASN1_STRING_set` | `0x1F320` | 227 | UnwindData |  |
| 123 | `ASN1_STRING_set0` | `0x1F410` | 86 | UnwindData |  |
| 127 | `ASN1_STRING_to_UTF8` | `0x1F470` | 190 | UnwindData |  |
| 87 | `ASN1_PCTX_get_nm_flags` | `0x1F530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `ASN1_STRING_type` | `0x1F530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1215 | `EVP_CIPHER_block_size` | `0x1F530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1310 | `EVP_MD_pkey_type` | `0x1F530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2860 | `X509_PURPOSE_get_trust` | `0x1F530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3005 | `X509_TRUST_get_flags` | `0x1F530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `ASN1_STRING_type_new` | `0x1F540` | 81 | UnwindData |  |
| 3210 | `a2i_ASN1_STRING` | `0x1F5A0` | 505 | UnwindData |  |
| 3424 | `i2a_ASN1_STRING` | `0x1F7A0` | 35 | UnwindData |  |
| 106 | `ASN1_STRING_TABLE_add` | `0x1F8C0` | 362 | UnwindData |  |
| 107 | `ASN1_STRING_TABLE_cleanup` | `0x1FA30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `ASN1_STRING_TABLE_get` | `0x1FA60` | 143 | UnwindData |  |
| 115 | `ASN1_STRING_get_default_mask` | `0x1FAF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `ASN1_STRING_set_by_NID` | `0x1FB00` | 187 | UnwindData |  |
| 125 | `ASN1_STRING_set_default_mask` | `0x1FBC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `ASN1_STRING_set_default_mask_asc` | `0x1FBD0` | 314 | UnwindData |  |
| 137 | `ASN1_TIME_diff` | `0x1FD30` | 259 | UnwindData |  |
| 138 | `ASN1_TIME_free` | `0x1FE40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `ASN1_TIME_new` | `0x1FE50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `ASN1_TIME_to_tm` | `0x1FE60` | 92 | UnwindData |  |
| 3243 | `d2i_ASN1_TIME` | `0x1FEC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3447 | `i2d_ASN1_TIME` | `0x1FED0` | 1,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `ASN1_GENERALIZEDTIME_adj` | `0x20660` | 121 | UnwindData |  |
| 46 | `ASN1_GENERALIZEDTIME_check` | `0x206E0` | 57 | UnwindData |  |
| 51 | `ASN1_GENERALIZEDTIME_set` | `0x207A0` | 101 | UnwindData |  |
| 52 | `ASN1_GENERALIZEDTIME_set_string` | `0x20810` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `ASN1_TIME_adj` | `0x20830` | 22 | UnwindData |  |
| 134 | `ASN1_TIME_check` | `0x20950` | 198 | UnwindData |  |
| 135 | `ASN1_TIME_cmp_time_t` | `0x20A20` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `ASN1_TIME_compare` | `0x20B90` | 400 | UnwindData |  |
| 141 | `ASN1_TIME_normalize` | `0x20D20` | 61 | UnwindData |  |
| 143 | `ASN1_TIME_set` | `0x20E30` | 28 | UnwindData |  |
| 144 | `ASN1_TIME_set_string` | `0x20E50` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `ASN1_TIME_set_string_X509` | `0x20E50` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `ASN1_TIME_set_tm` | `0x20F40` | 70 | UnwindData |  |
| 147 | `ASN1_TIME_to_generalizedtime` | `0x20F90` | 43 | UnwindData |  |
| 163 | `ASN1_UTCTIME_adj` | `0x21080` | 121 | UnwindData |  |
| 164 | `ASN1_UTCTIME_check` | `0x21100` | 57 | UnwindData |  |
| 165 | `ASN1_UTCTIME_cmp_time_t` | `0x211C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 170 | `ASN1_UTCTIME_set` | `0x211E0` | 101 | UnwindData |  |
| 171 | `ASN1_UTCTIME_set_string` | `0x21250` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 216 | `ASN1_time_parse` | `0x21270` | 31 | UnwindData |  |
| 218 | `ASN1_time_tm_cmp` | `0x21320` | 1,824 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `ASN1_TYPE_cmp` | `0x21A40` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `ASN1_TYPE_free` | `0x21AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 151 | `ASN1_TYPE_get` | `0x21AF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `ASN1_TYPE_get_int_octetstring` | `0x21B10` | 234 | UnwindData |  |
| 153 | `ASN1_TYPE_get_octetstring` | `0x21C00` | 38 | UnwindData |  |
| 154 | `ASN1_TYPE_new` | `0x21CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `ASN1_TYPE_set` | `0x21CC0` | 93 | UnwindData |  |
| 156 | `ASN1_TYPE_set1` | `0x21D20` | 252 | UnwindData |  |
| 157 | `ASN1_TYPE_set_int_octetstring` | `0x21E20` | 233 | UnwindData |  |
| 158 | `ASN1_TYPE_set_octetstring` | `0x21F10` | 142 | UnwindData |  |
| 3244 | `d2i_ASN1_TYPE` | `0x21FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3448 | `i2d_ASN1_TYPE` | `0x21FE0` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1343 | `EVP_PKEY_asn1_add0` | `0x22270` | 72 | UnwindData |  |
| 1344 | `EVP_PKEY_asn1_add_alias` | `0x222C0` | 171 | UnwindData |  |
| 1345 | `EVP_PKEY_asn1_copy` | `0x22370` | 157 | UnwindData |  |
| 1346 | `EVP_PKEY_asn1_find` | `0x22410` | 188 | UnwindData |  |
| 1347 | `EVP_PKEY_asn1_find_str` | `0x224D0` | 236 | UnwindData |  |
| 1348 | `EVP_PKEY_asn1_free` | `0x225C0` | 51 | UnwindData |  |
| 1349 | `EVP_PKEY_asn1_get0` | `0x22600` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1350 | `EVP_PKEY_asn1_get0_info` | `0x22630` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1351 | `EVP_PKEY_asn1_get_count` | `0x22690` | 39 | UnwindData |  |
| 1352 | `EVP_PKEY_asn1_new` | `0x226C0` | 183 | UnwindData |  |
| 1353 | `EVP_PKEY_asn1_set_check` | `0x22780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1354 | `EVP_PKEY_asn1_set_ctrl` | `0x22790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1355 | `EVP_PKEY_asn1_set_free` | `0x227A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1356 | `EVP_PKEY_asn1_set_param` | `0x227B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1357 | `EVP_PKEY_asn1_set_param_check` | `0x227F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1418 | `EVP_PKEY_meth_set_public_check` | `0x227F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1358 | `EVP_PKEY_asn1_set_private` | `0x22800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1359 | `EVP_PKEY_asn1_set_public` | `0x22810` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1360 | `EVP_PKEY_asn1_set_public_check` | `0x22840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1407 | `EVP_PKEY_meth_set_check` | `0x22840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1361 | `EVP_PKEY_asn1_set_security_bits` | `0x22850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 274 | `BIO_get_callback_ex` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 297 | `BIO_meth_get_write` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 635 | `CONF_imodule_get_value` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 773 | `CT_POLICY_EVAL_CTX_get0_log_store` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 841 | `DH_get0_g` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 906 | `DSA_get0_q` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1327 | `EVP_PKEY_CTX_get0_pkey` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1385 | `EVP_PKEY_get0_asn1` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1633 | `GOST_KEY_get0_private_key` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1875 | `OCSP_resp_get0_signature` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2048 | `PKCS12_SAFEBAG_get0_attrs` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2292 | `RSA_meth_get_pub_dec` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2426 | `TS_ACCURACY_get_micros` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2476 | `TS_REQ_get_policy_id` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2511 | `TS_RESP_get_tst_info` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2522 | `TS_STATUS_INFO_get0_failure_info` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2542 | `TS_TST_INFO_get_msg_imprint` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2603 | `UI_get0_user_data` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2908 | `X509_REVOKED_get0_extensions` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2928 | `X509_STORE_CTX_get0_cert` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2980 | `X509_STORE_get0_param` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3002 | `X509_TRUST_get0_name` | `0x22860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1121 | `ERR_load_ASN1_strings` | `0x22870` | 57 | UnwindData |  |
| 182 | `ASN1_generate_nconf` | `0x228B0` | 54 | UnwindData |  |
| 183 | `ASN1_generate_v3` | `0x228F0` | 1,014 | UnwindData |  |
| 188 | `ASN1_item_d2i_bio` | `0x23820` | 129 | UnwindData |  |
| 189 | `ASN1_item_d2i_fp` | `0x238B0` | 225 | UnwindData |  |
| 190 | `ASN1_item_digest` | `0x239A0` | 132 | UnwindData |  |
| 191 | `ASN1_item_dup` | `0x23A30` | 141 | UnwindData |  |
| 198 | `ASN1_item_i2d_bio` | `0x23AC0` | 196 | UnwindData |  |
| 199 | `ASN1_item_i2d_fp` | `0x23B90` | 307 | UnwindData |  |
| 201 | `ASN1_item_pack` | `0x23CD0` | 103 | UnwindData |  |
| 203 | `ASN1_item_sign` | `0x23DE0` | 160 | UnwindData |  |
| 204 | `ASN1_item_sign_ctx` | `0x23E80` | 154 | UnwindData |  |
| 205 | `ASN1_item_unpack` | `0x24250` | 86 | UnwindData |  |
| 206 | `ASN1_item_verify` | `0x242B0` | 252 | UnwindData |  |
| 179 | `ASN1_d2i_bio` | `0x24DC0` | 119 | UnwindData |  |
| 180 | `ASN1_d2i_fp` | `0x24E40` | 220 | UnwindData |  |
| 181 | `ASN1_dup` | `0x24F20` | 34 | UnwindData |  |
| 185 | `ASN1_i2d_bio` | `0x24FF0` | 220 | UnwindData |  |
| 186 | `ASN1_i2d_fp` | `0x250D0` | 343 | UnwindData |  |
| 184 | `ASN1_get_object` | `0x25230` | 352 | UnwindData |  |
| 209 | `ASN1_object_size` | `0x25390` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 212 | `ASN1_put_eoc` | `0x253D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 213 | `ASN1_put_object` | `0x253F0` | 271 | UnwindData |  |
| 210 | `ASN1_parse` | `0x25500` | 42 | UnwindData |  |
| 211 | `ASN1_parse_dump` | `0x25530` | 48 | UnwindData |  |
| 214 | `ASN1_tag2bit` | `0x25FE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 215 | `ASN1_tag2str` | `0x26010` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2407 | `SMIME_crlf_copy` | `0x262D0` | 410 | UnwindData |  |
| 2410 | `SMIME_text` | `0x26900` | 104 | UnwindData |  |
| 178 | `ASN1_add_oid_module` | `0x27D70` | 3,184 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1914 | `PBEPARAM_free` | `0x289E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1916 | `PBEPARAM_new` | `0x289F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2102 | `PKCS5_pbe_set` | `0x28A00` | 90 | UnwindData |  |
| 2103 | `PKCS5_pbe_set0_algor` | `0x28BC0` | 390 | UnwindData |  |
| 3324 | `d2i_PBEPARAM` | `0x28D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3527 | `i2d_PBEPARAM` | `0x28D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1911 | `PBE2PARAM_free` | `0x28D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1913 | `PBE2PARAM_new` | `0x28D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1917 | `PBKDF2PARAM_free` | `0x28D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1919 | `PBKDF2PARAM_new` | `0x28DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2100 | `PKCS5_pbe2_set` | `0x28DB0` | 31 | UnwindData |  |
| 2101 | `PKCS5_pbe2_set_iv` | `0x28DD0` | 670 | UnwindData |  |
| 2104 | `PKCS5_pbkdf2_set` | `0x29070` | 495 | UnwindData |  |
| 3323 | `d2i_PBE2PARAM` | `0x29260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3325 | `d2i_PBKDF2PARAM` | `0x29270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3526 | `i2d_PBE2PARAM` | `0x29280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3528 | `i2d_PBKDF2PARAM` | `0x29290` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2189 | `PKCS8_PRIV_KEY_INFO_free` | `0x292D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2191 | `PKCS8_PRIV_KEY_INFO_new` | `0x292E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 601 | `CMS_signed_add1_attr_by_NID` | `0x292F0` | 36 | UnwindData |  |
| 2196 | `PKCS8_pkey_add1_attr_by_NID` | `0x292F0` | 36 | UnwindData |  |
| 2197 | `PKCS8_pkey_get0` | `0x29320` | 128 | UnwindData |  |
| 273 | `BIO_get_callback_arg` | `0x293A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `BIO_meth_get_read` | `0x293A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 774 | `CT_POLICY_EVAL_CTX_get_time` | `0x293A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 900 | `DSA_get0_g` | `0x293A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1017 | `EC_KEY_get0_group` | `0x293A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1286 | `EVP_MD_CTX_md_data` | `0x293A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1326 | `EVP_PKEY_CTX_get0_peerkey` | `0x293A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1871 | `OCSP_resp_get0_certs` | `0x293A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2198 | `PKCS8_pkey_get0_attrs` | `0x293A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2272 | `RSA_get0_n` | `0x293A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2291 | `RSA_meth_get_priv_enc` | `0x293A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2475 | `TS_REQ_get_nonce` | `0x293A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2546 | `TS_TST_INFO_get_serial` | `0x293A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2854 | `X509_PURPOSE_get0_name` | `0x293A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2935 | `X509_STORE_CTX_get0_untrusted` | `0x293A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2983 | `X509_STORE_get_verify` | `0x293A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2199 | `PKCS8_pkey_set0` | `0x293B0` | 134 | UnwindData |  |
| 3346 | `d2i_PKCS8_PRIV_KEY_INFO` | `0x29440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3554 | `i2d_PKCS8_PRIV_KEY_INFO` | `0x29450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2751 | `X509_CRL_print` | `0x29460` | 149 | UnwindData |  |
| 2752 | `X509_CRL_print_fp` | `0x296D0` | 154 | UnwindData |  |
| 2892 | `X509_REQ_print` | `0x29770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2893 | `X509_REQ_print_ex` | `0x29780` | 1,508 | UnwindData |  |
| 2894 | `X509_REQ_print_fp` | `0x29D70` | 160 | UnwindData |  |
| 1714 | `NETSCAPE_SPKI_print` | `0x29E10` | 256 | UnwindData |  |
| 50 | `ASN1_GENERALIZEDTIME_print` | `0x29FC0` | 170 | UnwindData |  |
| 142 | `ASN1_TIME_print` | `0x2A1D0` | 29 | UnwindData |  |
| 169 | `ASN1_UTCTIME_print` | `0x2A3C0` | 128 | UnwindData |  |
| 2828 | `X509_NAME_print` | `0x2A580` | 290 | UnwindData |  |
| 3122 | `X509_ocspid_print` | `0x2A6B0` | 425 | UnwindData |  |
| 3123 | `X509_print` | `0x2A860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3124 | `X509_print_ex` | `0x2A870` | 1,318 | UnwindData |  |
| 3125 | `X509_print_ex_fp` | `0x2ADA0` | 174 | UnwindData |  |
| 3126 | `X509_print_fp` | `0x2AE50` | 160 | UnwindData |  |
| 3141 | `X509_signature_dump` | `0x2AEF0` | 265 | UnwindData |  |
| 3142 | `X509_signature_print` | `0x2B000` | 60 | UnwindData |  |
| 2711 | `X509_CERT_AUX_print` | `0x2B1F0` | 50 | UnwindData |  |
| 187 | `ASN1_item_d2i` | `0x2B490` | 165 | UnwindData |  |
| 192 | `ASN1_item_ex_d2i` | `0x2B540` | 159 | UnwindData |  |
| 194 | `ASN1_item_ex_i2d` | `0x2DB00` | 960 | UnwindData |  |
| 197 | `ASN1_item_i2d` | `0x2DEC0` | 2,480 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 193 | `ASN1_item_ex_free` | `0x2E870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 196 | `ASN1_item_free` | `0x2E880` | 24 | UnwindData |  |
| 195 | `ASN1_item_ex_new` | `0x2ECA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 200 | `ASN1_item_new` | `0x2ECB0` | 43 | UnwindData |  |
| 88 | `ASN1_PCTX_get_oid_flags` | `0x2F1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1220 | `EVP_CIPHER_iv_length` | `0x2F1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1296 | `EVP_MD_flags` | `0x2F1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 89 | `ASN1_PCTX_get_str_flags` | `0x2F1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1194 | `EVP_CIPHER_CTX_encrypting` | `0x2F1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1218 | `EVP_CIPHER_flags` | `0x2F1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2803 | `X509_NAME_ENTRY_set` | `0x2F1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | `ASN1_PCTX_new` | `0x2F1F0` | 67 | UnwindData |  |
| 91 | `ASN1_PCTX_set_cert_flags` | `0x2F240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `ASN1_PCTX_set_nm_flags` | `0x2F250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | `ASN1_PCTX_set_oid_flags` | `0x2F260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `ASN1_PCTX_set_str_flags` | `0x2F270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | `ASN1_item_print` | `0x2F280` | 81 | UnwindData |  |
| 34 | `ASN1_BMPSTRING_free` | `0x2FDD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `ASN1_BMPSTRING_new` | `0x2FDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `ASN1_GENERALIZEDTIME_free` | `0x2FDF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `ASN1_GENERALIZEDTIME_new` | `0x2FE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `ASN1_GENERALSTRING_free` | `0x2FE10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `ASN1_GENERALSTRING_new` | `0x2FE20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 56 | `ASN1_IA5STRING_free` | `0x2FE30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 58 | `ASN1_IA5STRING_new` | `0x2FE40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `ASN1_NULL_free` | `0x2FE50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `ASN1_NULL_new` | `0x2FE60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `ASN1_PRINTABLESTRING_free` | `0x2FE70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `ASN1_PRINTABLESTRING_new` | `0x2FE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `ASN1_PRINTABLE_free` | `0x2FE90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `ASN1_PRINTABLE_new` | `0x2FEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 130 | `ASN1_T61STRING_free` | `0x2FEB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `ASN1_T61STRING_new` | `0x2FEC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 159 | `ASN1_UNIVERSALSTRING_free` | `0x2FED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 161 | `ASN1_UNIVERSALSTRING_new` | `0x2FEE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `ASN1_UTCTIME_free` | `0x2FEF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 168 | `ASN1_UTCTIME_new` | `0x2FF00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 172 | `ASN1_UTF8STRING_free` | `0x2FF10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `ASN1_UTF8STRING_new` | `0x2FF20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | `ASN1_VISIBLESTRING_free` | `0x2FF30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 177 | `ASN1_VISIBLESTRING_new` | `0x2FF40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 869 | `DIRECTORYSTRING_free` | `0x2FF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 871 | `DIRECTORYSTRING_new` | `0x2FF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 872 | `DISPLAYTEXT_free` | `0x2FF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 874 | `DISPLAYTEXT_new` | `0x2FF80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3229 | `d2i_ASN1_BMPSTRING` | `0x2FF90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3231 | `d2i_ASN1_GENERALIZEDTIME` | `0x2FFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3232 | `d2i_ASN1_GENERALSTRING` | `0x2FFB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3233 | `d2i_ASN1_IA5STRING` | `0x2FFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3235 | `d2i_ASN1_NULL` | `0x2FFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3238 | `d2i_ASN1_PRINTABLE` | `0x2FFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3239 | `d2i_ASN1_PRINTABLESTRING` | `0x2FFF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3240 | `d2i_ASN1_SEQUENCE_ANY` | `0x30000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3241 | `d2i_ASN1_SET_ANY` | `0x30010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3242 | `d2i_ASN1_T61STRING` | `0x30020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3246 | `d2i_ASN1_UNIVERSALSTRING` | `0x30030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3247 | `d2i_ASN1_UTCTIME` | `0x30040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3248 | `d2i_ASN1_UTF8STRING` | `0x30050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3249 | `d2i_ASN1_VISIBLESTRING` | `0x30060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3263 | `d2i_DIRECTORYSTRING` | `0x30070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3264 | `d2i_DISPLAYTEXT` | `0x30080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3433 | `i2d_ASN1_BMPSTRING` | `0x30090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3435 | `i2d_ASN1_GENERALIZEDTIME` | `0x300A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3436 | `i2d_ASN1_GENERALSTRING` | `0x300B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3437 | `i2d_ASN1_IA5STRING` | `0x300C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3439 | `i2d_ASN1_NULL` | `0x300D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3442 | `i2d_ASN1_PRINTABLE` | `0x300E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3443 | `i2d_ASN1_PRINTABLESTRING` | `0x300F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3444 | `i2d_ASN1_SEQUENCE_ANY` | `0x30100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3445 | `i2d_ASN1_SET_ANY` | `0x30110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3446 | `i2d_ASN1_T61STRING` | `0x30120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3449 | `i2d_ASN1_UNIVERSALSTRING` | `0x30130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3450 | `i2d_ASN1_UTCTIME` | `0x30140` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3451 | `i2d_ASN1_UTF8STRING` | `0x30150` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3452 | `i2d_ASN1_VISIBLESTRING` | `0x30160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3466 | `i2d_DIRECTORYSTRING` | `0x30170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3467 | `i2d_DISPLAYTEXT` | `0x30180` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2686 | `X509_ALGOR_cmp` | `0x30500` | 77 | UnwindData |  |
| 2687 | `X509_ALGOR_dup` | `0x30550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2688 | `X509_ALGOR_free` | `0x30560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2689 | `X509_ALGOR_get0` | `0x30570` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2691 | `X509_ALGOR_new` | `0x305B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2692 | `X509_ALGOR_set0` | `0x305C0` | 172 | UnwindData |  |
| 2693 | `X509_ALGOR_set_md` | `0x30670` | 189 | UnwindData |  |
| 3389 | `d2i_X509_ALGOR` | `0x30730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3390 | `d2i_X509_ALGORS` | `0x30740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3597 | `i2d_X509_ALGOR` | `0x30750` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3598 | `i2d_X509_ALGORS` | `0x30760` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2695 | `X509_ATTRIBUTE_create` | `0x30770` | 159 | UnwindData |  |
| 2699 | `X509_ATTRIBUTE_dup` | `0x30810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2700 | `X509_ATTRIBUTE_free` | `0x30820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2705 | `X509_ATTRIBUTE_new` | `0x30830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3391 | `d2i_X509_ATTRIBUTE` | `0x30840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3599 | `i2d_X509_ATTRIBUTE` | `0x30850` | 2,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2715 | `X509_CRL_INFO_free` | `0x31080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2717 | `X509_CRL_INFO_new` | `0x31090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2718 | `X509_CRL_METHOD_free` | `0x310A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2719 | `X509_CRL_METHOD_new` | `0x310B0` | 95 | UnwindData |  |
| 2720 | `X509_CRL_add0_revoked` | `0x31110` | 133 | UnwindData |  |
| 2726 | `X509_CRL_dup` | `0x311A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2727 | `X509_CRL_free` | `0x311B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2728 | `X509_CRL_get0_by_cert` | `0x311C0` | 51 | UnwindData |  |
| 2729 | `X509_CRL_get0_by_serial` | `0x31240` | 39 | UnwindData |  |
| 2730 | `X509_CRL_get0_extensions` | `0x31270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3081 | `X509_get_X509_PUBKEY` | `0x31270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2731 | `X509_CRL_get0_lastUpdate` | `0x31280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2743 | `X509_CRL_get_lastUpdate` | `0x31280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2888 | `X509_REQ_get_subject_name` | `0x31280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3098 | `X509_get_issuer_name` | `0x31280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2732 | `X509_CRL_get0_nextUpdate` | `0x31290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2745 | `X509_CRL_get_nextUpdate` | `0x31290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2733 | `X509_CRL_get0_signature` | `0x312A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2878 | `X509_REQ_get0_signature` | `0x312A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 307 | `BIO_method_name` | `0x312C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2734 | `X509_CRL_get0_tbs_sigalg` | `0x312C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3075 | `X509_get0_serialNumber` | `0x312C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3102 | `X509_get_serialNumber` | `0x312C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2735 | `X509_CRL_get_REVOKED` | `0x312D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3105 | `X509_get_subject_name` | `0x312D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1873 | `OCSP_resp_get0_produced_at` | `0x312E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2742 | `X509_CRL_get_issuer` | `0x312E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3077 | `X509_get0_tbs_sigalg` | `0x312E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2744 | `X509_CRL_get_meth_data` | `0x312F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2746 | `X509_CRL_get_signature_nid` | `0x31300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2887 | `X509_REQ_get_signature_nid` | `0x31300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3103 | `X509_get_signature_nid` | `0x31300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2747 | `X509_CRL_get_version` | `0x31310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3106 | `X509_get_version` | `0x31310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2750 | `X509_CRL_new` | `0x31320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2755 | `X509_CRL_set_default_method` | `0x31330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2758 | `X509_CRL_set_meth_data` | `0x31350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2765 | `X509_CRL_verify` | `0x31360` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2906 | `X509_REVOKED_dup` | `0x313A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2907 | `X509_REVOKED_free` | `0x313B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2918 | `X509_REVOKED_new` | `0x313C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3395 | `d2i_X509_CRL` | `0x313D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3396 | `d2i_X509_CRL_INFO` | `0x313E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3408 | `d2i_X509_REVOKED` | `0x313F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3603 | `i2d_X509_CRL` | `0x31400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3604 | `i2d_X509_CRL_INFO` | `0x31410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3616 | `i2d_X509_REVOKED` | `0x31420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2769 | `X509_EXTENSION_dup` | `0x31430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2770 | `X509_EXTENSION_free` | `0x31440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2775 | `X509_EXTENSION_new` | `0x31450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3399 | `d2i_X509_EXTENSION` | `0x31460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3400 | `d2i_X509_EXTENSIONS` | `0x31470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3607 | `i2d_X509_EXTENSION` | `0x31480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3608 | `i2d_X509_EXTENSIONS` | `0x31490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2779 | `X509_INFO_free` | `0x314A0` | 100 | UnwindData |  |
| 2780 | `X509_INFO_new` | `0x31510` | 79 | UnwindData |  |
| 2797 | `X509_NAME_ENTRY_dup` | `0x31C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2798 | `X509_NAME_ENTRY_free` | `0x31CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2802 | `X509_NAME_ENTRY_new` | `0x31CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2814 | `X509_NAME_dup` | `0x31CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2816 | `X509_NAME_free` | `0x31CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2817 | `X509_NAME_get0_der` | `0x31CE0` | 118 | UnwindData |  |
| 2826 | `X509_NAME_new` | `0x31D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2831 | `X509_NAME_set` | `0x31D70` | 38 | UnwindData |  |
| 3401 | `d2i_X509_NAME` | `0x31F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3402 | `d2i_X509_NAME_ENTRY` | `0x31F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3609 | `i2d_X509_NAME` | `0x31F40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3610 | `i2d_X509_NAME_ENTRY` | `0x31F50` | 752 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2841 | `X509_PKEY_free` | `0x32240` | 117 | UnwindData |  |
| 2842 | `X509_PKEY_new` | `0x322C0` | 249 | UnwindData |  |
| 2843 | `X509_PUBKEY_free` | `0x32820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2844 | `X509_PUBKEY_get` | `0x32830` | 368 | UnwindData |  |
| 2845 | `X509_PUBKEY_get0` | `0x329A0` | 319 | UnwindData |  |
| 2846 | `X509_PUBKEY_get0_param` | `0x32AE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2848 | `X509_PUBKEY_new` | `0x32B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2849 | `X509_PUBKEY_set` | `0x32B30` | 228 | UnwindData |  |
| 2850 | `X509_PUBKEY_set0_param` | `0x32C20` | 78 | UnwindData |  |
| 3271 | `d2i_DSA_PUBKEY` | `0x32C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3272 | `d2i_DSA_PUBKEY_bio` | `0x32C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3273 | `d2i_DSA_PUBKEY_fp` | `0x32CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3286 | `d2i_EC_PUBKEY` | `0x32CC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3287 | `d2i_EC_PUBKEY_bio` | `0x32CD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3288 | `d2i_EC_PUBKEY_fp` | `0x32CF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3354 | `d2i_PUBKEY` | `0x32D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3355 | `d2i_PUBKEY_bio` | `0x32D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3356 | `d2i_PUBKEY_fp` | `0x32D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3369 | `d2i_RSA_PUBKEY` | `0x32D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3370 | `d2i_RSA_PUBKEY_bio` | `0x32D70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3371 | `d2i_RSA_PUBKEY_fp` | `0x32D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3403 | `d2i_X509_PUBKEY` | `0x32DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3474 | `i2d_DSA_PUBKEY` | `0x32DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3475 | `i2d_DSA_PUBKEY_bio` | `0x32DD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3476 | `i2d_DSA_PUBKEY_fp` | `0x32DF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3489 | `i2d_EC_PUBKEY` | `0x32E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3490 | `i2d_EC_PUBKEY_bio` | `0x32E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3491 | `i2d_EC_PUBKEY_fp` | `0x32E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3562 | `i2d_PUBKEY` | `0x32E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3563 | `i2d_PUBKEY_bio` | `0x32E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3564 | `i2d_PUBKEY_fp` | `0x32E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3577 | `i2d_RSA_PUBKEY` | `0x32EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3578 | `i2d_RSA_PUBKEY_bio` | `0x32EC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3579 | `i2d_RSA_PUBKEY_fp` | `0x32EE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3611 | `i2d_X509_PUBKEY` | `0x32F00` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2862 | `X509_REQ_INFO_free` | `0x331E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2864 | `X509_REQ_INFO_new` | `0x331F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2874 | `X509_REQ_dup` | `0x33200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2876 | `X509_REQ_free` | `0x33210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2891 | `X509_REQ_new` | `0x33220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3404 | `d2i_X509_REQ` | `0x33230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3405 | `d2i_X509_REQ_INFO` | `0x33240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3612 | `i2d_X509_REQ` | `0x33250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3613 | `i2d_X509_REQ_INFO` | `0x33260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2921 | `X509_SIG_free` | `0x33270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 886 | `DSA_SIG_get0` | `0x33280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 941 | `ECDSA_SIG_get0` | `0x33280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2922 | `X509_SIG_get0` | `0x33280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2923 | `X509_SIG_getm` | `0x33280` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2925 | `X509_SIG_new` | `0x332A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3409 | `d2i_X509_SIG` | `0x332B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3617 | `i2d_X509_SIG` | `0x332C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1705 | `NETSCAPE_SPKAC_free` | `0x332D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1707 | `NETSCAPE_SPKAC_new` | `0x332E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1710 | `NETSCAPE_SPKI_free` | `0x332F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1713 | `NETSCAPE_SPKI_new` | `0x33300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3302 | `d2i_NETSCAPE_SPKAC` | `0x33310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3303 | `d2i_NETSCAPE_SPKI` | `0x33320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3505 | `i2d_NETSCAPE_SPKAC` | `0x33330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3506 | `i2d_NETSCAPE_SPKI` | `0x33340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3009 | `X509_VAL_free` | `0x33350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3011 | `X509_VAL_new` | `0x33360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3410 | `d2i_X509_VAL` | `0x33370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3618 | `i2d_X509_VAL` | `0x33380` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2712 | `X509_CINF_free` | `0x334A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2714 | `X509_CINF_new` | `0x334B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3065 | `X509_dup` | `0x334C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3069 | `X509_free` | `0x334D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3076 | `X509_get0_signature` | `0x334E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3088 | `X509_get_ex_data` | `0x33500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3089 | `X509_get_ex_new_index` | `0x33510` | 42 | UnwindData |  |
| 3121 | `X509_new` | `0x33540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3131 | `X509_set_ex_data` | `0x33550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3388 | `d2i_X509` | `0x33560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3392 | `d2i_X509_AUX` | `0x33570` | 170 | UnwindData |  |
| 3394 | `d2i_X509_CINF` | `0x33620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3596 | `i2d_X509` | `0x33630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3600 | `i2d_X509_AUX` | `0x33640` | 73 | UnwindData |  |
| 3602 | `i2d_X509_CINF` | `0x33690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3623 | `i2d_re_X509_tbs` | `0x336A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2708 | `X509_CERT_AUX_free` | `0x336C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2710 | `X509_CERT_AUX_new` | `0x336D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3043 | `X509_add1_reject_object` | `0x336E0` | 153 | UnwindData |  |
| 3044 | `X509_add1_trust_object` | `0x33780` | 151 | UnwindData |  |
| 3046 | `X509_alias_get0` | `0x33820` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3047 | `X509_alias_set1` | `0x33860` | 203 | UnwindData |  |
| 3116 | `X509_keyid_get0` | `0x33930` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3117 | `X509_keyid_set1` | `0x33970` | 203 | UnwindData |  |
| 3128 | `X509_reject_clear` | `0x33A40` | 63 | UnwindData |  |
| 3150 | `X509_trust_clear` | `0x33A80` | 61 | UnwindData |  |
| 3393 | `d2i_X509_CERT_AUX` | `0x33AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3601 | `i2d_X509_CERT_AUX` | `0x33AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 232 | `BF_cfb64_encrypt` | `0x33AE0` | 58 | UnwindData |  |
| 234 | `BF_ecb_encrypt` | `0x33CF0` | 178 | UnwindData |  |
| 231 | `BF_cbc_encrypt` | `0x33DB0` | 629 | UnwindData |  |
| 233 | `BF_decrypt` | `0x342B0` | 1,121 | UnwindData |  |
| 235 | `BF_encrypt` | `0x34720` | 1,121 | UnwindData |  |
| 236 | `BF_ofb64_encrypt` | `0x34B90` | 455 | UnwindData |  |
| 237 | `BF_set_key` | `0x34D60` | 858 | UnwindData |  |
| 253 | `BIO_dump` | `0x350C0` | 38 | UnwindData |  |
| 254 | `BIO_dump_cb` | `0x350F0` | 22 | UnwindData |  |
| 255 | `BIO_dump_fp` | `0x35110` | 38 | UnwindData |  |
| 256 | `BIO_dump_indent` | `0x35140` | 35 | UnwindData |  |
| 257 | `BIO_dump_indent_cb` | `0x35170` | 168 | UnwindData |  |
| 258 | `BIO_dump_indent_fp` | `0x354F0` | 35 | UnwindData |  |
| 325 | `BIO_printf` | `0x35550` | 97 | UnwindData |  |
| 352 | `BIO_snprintf` | `0x355C0` | 117 | UnwindData |  |
| 363 | `BIO_vprintf` | `0x35640` | 89 | UnwindData |  |
| 364 | `BIO_vsnprintf` | `0x356A0` | 122 | UnwindData |  |
| 241 | `BIO_accept` | `0x35720` | 422 | UnwindData |  |
| 271 | `BIO_get_accept_socket` | `0x358D0` | 174 | UnwindData |  |
| 278 | `BIO_get_host_ip` | `0x35C70` | 323 | UnwindData |  |
| 281 | `BIO_get_port` | `0x35DC0` | 330 | UnwindData |  |
| 285 | `BIO_gethostbyname` | `0x35F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 351 | `BIO_set_tcp_ndelay` | `0x35F20` | 51 | UnwindData |  |
| 354 | `BIO_sock_error` | `0x35F60` | 64 | UnwindData |  |
| 358 | `BIO_socket_ioctl` | `0x35FA0` | 67 | UnwindData |  |
| 261 | `BIO_f_buffer` | `0x36930` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 264 | `BIO_f_nbio_test` | `0x36C50` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `BIO_f_null` | `0x36D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `BIO_debug_callback` | `0x36D50` | 830 | UnwindData |  |
| 1122 | `ERR_load_BIO_strings` | `0x37090` | 57 | UnwindData |  |
| 242 | `BIO_callback_ctrl` | `0x370D0` | 62 | UnwindData |  |
| 243 | `BIO_clear_flags` | `0x37280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 244 | `BIO_copy_next_retry` | `0x37290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 245 | `BIO_ctrl` | `0x372B0` | 78 | UnwindData |  |
| 248 | `BIO_ctrl_pending` | `0x37470` | 27 | UnwindData |  |
| 250 | `BIO_ctrl_wpending` | `0x37490` | 27 | UnwindData |  |
| 259 | `BIO_dup_chain` | `0x374B0` | 833 | UnwindData |  |
| 268 | `BIO_find_type` | `0x37800` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 269 | `BIO_free` | `0x37830` | 22 | UnwindData |  |
| 270 | `BIO_free_all` | `0x37940` | 17 | UnwindData |  |
| 275 | `BIO_get_data` | `0x37A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 291 | `BIO_meth_get_create` | `0x37A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1329 | `EVP_PKEY_CTX_get_cb` | `0x37A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2275 | `RSA_get0_q` | `0x37A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2287 | `RSA_meth_get_init` | `0x37A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2543 | `TS_TST_INFO_get_nonce` | `0x37A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2950 | `X509_STORE_CTX_get_verify` | `0x37A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `BIO_get_ex_data` | `0x37AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2277 | `RSA_get_ex_data` | `0x37AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `BIO_get_ex_new_index` | `0x37AB0` | 42 | UnwindData |  |
| 279 | `BIO_get_init` | `0x37AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1332 | `EVP_PKEY_CTX_get_operation` | `0x37AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3021 | `X509_VERIFY_PARAM_get_depth` | `0x37AE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 280 | `BIO_get_new_index` | `0x37AF0` | 63 | UnwindData |  |
| 282 | `BIO_get_retry_BIO` | `0x37B30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 283 | `BIO_get_retry_reason` | `0x37B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `BIO_get_shutdown` | `0x37B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 286 | `BIO_gets` | `0x37B80` | 66 | UnwindData |  |
| 287 | `BIO_indent` | `0x37E00` | 62 | UnwindData |  |
| 288 | `BIO_int_ctrl` | `0x37E40` | 24 | UnwindData |  |
| 308 | `BIO_method_type` | `0x37E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1204 | `EVP_CIPHER_CTX_nid` | `0x37E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 309 | `BIO_new` | `0x37E70` | 235 | UnwindData |  |
| 321 | `BIO_next` | `0x37F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 322 | `BIO_number_read` | `0x37F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 323 | `BIO_number_written` | `0x37F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 324 | `BIO_pop` | `0x37F90` | 105 | UnwindData |  |
| 326 | `BIO_ptr_ctrl` | `0x38000` | 43 | UnwindData |  |
| 327 | `BIO_push` | `0x38030` | 118 | UnwindData |  |
| 328 | `BIO_puts` | `0x380B0` | 63 | UnwindData |  |
| 329 | `BIO_read` | `0x382F0` | 135 | UnwindData |  |
| 339 | `BIO_set` | `0x385C0` | 171 | UnwindData |  |
| 340 | `BIO_set_callback` | `0x38670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1414 | `EVP_PKEY_meth_set_init` | `0x38670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 341 | `BIO_set_callback_arg` | `0x38680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 779 | `CT_POLICY_EVAL_CTX_set_time` | `0x38680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1408 | `EVP_PKEY_meth_set_cleanup` | `0x38680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2958 | `X509_STORE_CTX_set0_untrusted` | `0x38680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2961 | `X509_STORE_CTX_set_chain` | `0x38680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2996 | `X509_STORE_set_verify` | `0x38680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 342 | `BIO_set_callback_ex` | `0x38690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 778 | `CT_POLICY_EVAL_CTX_set_shared_CTLOG_STORE` | `0x38690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1409 | `EVP_PKEY_meth_set_copy` | `0x38690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2960 | `X509_STORE_CTX_set_cert` | `0x38690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 344 | `BIO_set_data` | `0x386A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1337 | `EVP_PKEY_CTX_set_cb` | `0x386A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2972 | `X509_STORE_CTX_set_verify` | `0x386A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 345 | `BIO_set_ex_data` | `0x386B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2337 | `RSA_set_ex_data` | `0x386B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 346 | `BIO_set_flags` | `0x386C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 347 | `BIO_set_init` | `0x386D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3035 | `X509_VERIFY_PARAM_set_depth` | `0x386D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 348 | `BIO_set_next` | `0x386E0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 349 | `BIO_set_retry_reason` | `0x38720` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 350 | `BIO_set_shutdown` | `0x38730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3034 | `X509_VERIFY_PARAM_set_auth_level` | `0x38730` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 360 | `BIO_test_flags` | `0x38740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 361 | `BIO_up_ref` | `0x38750` | 49 | UnwindData |  |
| 362 | `BIO_vfree` | `0x38790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 365 | `BIO_write` | `0x387A0` | 48 | UnwindData |  |
| 290 | `BIO_meth_get_callback_ctrl` | `0x38A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 548 | `CMS_SignerInfo_get0_md_ctx` | `0x38A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2267 | `RSA_get0_dmq1` | `0x38A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2541 | `TS_TST_INFO_get_exts` | `0x38A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 292 | `BIO_meth_get_ctrl` | `0x38A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1328 | `EVP_PKEY_CTX_get_app_data` | `0x38A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2273 | `RSA_get0_p` | `0x38A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2284 | `RSA_meth_get_bn_mod_exp` | `0x38A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2932 | `X509_STORE_CTX_get0_param` | `0x38A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2981 | `X509_STORE_get_check_issued` | `0x38A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 293 | `BIO_meth_get_destroy` | `0x38AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 847 | `DH_get0_q` | `0x38AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2266 | `RSA_get0_dmp1` | `0x38AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2285 | `RSA_meth_get_finish` | `0x38AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2548 | `TS_TST_INFO_get_tsa` | `0x38AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2951 | `X509_STORE_CTX_get_verify_cb` | `0x38AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3019 | `X509_VERIFY_PARAM_get0_peername` | `0x38AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `BIO_meth_get_gets` | `0x38AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 550 | `CMS_SignerInfo_get0_signature` | `0x38AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 767 | `CTLOG_get0_public_key` | `0x38AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 845 | `DH_get0_priv_key` | `0x38AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 904 | `DSA_get0_priv_key` | `0x38AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1018 | `EC_KEY_get0_private_key` | `0x38AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1330 | `EVP_PKEY_CTX_get_data` | `0x38AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2265 | `RSA_get0_d` | `0x38AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2289 | `RSA_meth_get_mod_exp` | `0x38AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2359 | `SCT_get_timestamp` | `0x38AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2473 | `TS_REQ_get_exts` | `0x38AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2534 | `TS_TST_INFO_get_accuracy` | `0x38AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 295 | `BIO_meth_get_puts` | `0x38AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 634 | `CONF_imodule_get_usr_data` | `0x38AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 642 | `CONF_module_get_usr_data` | `0x38AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 846 | `DH_get0_pub_key` | `0x38AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 905 | `DSA_get0_pub_key` | `0x38AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1019 | `EC_KEY_get0_public_key` | `0x38AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1288 | `EVP_MD_CTX_pkey_ctx` | `0x38AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1380 | `EVP_PKEY_get0` | `0x38AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2268 | `RSA_get0_e` | `0x38AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2290 | `RSA_meth_get_priv_dec` | `0x38AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2547 | `TS_TST_INFO_get_time` | `0x38AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2855 | `X509_PURPOSE_get0_sname` | `0x38AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2984 | `X509_STORE_get_verify_cb` | `0x38AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 298 | `BIO_meth_new` | `0x38AD0` | 63 | UnwindData |  |
| 299 | `BIO_meth_set_callback_ctrl` | `0x38B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1226 | `EVP_CIPHER_meth_set_ctrl` | `0x38B10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 300 | `BIO_meth_set_create` | `0x38B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 915 | `DSA_meth_set_finish` | `0x38B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1233 | `EVP_CIPHER_meth_set_set_asn1_params` | `0x38B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2302 | `RSA_meth_set_init` | `0x38B20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 301 | `BIO_meth_set_ctrl` | `0x38B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1301 | `EVP_MD_meth_set_cleanup` | `0x38B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2299 | `RSA_meth_set_bn_mod_exp` | `0x38B30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 302 | `BIO_meth_set_destroy` | `0x38B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1229 | `EVP_CIPHER_meth_set_get_asn1_params` | `0x38B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1303 | `EVP_MD_meth_set_ctrl` | `0x38B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2300 | `RSA_meth_set_finish` | `0x38B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 303 | `BIO_meth_set_gets` | `0x38B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1225 | `EVP_CIPHER_meth_set_cleanup` | `0x38B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1302 | `EVP_MD_meth_set_copy` | `0x38B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2304 | `RSA_meth_set_mod_exp` | `0x38B50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 304 | `BIO_meth_set_puts` | `0x38B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1227 | `EVP_CIPHER_meth_set_do_cipher` | `0x38B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1304 | `EVP_MD_meth_set_final` | `0x38B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2305 | `RSA_meth_set_priv_dec` | `0x38B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 305 | `BIO_meth_set_read` | `0x38B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1231 | `EVP_CIPHER_meth_set_init` | `0x38B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1309 | `EVP_MD_meth_set_update` | `0x38B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2306 | `RSA_meth_set_priv_enc` | `0x38B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 306 | `BIO_meth_set_write` | `0x38B80` | 2,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1306 | `EVP_MD_meth_set_init` | `0x38B80` | 2,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2307 | `RSA_meth_set_pub_dec` | `0x38B80` | 2,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 312 | `BIO_new_accept` | `0x39420` | 91 | UnwindData |  |
| 330 | `BIO_s_accept` | `0x39480` | 2,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 246 | `BIO_ctrl_get_read_request` | `0x39F30` | 27 | UnwindData |  |
| 247 | `BIO_ctrl_get_write_guarantee` | `0x39F50` | 27 | UnwindData |  |
| 249 | `BIO_ctrl_reset_read_request` | `0x39F70` | 34 | UnwindData |  |
| 313 | `BIO_new_bio_pair` | `0x39FA0` | 243 | UnwindData |  |
| 331 | `BIO_s_bio` | `0x3A0A0` | 1,648 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 239 | `BIO_CONNECT_free` | `0x3A710` | 45 | UnwindData |  |
| 240 | `BIO_CONNECT_new` | `0x3A740` | 66 | UnwindData |  |
| 314 | `BIO_new_connect` | `0x3A790` | 91 | UnwindData |  |
| 332 | `BIO_s_connect` | `0x3A7F0` | 3,680 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `BIO_dgram_non_fatal_error` | `0x3B650` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 315 | `BIO_new_dgram` | `0x3B670` | 93 | UnwindData |  |
| 333 | `BIO_s_datagram` | `0x3B6D0` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 266 | `BIO_fd_non_fatal_error` | `0x3BBB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 356 | `BIO_sock_non_fatal_error` | `0x3BBB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 267 | `BIO_fd_should_retry` | `0x3BBE0` | 64 | UnwindData |  |
| 357 | `BIO_sock_should_retry` | `0x3BBE0` | 64 | UnwindData |  |
| 316 | `BIO_new_fd` | `0x3BC20` | 93 | UnwindData |  |
| 334 | `BIO_s_fd` | `0x3BC80` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 317 | `BIO_new_file` | `0x3C160` | 261 | UnwindData |  |
| 318 | `BIO_new_fp` | `0x3C270` | 94 | UnwindData |  |
| 335 | `BIO_s_file` | `0x3C2D0` | 1,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 319 | `BIO_new_mem_buf` | `0x3CA20` | 212 | UnwindData |  |
| 336 | `BIO_s_mem` | `0x3CB00` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 337 | `BIO_s_null` | `0x3CBB0` | 976 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 320 | `BIO_new_socket` | `0x3CF80` | 93 | UnwindData |  |
| 338 | `BIO_s_socket` | `0x3CFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 383 | `BN_add` | `0x3CFF0` | 154 | UnwindData |  |
| 474 | `BN_sub` | `0x3D090` | 159 | UnwindData |  |
| 480 | `BN_uadd` | `0x3D130` | 148 | UnwindData |  |
| 482 | `BN_usub` | `0x3D1D0` | 100 | UnwindData |  |
| 409 | `BN_get_rfc2409_prime_1024` | `0x3E430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 410 | `BN_get_rfc2409_prime_768` | `0x3E450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 411 | `BN_get_rfc3526_prime_1536` | `0x3E470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 412 | `BN_get_rfc3526_prime_2048` | `0x3E490` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 413 | `BN_get_rfc3526_prime_3072` | `0x3E4B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 414 | `BN_get_rfc3526_prime_4096` | `0x3E4D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 415 | `BN_get_rfc3526_prime_6144` | `0x3E4F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 416 | `BN_get_rfc3526_prime_8192` | `0x3E510` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 385 | `BN_asc2bn` | `0x3E530` | 284 | UnwindData |  |
| 386 | `BN_bin2bn` | `0x3E650` | 58 | UnwindData |  |
| 387 | `BN_bn2bin` | `0x3E750` | 228 | UnwindData |  |
| 388 | `BN_bn2binpad` | `0x3E840` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 389 | `BN_bn2dec` | `0x3E860` | 73 | UnwindData |  |
| 390 | `BN_bn2hex` | `0x3EA50` | 53 | UnwindData |  |
| 391 | `BN_bn2lebinpad` | `0x3EA90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 392 | `BN_bn2mpi` | `0x3EAB0` | 107 | UnwindData |  |
| 399 | `BN_dec2bn` | `0x3EC10` | 105 | UnwindData |  |
| 418 | `BN_hex2bn` | `0x3EC80` | 105 | UnwindData |  |
| 428 | `BN_lebin2bn` | `0x3ECF0` | 255 | UnwindData |  |
| 452 | `BN_mpi2bn` | `0x3EDF0` | 76 | UnwindData |  |
| 366 | `BN_CTX_end` | `0x3F7A0` | 109 | UnwindData |  |
| 367 | `BN_CTX_free` | `0x3F810` | 10 | UnwindData |  |
| 368 | `BN_CTX_get` | `0x3F880` | 338 | UnwindData |  |
| 369 | `BN_CTX_new` | `0x3F9E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1280 | `EVP_MD_CTX_create` | `0x3F9E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1287 | `EVP_MD_CTX_new` | `0x3F9E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 370 | `BN_CTX_start` | `0x3F9F0` | 64 | UnwindData |  |
| 400 | `BN_div` | `0x3FA30` | 123 | UnwindData |  |
| 1123 | `ERR_load_BN_strings` | `0x401E0` | 57 | UnwindData |  |
| 403 | `BN_exp` | `0x40220` | 130 | UnwindData |  |
| 434 | `BN_mod_exp` | `0x403B0` | 107 | UnwindData |  |
| 435 | `BN_mod_exp2_mont` | `0x40420` | 228 | UnwindData |  |
| 436 | `BN_mod_exp_mont` | `0x40C30` | 117 | UnwindData |  |
| 437 | `BN_mod_exp_mont_consttime` | `0x40CB0` | 176 | UnwindData |  |
| 438 | `BN_mod_exp_mont_word` | `0x415F0` | 297 | UnwindData |  |
| 439 | `BN_mod_exp_simple` | `0x41DD0` | 140 | UnwindData |  |
| 406 | `BN_gcd` | `0x423C0` | 71 | UnwindData |  |
| 440 | `BN_mod_inverse` | `0x42810` | 113 | UnwindData |  |
| 427 | `BN_kronecker` | `0x43590` | 65 | UnwindData |  |
| 372 | `BN_GENCB_free` | `0x43800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 374 | `BN_GENCB_new` | `0x43810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 375 | `BN_GENCB_set` | `0x43820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 376 | `BN_GENCB_set_old` | `0x43830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 382 | `BN_abs_is_word` | `0x43840` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 393 | `BN_clear` | `0x43870` | 44 | UnwindData |  |
| 394 | `BN_clear_bit` | `0x438A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 395 | `BN_clear_free` | `0x43900` | 70 | UnwindData |  |
| 404 | `BN_free` | `0x43900` | 70 | UnwindData |  |
| 396 | `BN_cmp` | `0x43950` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 397 | `BN_consttime_swap` | `0x43990` | 185 | UnwindData |  |
| 398 | `BN_copy` | `0x43C60` | 118 | UnwindData |  |
| 402 | `BN_dup` | `0x43CE0` | 270 | UnwindData |  |
| 408 | `BN_get_flags` | `0x43DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 417 | `BN_get_word` | `0x43E00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 419 | `BN_is_bit_set` | `0x43E30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 420 | `BN_is_negative` | `0x43E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 421 | `BN_is_odd` | `0x43E70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 422 | `BN_is_one` | `0x43E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 425 | `BN_is_word` | `0x43EB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 426 | `BN_is_zero` | `0x43EE0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 431 | `BN_mask_bits` | `0x43F90` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 455 | `BN_new` | `0x44000` | 79 | UnwindData |  |
| 457 | `BN_num_bits` | `0x44050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 458 | `BN_num_bits_word` | `0x44060` | 23 | UnwindData |  |
| 459 | `BN_one` | `0x44080` | 157 | UnwindData |  |
| 468 | `BN_security_bits` | `0x44120` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 469 | `BN_set_bit` | `0x44190` | 143 | UnwindData |  |
| 470 | `BN_set_flags` | `0x44220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 471 | `BN_set_negative` | `0x44230` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 472 | `BN_set_word` | `0x44270` | 168 | UnwindData |  |
| 476 | `BN_swap` | `0x44320` | 120 | UnwindData |  |
| 481 | `BN_ucmp` | `0x445B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 483 | `BN_value_one` | `0x44620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 484 | `BN_with_flags` | `0x44630` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 485 | `BN_zero` | `0x44660` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 432 | `BN_mod_add` | `0x44850` | 108 | UnwindData |  |
| 433 | `BN_mod_add_quick` | `0x448C0` | 137 | UnwindData |  |
| 441 | `BN_mod_lshift` | `0x44970` | 224 | UnwindData |  |
| 442 | `BN_mod_lshift1` | `0x44B20` | 124 | UnwindData |  |
| 443 | `BN_mod_lshift1_quick` | `0x44BA0` | 137 | UnwindData |  |
| 444 | `BN_mod_lshift_quick` | `0x44C30` | 286 | UnwindData |  |
| 445 | `BN_mod_mul` | `0x44D50` | 96 | UnwindData |  |
| 447 | `BN_mod_sqr` | `0x44E40` | 84 | UnwindData |  |
| 449 | `BN_mod_sub` | `0x44F10` | 108 | UnwindData |  |
| 450 | `BN_mod_sub_quick` | `0x44F80` | 156 | UnwindData |  |
| 456 | `BN_nnmod` | `0x45020` | 147 | UnwindData |  |
| 448 | `BN_mod_sqrt` | `0x450C0` | 127 | UnwindData |  |
| 377 | `BN_MONT_CTX_copy` | `0x45B70` | 98 | UnwindData |  |
| 378 | `BN_MONT_CTX_free` | `0x45BE0` | 51 | UnwindData |  |
| 379 | `BN_MONT_CTX_new` | `0x45C20` | 69 | UnwindData |  |
| 380 | `BN_MONT_CTX_set` | `0x45C70` | 54 | UnwindData |  |
| 381 | `BN_MONT_CTX_set_locked` | `0x45EB0` | 76 | UnwindData |  |
| 405 | `BN_from_montgomery` | `0x45FF0` | 136 | UnwindData |  |
| 446 | `BN_mod_mul_montgomery` | `0x46080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 479 | `BN_to_montgomery` | `0x46090` | 29 | UnwindData |  |
| 453 | `BN_mul` | `0x46910` | 341 | UnwindData |  |
| 371 | `BN_GENCB_call` | `0x47960` | 96 | UnwindData |  |
| 407 | `BN_generate_prime_ex` | `0x479C0` | 54 | UnwindData |  |
| 423 | `BN_is_prime_ex` | `0x47D20` | 335 | UnwindData |  |
| 424 | `BN_is_prime_fasttest_ex` | `0x47E70` | 320 | UnwindData |  |
| 460 | `BN_print` | `0x483D0` | 108 | UnwindData |  |
| 461 | `BN_print_fp` | `0x48440` | 108 | UnwindData |  |
| 462 | `BN_pseudo_rand` | `0x48890` | 33 | UnwindData |  |
| 463 | `BN_pseudo_rand_range` | `0x488C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 464 | `BN_rand` | `0x488D0` | 30 | UnwindData |  |
| 465 | `BN_rand_range` | `0x488F0` | 2,384 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 429 | `BN_lshift` | `0x49240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 430 | `BN_lshift1` | `0x49250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 466 | `BN_rshift` | `0x49260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 467 | `BN_rshift1` | `0x49270` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 473 | `BN_sqr` | `0x49510` | 127 | UnwindData |  |
| 384 | `BN_add_word` | `0x4A430` | 404 | UnwindData |  |
| 401 | `BN_div_word` | `0x4A5D0` | 91 | UnwindData |  |
| 451 | `BN_mod_word` | `0x4A6C0` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 454 | `BN_mul_word` | `0x4A710` | 124 | UnwindData |  |
| 475 | `BN_sub_word` | `0x4A790` | 273 | UnwindData |  |
| 1124 | `ERR_load_BUF_strings` | `0x4A8B0` | 57 | UnwindData |  |
| 486 | `BUF_MEM_free` | `0x4A8F0` | 40 | UnwindData |  |
| 487 | `BUF_MEM_grow` | `0x4A920` | 124 | UnwindData |  |
| 488 | `BUF_MEM_grow_clean` | `0x4A920` | 124 | UnwindData |  |
| 489 | `BUF_MEM_new` | `0x4AA30` | 67 | UnwindData |  |
| 589 | `CMS_get0_type` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 632 | `CONF_imodule_get_module` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 766 | `CTLOG_get0_name` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 771 | `CT_POLICY_EVAL_CTX_get0_cert` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 912 | `DSA_meth_get0_name` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 942 | `ECDSA_SIG_get0_r` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 985 | `EC_GROUP_method_of` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1025 | `EC_KEY_get_method` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1061 | `EC_POINT_method_of` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1189 | `EVP_CIPHER_CTX_cipher` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1632 | `GOST_KEY_get0_group` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1654 | `HMAC_CTX_get_md` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1829 | `OCSP_SINGLERESP_get0_id` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1856 | `OCSP_onereq_get0_id` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1874 | `OCSP_resp_get0_respdata` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2052 | `PKCS12_SAFEBAG_get0_type` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2283 | `RSA_meth_get0_name` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2428 | `TS_ACCURACY_get_seconds` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2453 | `TS_MSG_IMPRINT_get_algo` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2509 | `TS_RESP_get_status_info` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2523 | `TS_STATUS_INFO_get0_status` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2608 | `UI_get_method` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2910 | `X509_REVOKED_get0_serialNumber` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2934 | `X509_STORE_CTX_get0_store` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2979 | `X509_STORE_get0_objects` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3018 | `X509_VERIFY_PARAM_get0_name` | `0x4B370` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 781 | `Camellia_cfb128_encrypt` | `0x4B7D0` | 57 | UnwindData |  |
| 782 | `Camellia_cfb1_encrypt` | `0x4B810` | 57 | UnwindData |  |
| 783 | `Camellia_cfb8_encrypt` | `0x4B850` | 57 | UnwindData |  |
| 784 | `Camellia_ctr128_encrypt` | `0x4B890` | 59 | UnwindData |  |
| 786 | `Camellia_ecb_encrypt` | `0x4B8D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 785 | `Camellia_decrypt` | `0x4B8E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 787 | `Camellia_encrypt` | `0x4B900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 789 | `Camellia_set_key` | `0x4B920` | 87 | UnwindData |  |
| 788 | `Camellia_ofb128_encrypt` | `0x4B980` | 46 | UnwindData |  |
| 491 | `CAST_cfb64_encrypt` | `0x4B9B0` | 58 | UnwindData |  |
| 493 | `CAST_ecb_encrypt` | `0x4BBC0` | 178 | UnwindData |  |
| 490 | `CAST_cbc_encrypt` | `0x4BC80` | 629 | UnwindData |  |
| 492 | `CAST_decrypt` | `0x4C180` | 1,264 | UnwindData |  |
| 494 | `CAST_encrypt` | `0x4C670` | 1,258 | UnwindData |  |
| 495 | `CAST_ofb64_encrypt` | `0x4CB60` | 455 | UnwindData |  |
| 496 | `CAST_set_key` | `0x4CD30` | 5,978 | UnwindData |  |
| 677 | `CRYPTO_chacha_20` | `0x4E490` | 176 | UnwindData |  |
| 720 | `CRYPTO_hchacha_20` | `0x4E5B0` | 1,266 | UnwindData |  |
| 757 | `CRYPTO_xchacha_20` | `0x4EAB0` | 149 | UnwindData |  |
| 790 | `ChaCha` | `0x4EBA0` | 107 | UnwindData |  |
| 791 | `ChaCha_set_iv` | `0x4EC60` | 25 | UnwindData |  |
| 792 | `ChaCha_set_key` | `0x4EC80` | 27 | UnwindData |  |
| 501 | `CMAC_CTX_cleanup` | `0x4FF60` | 98 | UnwindData |  |
| 502 | `CMAC_CTX_copy` | `0x4FFD0` | 45 | UnwindData |  |
| 503 | `CMAC_CTX_free` | `0x50090` | 110 | UnwindData |  |
| 504 | `CMAC_CTX_get0_cipher_ctx` | `0x50100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 505 | `CMAC_CTX_new` | `0x50110` | 57 | UnwindData |  |
| 506 | `CMAC_Final` | `0x50150` | 318 | UnwindData |  |
| 507 | `CMAC_Init` | `0x50290` | 448 | UnwindData |  |
| 508 | `CMAC_Update` | `0x50450` | 283 | UnwindData |  |
| 509 | `CMAC_resume` | `0x50570` | 50 | UnwindData |  |
| 544 | `CMS_SharedInfo_encode` | `0x507D0` | 121 | UnwindData |  |
| 600 | `CMS_signed_add1_attr` | `0x50850` | 28 | UnwindData |  |
| 602 | `CMS_signed_add1_attr_by_OBJ` | `0x50870` | 36 | UnwindData |  |
| 603 | `CMS_signed_add1_attr_by_txt` | `0x508A0` | 36 | UnwindData |  |
| 604 | `CMS_signed_delete_attr` | `0x508D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 605 | `CMS_signed_get0_data_by_OBJ` | `0x508E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 606 | `CMS_signed_get_attr` | `0x508F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 607 | `CMS_signed_get_attr_by_NID` | `0x50900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 608 | `CMS_signed_get_attr_by_OBJ` | `0x50910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 609 | `CMS_signed_get_attr_count` | `0x50920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 612 | `CMS_unsigned_add1_attr` | `0x50930` | 28 | UnwindData |  |
| 1339 | `EVP_PKEY_add1_attr` | `0x50930` | 28 | UnwindData |  |
| 613 | `CMS_unsigned_add1_attr_by_NID` | `0x50950` | 36 | UnwindData |  |
| 1340 | `EVP_PKEY_add1_attr_by_NID` | `0x50950` | 36 | UnwindData |  |
| 614 | `CMS_unsigned_add1_attr_by_OBJ` | `0x50980` | 36 | UnwindData |  |
| 1341 | `EVP_PKEY_add1_attr_by_OBJ` | `0x50980` | 36 | UnwindData |  |
| 615 | `CMS_unsigned_add1_attr_by_txt` | `0x509B0` | 36 | UnwindData |  |
| 1342 | `EVP_PKEY_add1_attr_by_txt` | `0x509B0` | 36 | UnwindData |  |
| 616 | `CMS_unsigned_delete_attr` | `0x509E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1372 | `EVP_PKEY_delete_attr` | `0x509E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 617 | `CMS_unsigned_get0_data_by_OBJ` | `0x509F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 618 | `CMS_unsigned_get_attr` | `0x50A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1391 | `EVP_PKEY_get_attr` | `0x50A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 619 | `CMS_unsigned_get_attr_by_NID` | `0x50A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1392 | `EVP_PKEY_get_attr_by_NID` | `0x50A10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 620 | `CMS_unsigned_get_attr_by_OBJ` | `0x50A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1393 | `EVP_PKEY_get_attr_by_OBJ` | `0x50A20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 621 | `CMS_unsigned_get_attr_count` | `0x50A30` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1394 | `EVP_PKEY_get_attr_count` | `0x50A30` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 516 | `CMS_EncryptedData_set1_key` | `0x50C70` | 51 | UnwindData |  |
| 517 | `CMS_EnvelopedData_create` | `0x512D0` | 153 | UnwindData |  |
| 525 | `CMS_RecipientInfo_decrypt` | `0x51410` | 97 | UnwindData |  |
| 526 | `CMS_RecipientInfo_encrypt` | `0x51480` | 47 | UnwindData |  |
| 527 | `CMS_RecipientInfo_get0_pkey_ctx` | `0x51690` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 535 | `CMS_RecipientInfo_kekri_get0_id` | `0x516B0` | 180 | UnwindData |  |
| 536 | `CMS_RecipientInfo_kekri_id_cmp` | `0x51770` | 107 | UnwindData |  |
| 537 | `CMS_RecipientInfo_ktri_cert_cmp` | `0x517E0` | 72 | UnwindData |  |
| 538 | `CMS_RecipientInfo_ktri_get0_algs` | `0x51830` | 102 | UnwindData |  |
| 539 | `CMS_RecipientInfo_ktri_get0_signer_id` | `0x518A0` | 69 | UnwindData |  |
| 540 | `CMS_RecipientInfo_set0_key` | `0x518F0` | 74 | UnwindData |  |
| 542 | `CMS_RecipientInfo_set0_pkey` | `0x51940` | 107 | UnwindData |  |
| 561 | `CMS_add0_recipient_key` | `0x519B0` | 586 | UnwindData |  |
| 566 | `CMS_add1_recipient_cert` | `0x51C00` | 500 | UnwindData |  |
| 584 | `CMS_get0_RecipientInfos` | `0x51E00` | 91 | UnwindData |  |
| 1125 | `ERR_load_CMS_strings` | `0x52800` | 64 | UnwindData |  |
| 518 | `CMS_ReceiptRequest_create0` | `0x52840` | 264 | UnwindData |  |
| 519 | `CMS_ReceiptRequest_free` | `0x52950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 520 | `CMS_ReceiptRequest_get0_values` | `0x52960` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 522 | `CMS_ReceiptRequest_new` | `0x529C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 563 | `CMS_add1_ReceiptRequest` | `0x529D0` | 148 | UnwindData |  |
| 590 | `CMS_get1_ReceiptRequest` | `0x52A70` | 168 | UnwindData |  |
| 3257 | `d2i_CMS_ReceiptRequest` | `0x530B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3459 | `i2d_CMS_ReceiptRequest` | `0x530C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 310 | `BIO_new_CMS` | `0x530D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 610 | `CMS_stream` | `0x530E0` | 136 | UnwindData |  |
| 1937 | `PEM_read_CMS` | `0x53170` | 44 | UnwindData |  |
| 1958 | `PEM_read_bio_CMS` | `0x531A0` | 44 | UnwindData |  |
| 1980 | `PEM_write_CMS` | `0x531D0` | 60 | UnwindData |  |
| 2004 | `PEM_write_bio_CMS` | `0x53210` | 60 | UnwindData |  |
| 2005 | `PEM_write_bio_CMS_stream` | `0x53250` | 38 | UnwindData |  |
| 2408 | `SMIME_read_CMS` | `0x53280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2411 | `SMIME_write_CMS` | `0x53290` | 144 | UnwindData |  |
| 3258 | `d2i_CMS_bio` | `0x53320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3460 | `i2d_CMS_bio` | `0x53340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3461 | `i2d_CMS_bio_stream` | `0x53360` | 26 | UnwindData |  |
| 523 | `CMS_RecipientEncryptedKey_cert_cmp` | `0x53380` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 524 | `CMS_RecipientEncryptedKey_get0_id` | `0x533B0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 528 | `CMS_RecipientInfo_kari_decrypt` | `0x53460` | 177 | UnwindData |  |
| 529 | `CMS_RecipientInfo_kari_get0_alg` | `0x53520` | 99 | UnwindData |  |
| 530 | `CMS_RecipientInfo_kari_get0_ctx` | `0x53590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 531 | `CMS_RecipientInfo_kari_get0_orig_id` | `0x535B0` | 248 | UnwindData |  |
| 532 | `CMS_RecipientInfo_kari_get0_reks` | `0x536B0` | 65 | UnwindData |  |
| 533 | `CMS_RecipientInfo_kari_orig_id_cmp` | `0x53700` | 110 | UnwindData |  |
| 534 | `CMS_RecipientInfo_kari_set0_pkey` | `0x53770` | 110 | UnwindData |  |
| 510 | `CMS_ContentInfo_free` | `0x53CA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 512 | `CMS_ContentInfo_new` | `0x53CB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 513 | `CMS_ContentInfo_print_ctx` | `0x53CC0` | 26 | UnwindData |  |
| 552 | `CMS_SignerInfo_get_version` | `0x53CE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 557 | `CMS_add0_CertificateChoices` | `0x53CF0` | 121 | UnwindData |  |
| 558 | `CMS_add0_RevocationInfoChoice` | `0x53D70` | 121 | UnwindData |  |
| 559 | `CMS_add0_cert` | `0x53DF0` | 274 | UnwindData |  |
| 560 | `CMS_add0_crl` | `0x53F10` | 151 | UnwindData |  |
| 564 | `CMS_add1_cert` | `0x53FB0` | 53 | UnwindData |  |
| 565 | `CMS_add1_crl` | `0x540D0` | 159 | UnwindData |  |
| 573 | `CMS_dataFinal` | `0x54170` | 40 | UnwindData |  |
| 574 | `CMS_dataInit` | `0x54300` | 353 | UnwindData |  |
| 586 | `CMS_get0_content` | `0x54470` | 211 | UnwindData |  |
| 587 | `CMS_get0_eContentType` | `0x54550` | 27 | UnwindData |  |
| 591 | `CMS_get1_certs` | `0x54570` | 169 | UnwindData |  |
| 592 | `CMS_get1_crls` | `0x54620` | 169 | UnwindData |  |
| 593 | `CMS_get_version` | `0x546D0` | 133 | UnwindData |  |
| 594 | `CMS_is_detached` | `0x54760` | 40 | UnwindData |  |
| 595 | `CMS_set1_eContentType` | `0x54790` | 87 | UnwindData |  |
| 597 | `CMS_set_detached` | `0x547F0` | 150 | UnwindData |  |
| 3256 | `d2i_CMS_ContentInfo` | `0x54ED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3458 | `i2d_CMS_ContentInfo` | `0x54EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 541 | `CMS_RecipientInfo_set0_password` | `0x54EF0` | 105 | UnwindData |  |
| 562 | `CMS_add0_recipient_password` | `0x54F60` | 181 | UnwindData |  |
| 545 | `CMS_SignedData_init` | `0x559F0` | 24 | UnwindData |  |
| 546 | `CMS_SignerInfo_cert_cmp` | `0x55A10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 547 | `CMS_SignerInfo_get0_algs` | `0x55A40` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 549 | `CMS_SignerInfo_get0_pkey_ctx` | `0x55A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 973 | `EC_GROUP_get0_seed` | `0x55A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2270 | `RSA_get0_iqmp` | `0x55A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2282 | `RSA_meth_get0_app_data` | `0x55A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2942 | `X509_STORE_CTX_get_check_issued` | `0x55A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 551 | `CMS_SignerInfo_get0_signer_id` | `0x55A90` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 553 | `CMS_SignerInfo_set1_signer_cert` | `0x55AE0` | 74 | UnwindData |  |
| 554 | `CMS_SignerInfo_sign` | `0x55B30` | 11 | UnwindData |  |
| 555 | `CMS_SignerInfo_verify` | `0x55DA0` | 360 | UnwindData |  |
| 556 | `CMS_SignerInfo_verify_content` | `0x55F10` | 641 | UnwindData |  |
| 567 | `CMS_add1_signer` | `0x561A0` | 106 | UnwindData |  |
| 568 | `CMS_add_simple_smimecap` | `0x56B90` | 78 | UnwindData |  |
| 569 | `CMS_add_smimecap` | `0x56C80` | 97 | UnwindData |  |
| 570 | `CMS_add_standard_smimecap` | `0x56CF0` | 343 | UnwindData |  |
| 585 | `CMS_get0_SignerInfos` | `0x56E50` | 91 | UnwindData |  |
| 588 | `CMS_get0_signers` | `0x56EB0` | 217 | UnwindData |  |
| 596 | `CMS_set1_signers_certs` | `0x56F90` | 157 | UnwindData |  |
| 514 | `CMS_EncryptedData_decrypt` | `0x57AA0` | 297 | UnwindData |  |
| 515 | `CMS_EncryptedData_encrypt` | `0x57BD0` | 78 | UnwindData |  |
| 571 | `CMS_compress` | `0x57CA0` | 47 | UnwindData |  |
| 572 | `CMS_data` | `0x57CD0` | 166 | UnwindData |  |
| 575 | `CMS_data_create` | `0x57D80` | 105 | UnwindData |  |
| 576 | `CMS_decrypt` | `0x57DF0` | 164 | UnwindData |  |
| 577 | `CMS_decrypt_set1_key` | `0x57F70` | 294 | UnwindData |  |
| 578 | `CMS_decrypt_set1_password` | `0x580A0` | 224 | UnwindData |  |
| 579 | `CMS_decrypt_set1_pkey` | `0x58180` | 692 | UnwindData |  |
| 580 | `CMS_digest_create` | `0x58440` | 138 | UnwindData |  |
| 581 | `CMS_digest_verify` | `0x584D0` | 160 | UnwindData |  |
| 582 | `CMS_encrypt` | `0x58600` | 458 | UnwindData |  |
| 583 | `CMS_final` | `0x587D0` | 262 | UnwindData |  |
| 598 | `CMS_sign` | `0x588E0` | 336 | UnwindData |  |
| 599 | `CMS_sign_receipt` | `0x58A30` | 72 | UnwindData |  |
| 611 | `CMS_uncompress` | `0x58C70` | 47 | UnwindData |  |
| 622 | `CMS_verify` | `0x58CA0` | 1,774 | UnwindData |  |
| 623 | `CMS_verify_receipt` | `0x59390` | 85 | UnwindData |  |
| 3200 | `_CONF_add_string` | `0x595C0` | 140 | UnwindData |  |
| 3201 | `_CONF_free_data` | `0x59650` | 79 | UnwindData |  |
| 3202 | `_CONF_get_section` | `0x596A0` | 54 | UnwindData |  |
| 3203 | `_CONF_get_section_values` | `0x596E0` | 63 | UnwindData |  |
| 3204 | `_CONF_get_string` | `0x59720` | 124 | UnwindData |  |
| 3205 | `_CONF_new_data` | `0x597A0` | 79 | UnwindData |  |
| 3206 | `_CONF_new_section` | `0x597F0` | 212 | UnwindData |  |
| 1692 | `NCONF_WIN32` | `0x5A3C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1693 | `NCONF_default` | `0x5A3D0` | 1,440 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1126 | `ERR_load_CONF_strings` | `0x5A970` | 57 | UnwindData |  |
| 624 | `CONF_dump_bio` | `0x5A9B0` | 94 | UnwindData |  |
| 625 | `CONF_dump_fp` | `0x5AA10` | 173 | UnwindData |  |
| 626 | `CONF_free` | `0x5AAC0` | 79 | UnwindData |  |
| 628 | `CONF_get_number` | `0x5AB10` | 477 | UnwindData |  |
| 629 | `CONF_get_section` | `0x5ACF0` | 143 | UnwindData |  |
| 630 | `CONF_get_string` | `0x5AD80` | 245 | UnwindData |  |
| 638 | `CONF_load` | `0x5AE80` | 145 | UnwindData |  |
| 639 | `CONF_load_bio` | `0x5AF20` | 123 | UnwindData |  |
| 640 | `CONF_load_fp` | `0x5AFA0` | 140 | UnwindData |  |
| 650 | `CONF_set_default_method` | `0x5B030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 651 | `CONF_set_nconf` | `0x5B040` | 68 | UnwindData |  |
| 1694 | `NCONF_dump_bio` | `0x5B090` | 70 | UnwindData |  |
| 1695 | `NCONF_dump_fp` | `0x5B0E0` | 168 | UnwindData |  |
| 1696 | `NCONF_free` | `0x5B190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1697 | `NCONF_free_data` | `0x5B1B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1698 | `NCONF_get_number_e` | `0x5B1D0` | 81 | UnwindData |  |
| 1699 | `NCONF_get_section` | `0x5B310` | 109 | UnwindData |  |
| 1700 | `NCONF_get_string` | `0x5B380` | 159 | UnwindData |  |
| 1701 | `NCONF_load` | `0x5B420` | 70 | UnwindData |  |
| 1702 | `NCONF_load_bio` | `0x5B470` | 70 | UnwindData |  |
| 1703 | `NCONF_load_fp` | `0x5B4C0` | 189 | UnwindData |  |
| 1704 | `NCONF_new` | `0x5B580` | 78 | UnwindData |  |
| 1897 | `OPENSSL_load_builtin_modules` | `0x5B5D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 627 | `CONF_get1_default_config_file` | `0x5B5E0` | 59 | UnwindData |  |
| 631 | `CONF_imodule_get_flags` | `0x5B620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 851 | `DH_get_length` | `0x5B620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 636 | `CONF_imodule_set_flags` | `0x5B630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 637 | `CONF_imodule_set_usr_data` | `0x5B640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 643 | `CONF_module_set_usr_data` | `0x5B640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2997 | `X509_STORE_set_verify_cb` | `0x5B640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 641 | `CONF_module_add` | `0x5B650` | 166 | UnwindData |  |
| 644 | `CONF_modules_finish` | `0x5B700` | 20 | UnwindData |  |
| 645 | `CONF_modules_free` | `0x5B7A0` | 4 | UnwindData |  |
| 646 | `CONF_modules_load` | `0x5B840` | 206 | UnwindData |  |
| 647 | `CONF_modules_load_file` | `0x5B910` | 371 | UnwindData |  |
| 648 | `CONF_modules_unload` | `0x5BA90` | 181 | UnwindData |  |
| 649 | `CONF_parse_list` | `0x5BB50` | 326 | UnwindData |  |
| 1892 | `OPENSSL_config` | `0x5BF20` | 69 | UnwindData |  |
| 1898 | `OPENSSL_no_config` | `0x5BFF0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 769 | `CTLOG_new_from_base64` | `0x5C090` | 137 | UnwindData |  |
| 2363 | `SCT_new_from_base64` | `0x5C1D0` | 477 | UnwindData |  |
| 759 | `CTLOG_STORE_free` | `0x5C4F0` | 42 | UnwindData |  |
| 760 | `CTLOG_STORE_get0_log_by_id` | `0x5C520` | 129 | UnwindData |  |
| 761 | `CTLOG_STORE_load_default_file` | `0x5C5B0` | 304 | UnwindData |  |
| 762 | `CTLOG_STORE_load_file` | `0x5C6E0` | 302 | UnwindData |  |
| 763 | `CTLOG_STORE_new` | `0x5C810` | 111 | UnwindData |  |
| 764 | `CTLOG_free` | `0x5C880` | 44 | UnwindData |  |
| 765 | `CTLOG_get0_log_id` | `0x5C8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 768 | `CTLOG_new` | `0x5C8C0` | 320 | UnwindData |  |
| 3372 | `d2i_SCT_LIST` | `0x5CB80` | 79 | UnwindData |  |
| 3580 | `i2d_SCT_LIST` | `0x5CD30` | 385 | UnwindData |  |
| 3625 | `i2o_SCT` | `0x5CEC0` | 607 | UnwindData |  |
| 3626 | `i2o_SCT_LIST` | `0x5D120` | 185 | UnwindData |  |
| 3658 | `o2i_SCT` | `0x5D330` | 131 | UnwindData |  |
| 3659 | `o2i_SCT_LIST` | `0x5D3C0` | 345 | UnwindData |  |
| 770 | `CT_POLICY_EVAL_CTX_free` | `0x5D8C0` | 44 | UnwindData |  |
| 775 | `CT_POLICY_EVAL_CTX_new` | `0x5D8F0` | 106 | UnwindData |  |
| 776 | `CT_POLICY_EVAL_CTX_set1_cert` | `0x5D960` | 58 | UnwindData |  |
| 777 | `CT_POLICY_EVAL_CTX_set1_issuer` | `0x5D9A0` | 59 | UnwindData |  |
| 2350 | `SCT_LIST_print` | `0x5DAF0` | 81 | UnwindData |  |
| 2364 | `SCT_print` | `0x5DE70` | 706 | UnwindData |  |
| 2377 | `SCT_validation_status_string` | `0x5E140` | 144 | UnwindData |  |
| 2349 | `SCT_LIST_free` | `0x5E1D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2351 | `SCT_LIST_validate` | `0x5E1E0` | 460 | UnwindData |  |
| 2352 | `SCT_free` | `0x5E3B0` | 63 | UnwindData |  |
| 2353 | `SCT_get0_extensions` | `0x5E3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2354 | `SCT_get0_log_id` | `0x5E400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2355 | `SCT_get0_signature` | `0x5E410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2356 | `SCT_get_log_entry_type` | `0x5E420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2357 | `SCT_get_signature_nid` | `0x5E430` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2358 | `SCT_get_source` | `0x5E460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2360 | `SCT_get_validation_status` | `0x5E470` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2362 | `SCT_new` | `0x5E4D0` | 85 | UnwindData |  |
| 2365 | `SCT_set0_extensions` | `0x5E530` | 64 | UnwindData |  |
| 2366 | `SCT_set0_log_id` | `0x5E570` | 134 | UnwindData |  |
| 2367 | `SCT_set0_signature` | `0x5E600` | 64 | UnwindData |  |
| 2368 | `SCT_set1_extensions` | `0x5E640` | 169 | UnwindData |  |
| 2369 | `SCT_set1_log_id` | `0x5E6F0` | 234 | UnwindData |  |
| 2370 | `SCT_set1_signature` | `0x5E7E0` | 169 | UnwindData |  |
| 2371 | `SCT_set_log_entry_type` | `0x5E890` | 76 | UnwindData |  |
| 2372 | `SCT_set_signature_nid` | `0x5E8E0` | 106 | UnwindData |  |
| 2373 | `SCT_set_source` | `0x5E950` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2374 | `SCT_set_timestamp` | `0x5E980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2375 | `SCT_set_version` | `0x5E990` | 68 | UnwindData |  |
| 2376 | `SCT_validate` | `0x5EA10` | 73 | UnwindData |  |
| 1005 | `EC_KEY_METHOD_set_compute_key` | `0x5EF80` | 1,488 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1082 | `ED25519_keypair` | `0x5F550` | 255 | UnwindData |  |
| 1083 | `ED25519_sign` | `0x5F740` | 433 | UnwindData |  |
| 1084 | `ED25519_verify` | `0x5F900` | 560 | UnwindData |  |
| 2640 | `X25519` | `0x5FB30` | 50 | UnwindData |  |
| 2641 | `X25519_keypair` | `0x5FB70` | 68 | UnwindData |  |
| 793 | `DES_cbc_cksum` | `0x67B20` | 11 | UnwindData |  |
| 794 | `DES_cbc_encrypt` | `0x67D60` | 670 | UnwindData |  |
| 805 | `DES_ede3_cfb64_encrypt` | `0x68280` | 57 | UnwindData |  |
| 806 | `DES_ede3_cfb_encrypt` | `0x684F0` | 114 | UnwindData |  |
| 795 | `DES_cfb64_encrypt` | `0x68D50` | 58 | UnwindData |  |
| 796 | `DES_cfb_encrypt` | `0x68F80` | 116 | UnwindData |  |
| 800 | `DES_decrypt3` | `0x69620` | 365 | UnwindData |  |
| 803 | `DES_ede3_cbc_encrypt` | `0x69790` | 1,308 | UnwindData |  |
| 810 | `DES_encrypt1` | `0x69CB0` | 5,059 | UnwindData |  |
| 811 | `DES_encrypt2` | `0x6B080` | 4,909 | UnwindData |  |
| 812 | `DES_encrypt3` | `0x6C3B0` | 368 | UnwindData |  |
| 816 | `DES_ncbc_encrypt` | `0x6C520` | 1,268 | UnwindData |  |
| 801 | `DES_ecb3_encrypt` | `0x6CA20` | 219 | UnwindData |  |
| 802 | `DES_ecb_encrypt` | `0x6CB00` | 187 | UnwindData |  |
| 804 | `DES_ede3_cbcm_encrypt` | `0x6CBC0` | 1,372 | UnwindData |  |
| 808 | `DES_enc_read` | `0x6D120` | 791 | UnwindData |  |
| 809 | `DES_enc_write` | `0x6D440` | 470 | UnwindData |  |
| 799 | `DES_crypt` | `0x6D620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 813 | `DES_fcrypt` | `0x6D630` | 652 | UnwindData |  |
| 807 | `DES_ede3_ofb64_encrypt` | `0x6E6D0` | 499 | UnwindData |  |
| 817 | `DES_ofb64_encrypt` | `0x6E8D0` | 449 | UnwindData |  |
| 818 | `DES_ofb_encrypt` | `0x6EAA0` | 46 | UnwindData |  |
| 819 | `DES_pcbc_encrypt` | `0x6EE40` | 972 | UnwindData |  |
| 820 | `DES_quad_cksum` | `0x6F210` | 327 | UnwindData |  |
| 821 | `DES_random_key` | `0x6F360` | 60 | UnwindData |  |
| 798 | `DES_check_key_parity` | `0x6F3A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 814 | `DES_is_weak_key` | `0x6F3D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 815 | `DES_key_sched` | `0x6F400` | 143 | UnwindData |  |
| 823 | `DES_set_key` | `0x6F490` | 20 | UnwindData |  |
| 824 | `DES_set_key_checked` | `0x6F540` | 122 | UnwindData |  |
| 825 | `DES_set_key_unchecked` | `0x6F5C0` | 1,696 | UnwindData |  |
| 826 | `DES_set_odd_parity` | `0x6FC60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 827 | `DES_string_to_2keys` | `0x6FCD0` | 417 | UnwindData |  |
| 828 | `DES_string_to_key` | `0x6FE80` | 305 | UnwindData |  |
| 829 | `DES_xcbc_encrypt` | `0x6FFC0` | 1,588 | UnwindData |  |
| 867 | `DHparams_print` | `0x70F90` | 31 | UnwindData |  |
| 868 | `DHparams_print_fp` | `0x70FB0` | 171 | UnwindData |  |
| 865 | `DHparams_dup` | `0x71270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3260 | `d2i_DHparams` | `0x71280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3261 | `d2i_DHparams_bio` | `0x71290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3262 | `d2i_DHparams_fp` | `0x712B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3463 | `i2d_DHparams` | `0x712D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3464 | `i2d_DHparams_bio` | `0x712E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3465 | `i2d_DHparams_fp` | `0x71300` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 832 | `DH_check` | `0x71320` | 56 | UnwindData |  |
| 833 | `DH_check_pub_key` | `0x716E0` | 53 | UnwindData |  |
| 1128 | `ERR_load_DH_strings` | `0x719B0` | 57 | UnwindData |  |
| 838 | `DH_generate_parameters` | `0x719F0` | 150 | UnwindData |  |
| 839 | `DH_generate_parameters_ex` | `0x71A90` | 37 | UnwindData |  |
| 830 | `DH_OpenSSL` | `0x72090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 835 | `DH_compute_key` | `0x720A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 837 | `DH_generate_key` | `0x720B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 831 | `DH_bits` | `0x720C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 890 | `DSA_bits` | `0x720C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 834 | `DH_clear_flags` | `0x720D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 836 | `DH_free` | `0x720E0` | 185 | UnwindData |  |
| 840 | `DH_get0_engine` | `0x721A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2492 | `TS_RESP_CTX_get_request` | `0x721A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 842 | `DH_get0_key` | `0x721B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 901 | `DSA_get0_key` | `0x721B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 844 | `DH_get0_pqg` | `0x721D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 848 | `DH_get_default_method` | `0x72200` | 33 | UnwindData |  |
| 849 | `DH_get_ex_data` | `0x72230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2982 | `X509_STORE_get_ex_data` | `0x72230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 850 | `DH_get_ex_new_index` | `0x72240` | 42 | UnwindData |  |
| 852 | `DH_new` | `0x72270` | 383 | UnwindData |  |
| 853 | `DH_new_method` | `0x72270` | 383 | UnwindData |  |
| 854 | `DH_security_bits` | `0x723F0` | 72 | UnwindData |  |
| 855 | `DH_set0_key` | `0x72440` | 81 | UnwindData |  |
| 856 | `DH_set0_pqg` | `0x724A0` | 149 | UnwindData |  |
| 857 | `DH_set_default_method` | `0x72540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 858 | `DH_set_ex_data` | `0x72550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2992 | `X509_STORE_set_ex_data` | `0x72550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 859 | `DH_set_flags` | `0x72560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 860 | `DH_set_length` | `0x72570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 861 | `DH_set_method` | `0x72580` | 73 | UnwindData |  |
| 862 | `DH_size` | `0x725D0` | 30 | UnwindData |  |
| 863 | `DH_test_flags` | `0x725F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 864 | `DH_up_ref` | `0x72600` | 49 | UnwindData |  |
| 889 | `DSA_SIG_set0` | `0x73BB0` | 97 | UnwindData |  |
| 928 | `DSA_sign` | `0x73C20` | 112 | UnwindData |  |
| 933 | `DSA_verify` | `0x73C90` | 188 | UnwindData |  |
| 934 | `DSAparams_dup` | `0x73D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3267 | `d2i_DSAPrivateKey` | `0x73D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3270 | `d2i_DSAPublicKey` | `0x73D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3274 | `d2i_DSA_SIG` | `0x73D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3275 | `d2i_DSAparams` | `0x73D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3276 | `d2i_DSAparams_bio` | `0x73DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3277 | `d2i_DSAparams_fp` | `0x73DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3470 | `i2d_DSAPrivateKey` | `0x73DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3473 | `i2d_DSAPublicKey` | `0x73DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3477 | `i2d_DSA_SIG` | `0x73E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3478 | `i2d_DSAparams` | `0x73E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3479 | `i2d_DSAparams_bio` | `0x73E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3480 | `i2d_DSAparams_fp` | `0x73E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1129 | `ERR_load_DSA_strings` | `0x73E60` | 57 | UnwindData |  |
| 897 | `DSA_generate_parameters` | `0x73EA0` | 134 | UnwindData |  |
| 898 | `DSA_generate_parameters_ex` | `0x73FC0` | 98 | UnwindData |  |
| 896 | `DSA_generate_key` | `0x74980` | 236 | UnwindData |  |
| 891 | `DSA_clear_flags` | `0x74A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 894 | `DSA_dup_DH` | `0x74A80` | 203 | UnwindData |  |
| 895 | `DSA_free` | `0x74B50` | 176 | UnwindData |  |
| 899 | `DSA_get0_engine` | `0x74C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2288 | `RSA_meth_get_keygen` | `0x74C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 903 | `DSA_get0_pqg` | `0x74C10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 907 | `DSA_get_default_method` | `0x74C40` | 33 | UnwindData |  |
| 908 | `DSA_get_ex_data` | `0x74C70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 909 | `DSA_get_ex_new_index` | `0x74C80` | 42 | UnwindData |  |
| 917 | `DSA_new` | `0x74CB0` | 374 | UnwindData |  |
| 918 | `DSA_new_method` | `0x74CB0` | 374 | UnwindData |  |
| 921 | `DSA_security_bits` | `0x74E30` | 20 | UnwindData |  |
| 922 | `DSA_set0_key` | `0x74E90` | 109 | UnwindData |  |
| 923 | `DSA_set0_pqg` | `0x74F00` | 150 | UnwindData |  |
| 924 | `DSA_set_default_method` | `0x74FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 925 | `DSA_set_ex_data` | `0x74FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 926 | `DSA_set_flags` | `0x74FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 927 | `DSA_set_method` | `0x74FD0` | 73 | UnwindData |  |
| 930 | `DSA_size` | `0x75020` | 44 | UnwindData |  |
| 931 | `DSA_test_flags` | `0x75050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 932 | `DSA_up_ref` | `0x75060` | 49 | UnwindData |  |
| 910 | `DSA_meth_dup` | `0x75300` | 133 | UnwindData |  |
| 911 | `DSA_meth_free` | `0x75390` | 35 | UnwindData |  |
| 2281 | `RSA_meth_free` | `0x75390` | 35 | UnwindData |  |
| 2591 | `UI_destroy_method` | `0x75390` | 35 | UnwindData |  |
| 913 | `DSA_meth_new` | `0x753C0` | 107 | UnwindData |  |
| 914 | `DSA_meth_set1_name` | `0x75430` | 105 | UnwindData |  |
| 916 | `DSA_meth_set_sign` | `0x754A0` | 2,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2308 | `RSA_meth_set_pub_enc` | `0x754A0` | 2,320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 884 | `DSA_OpenSSL` | `0x75DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 885 | `DSA_SIG_free` | `0x75DC0` | 44 | UnwindData |  |
| 888 | `DSA_SIG_new` | `0x75DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1179 | `EVP_AEAD_CTX_new` | `0x75DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 892 | `DSA_do_sign` | `0x75E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 893 | `DSA_do_verify` | `0x75E10` | 23 | UnwindData |  |
| 929 | `DSA_sign_setup` | `0x75E30` | 23 | UnwindData |  |
| 919 | `DSA_print` | `0x76540` | 121 | UnwindData |  |
| 920 | `DSA_print_fp` | `0x765C0` | 94 | UnwindData |  |
| 936 | `DSAparams_print` | `0x766A0` | 109 | UnwindData |  |
| 937 | `DSAparams_print_fp` | `0x76710` | 211 | UnwindData |  |
| 952 | `ECPARAMETERS_free` | `0x78090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 954 | `ECPARAMETERS_new` | `0x780A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 955 | `ECPKPARAMETERS_free` | `0x780B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 957 | `ECPKPARAMETERS_new` | `0x780C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1076 | `EC_PRIVATEKEY_free` | `0x780D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1078 | `EC_PRIVATEKEY_new` | `0x780E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3191 | `X9_62_CHARACTERISTIC_TWO_free` | `0x780F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3193 | `X9_62_CHARACTERISTIC_TWO_new` | `0x78100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3196 | `X9_62_PENTANOMIAL_free` | `0x78110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3198 | `X9_62_PENTANOMIAL_new` | `0x78120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3279 | `d2i_ECPKPARAMETERS` | `0x78130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3280 | `d2i_ECPKParameters` | `0x78140` | 184 | UnwindData |  |
| 3281 | `d2i_ECParameters` | `0x78200` | 37 | UnwindData |  |
| 3282 | `d2i_ECPrivateKey` | `0x783A0` | 206 | UnwindData |  |
| 3285 | `d2i_EC_PRIVATEKEY` | `0x78610` | 3,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3482 | `i2d_ECPKPARAMETERS` | `0x79320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3483 | `i2d_ECPKParameters` | `0x79330` | 193 | UnwindData |  |
| 3484 | `i2d_ECParameters` | `0x79400` | 64 | UnwindData |  |
| 3485 | `i2d_ECPrivateKey` | `0x79500` | 120 | UnwindData |  |
| 3488 | `i2d_EC_PRIVATEKEY` | `0x79850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3624 | `i2o_ECPublicKey` | `0x79860` | 101 | UnwindData |  |
| 3657 | `o2i_ECPublicKey` | `0x799B0` | 227 | UnwindData |  |
| 965 | `EC_GROUP_check` | `0x79AA0` | 238 | UnwindData |  |
| 987 | `EC_GROUP_new_by_curve_name` | `0x79C70` | 106 | UnwindData |  |
| 1079 | `EC_curve_nid2nist` | `0x79CE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1080 | `EC_curve_nist2nid` | `0x79D20` | 95 | UnwindData |  |
| 1081 | `EC_get_builtin_curves` | `0x79D80` | 1,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 988 | `EC_GROUP_new_curve_GFp` | `0x7A250` | 127 | UnwindData |  |
| 1130 | `ERR_load_EC_strings` | `0x7A2D0` | 57 | UnwindData |  |
| 1011 | `EC_KEY_check_key` | `0x7A310` | 524 | UnwindData |  |
| 1012 | `EC_KEY_clear_flags` | `0x7A520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1013 | `EC_KEY_copy` | `0x7A530` | 71 | UnwindData |  |
| 1014 | `EC_KEY_dup` | `0x7A6D0` | 81 | UnwindData |  |
| 1015 | `EC_KEY_free` | `0x7A730` | 144 | UnwindData |  |
| 1016 | `EC_KEY_generate_key` | `0x7A7C0` | 70 | UnwindData |  |
| 1020 | `EC_KEY_get_conv_form` | `0x7A810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1022 | `EC_KEY_get_enc_flags` | `0x7A820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1023 | `EC_KEY_get_ex_data` | `0x7A830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1024 | `EC_KEY_get_flags` | `0x7A840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1026 | `EC_KEY_new` | `0x7A850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1027 | `EC_KEY_new_by_curve_name` | `0x7A860` | 109 | UnwindData |  |
| 1029 | `EC_KEY_precompute_mult` | `0x7A8D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1032 | `EC_KEY_set_asn1_flag` | `0x7A8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1033 | `EC_KEY_set_conv_form` | `0x7A900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1035 | `EC_KEY_set_enc_flags` | `0x7A920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1036 | `EC_KEY_set_ex_data` | `0x7A930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1037 | `EC_KEY_set_flags` | `0x7A940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1038 | `EC_KEY_set_group` | `0x7A950` | 91 | UnwindData |  |
| 1040 | `EC_KEY_set_private_key` | `0x7A9B0` | 91 | UnwindData |  |
| 1041 | `EC_KEY_set_public_key` | `0x7AA10` | 95 | UnwindData |  |
| 1042 | `EC_KEY_set_public_key_affine_coordinates` | `0x7AA70` | 445 | UnwindData |  |
| 1043 | `EC_KEY_up_ref` | `0x7AC30` | 49 | UnwindData |  |
| 998 | `EC_KEY_METHOD_free` | `0x7AD80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 999 | `EC_KEY_METHOD_get_compute_key` | `0x7AD90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1000 | `EC_KEY_METHOD_get_init` | `0x7ADA0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1001 | `EC_KEY_METHOD_get_keygen` | `0x7AE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1002 | `EC_KEY_METHOD_get_sign` | `0x7AE10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1003 | `EC_KEY_METHOD_get_verify` | `0x7AE40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1004 | `EC_KEY_METHOD_new` | `0x7AE60` | 114 | UnwindData |  |
| 1006 | `EC_KEY_METHOD_set_init` | `0x7AEE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1007 | `EC_KEY_METHOD_set_keygen` | `0x7AF10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2973 | `X509_STORE_CTX_set_verify_cb` | `0x7AF10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1008 | `EC_KEY_METHOD_set_sign` | `0x7AF20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1009 | `EC_KEY_METHOD_set_verify` | `0x7AF30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1010 | `EC_KEY_OpenSSL` | `0x7AF40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1021 | `EC_KEY_get_default_method` | `0x7AF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1028 | `EC_KEY_new_method` | `0x7AF60` | 193 | UnwindData |  |
| 1034 | `EC_KEY_set_default_method` | `0x7B030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1039 | `EC_KEY_set_method` | `0x7B050` | 82 | UnwindData |  |
| 960 | `ECParameters_dup` | `0x7B0B0` | 37 | UnwindData |  |
| 966 | `EC_GROUP_check_discriminant` | `0x7B120` | 151 | UnwindData |  |
| 967 | `EC_GROUP_clear_free` | `0x7B1C0` | 20 | UnwindData |  |
| 971 | `EC_GROUP_free` | `0x7B1C0` | 20 | UnwindData |  |
| 968 | `EC_GROUP_cmp` | `0x7B250` | 110 | UnwindData |  |
| 969 | `EC_GROUP_copy` | `0x7B5B0` | 150 | UnwindData |  |
| 970 | `EC_GROUP_dup` | `0x7B770` | 24 | UnwindData |  |
| 974 | `EC_GROUP_get_asn1_flag` | `0x7B8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 976 | `EC_GROUP_get_cofactor` | `0x7B900` | 57 | UnwindData |  |
| 977 | `EC_GROUP_get_curve` | `0x7B940` | 180 | UnwindData |  |
| 978 | `EC_GROUP_get_curve_GFp` | `0x7B940` | 180 | UnwindData |  |
| 979 | `EC_GROUP_get_curve_name` | `0x7BA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 980 | `EC_GROUP_get_degree` | `0x7BA10` | 70 | UnwindData |  |
| 981 | `EC_GROUP_get_order` | `0x7BA60` | 54 | UnwindData |  |
| 982 | `EC_GROUP_get_point_conversion_form` | `0x7BAA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2286 | `RSA_meth_get_flags` | `0x7BAA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 983 | `EC_GROUP_get_seed_len` | `0x7BAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2274 | `RSA_get0_pss_params` | `0x7BAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2294 | `RSA_meth_get_sign` | `0x7BAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 986 | `EC_GROUP_new` | `0x7BAC0` | 114 | UnwindData |  |
| 989 | `EC_GROUP_order_bits` | `0x7BBF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 991 | `EC_GROUP_set_asn1_flag` | `0x7BC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 992 | `EC_GROUP_set_curve` | `0x7BC10` | 180 | UnwindData |  |
| 993 | `EC_GROUP_set_curve_GFp` | `0x7BC10` | 180 | UnwindData |  |
| 994 | `EC_GROUP_set_curve_name` | `0x7BCD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 995 | `EC_GROUP_set_generator` | `0x7BCE0` | 85 | UnwindData |  |
| 996 | `EC_GROUP_set_point_conversion_form` | `0x7BE40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 997 | `EC_GROUP_set_seed` | `0x7BE50` | 129 | UnwindData |  |
| 1045 | `EC_POINT_add` | `0x7BEE0` | 223 | UnwindData |  |
| 1047 | `EC_POINT_clear_free` | `0x7BFC0` | 50 | UnwindData |  |
| 1052 | `EC_POINT_free` | `0x7BFC0` | 50 | UnwindData |  |
| 1048 | `EC_POINT_cmp` | `0x7C000` | 208 | UnwindData |  |
| 1049 | `EC_POINT_copy` | `0x7C0D0` | 136 | UnwindData |  |
| 1050 | `EC_POINT_dbl` | `0x7C160` | 205 | UnwindData |  |
| 1051 | `EC_POINT_dup` | `0x7C230` | 110 | UnwindData |  |
| 1053 | `EC_POINT_get_Jprojective_coordinates_GFp` | `0x7C2A0` | 250 | UnwindData |  |
| 1054 | `EC_POINT_get_affine_coordinates` | `0x7C3A0` | 234 | UnwindData |  |
| 1055 | `EC_POINT_get_affine_coordinates_GFp` | `0x7C3A0` | 234 | UnwindData |  |
| 1057 | `EC_POINT_invert` | `0x7C490` | 221 | UnwindData |  |
| 1058 | `EC_POINT_is_at_infinity` | `0x7C570` | 124 | UnwindData |  |
| 1059 | `EC_POINT_is_on_curve` | `0x7C5F0` | 224 | UnwindData |  |
| 1060 | `EC_POINT_make_affine` | `0x7C6D0` | 221 | UnwindData |  |
| 1062 | `EC_POINT_mul` | `0x7C7B0` | 355 | UnwindData |  |
| 1063 | `EC_POINT_new` | `0x7C920` | 117 | UnwindData |  |
| 1068 | `EC_POINT_set_Jprojective_coordinates_GFp` | `0x7CA20` | 316 | UnwindData |  |
| 1069 | `EC_POINT_set_affine_coordinates` | `0x7CB60` | 297 | UnwindData |  |
| 1070 | `EC_POINT_set_affine_coordinates_GFp` | `0x7CB60` | 297 | UnwindData |  |
| 1073 | `EC_POINT_set_to_infinity` | `0x7CC90` | 121 | UnwindData |  |
| 1074 | `EC_POINTs_make_affine` | `0x7CD10` | 246 | UnwindData |  |
| 1075 | `EC_POINTs_mul` | `0x7CE10` | 71 | UnwindData |  |
| 1064 | `EC_POINT_oct2point` | `0x7DCA0` | 234 | UnwindData |  |
| 1067 | `EC_POINT_point2oct` | `0x7DD90` | 255 | UnwindData |  |
| 1071 | `EC_POINT_set_compressed_coordinates` | `0x7DE90` | 234 | UnwindData |  |
| 1072 | `EC_POINT_set_compressed_coordinates_GFp` | `0x7DE90` | 234 | UnwindData |  |
| 1046 | `EC_POINT_bn2point` | `0x7EDA0` | 207 | UnwindData |  |
| 1056 | `EC_POINT_hex2point` | `0x7EE70` | 110 | UnwindData |  |
| 1065 | `EC_POINT_point2bn` | `0x7EF90` | 192 | UnwindData |  |
| 1066 | `EC_POINT_point2hex` | `0x7F050` | 278 | UnwindData |  |
| 958 | `ECPKParameters_print` | `0x7F170` | 102 | UnwindData |  |
| 959 | `ECPKParameters_print_fp` | `0x7F330` | 476 | UnwindData |  |
| 961 | `ECParameters_print` | `0x7F510` | 109 | UnwindData |  |
| 962 | `ECParameters_print_fp` | `0x7F580` | 211 | UnwindData |  |
| 1030 | `EC_KEY_print` | `0x7F660` | 121 | UnwindData |  |
| 1031 | `EC_KEY_print_fp` | `0x7F6E0` | 94 | UnwindData |  |
| 963 | `EC_GFp_mont_method` | `0x800C0` | 12,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 964 | `EC_GFp_simple_method` | `0x82FF0` | 6,800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 938 | `ECDH_compute_key` | `0x84A80` | 157 | UnwindData |  |
| 939 | `ECDH_size` | `0x84C30` | 34 | UnwindData |  |
| 940 | `ECDSA_SIG_free` | `0x850E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 945 | `ECDSA_SIG_new` | `0x850F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 946 | `ECDSA_SIG_set0` | `0x85100` | 97 | UnwindData |  |
| 947 | `ECDSA_do_sign` | `0x85170` | 81 | UnwindData |  |
| 948 | `ECDSA_do_verify` | `0x851D0` | 70 | UnwindData |  |
| 949 | `ECDSA_sign` | `0x85220` | 114 | UnwindData |  |
| 950 | `ECDSA_size` | `0x852A0` | 84 | UnwindData |  |
| 951 | `ECDSA_verify` | `0x85300` | 94 | UnwindData |  |
| 3278 | `d2i_ECDSA_SIG` | `0x85360` | 4,208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3481 | `i2d_ECDSA_SIG` | `0x863D0` | 2,352 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1107 | `ERR_add_error_data` | `0x86D00` | 317 | UnwindData |  |
| 1108 | `ERR_add_error_vdata` | `0x86E40` | 327 | UnwindData |  |
| 1109 | `ERR_asprintf_error_data` | `0x86F90` | 52 | UnwindData |  |
| 1110 | `ERR_clear_error` | `0x87050` | 167 | UnwindData |  |
| 1111 | `ERR_error_string` | `0x87100` | 43 | UnwindData |  |
| 1112 | `ERR_error_string_n` | `0x87130` | 768 | UnwindData |  |
| 1113 | `ERR_free_strings` | `0x87430` | 134 | UnwindData |  |
| 1114 | `ERR_func_error_string` | `0x874C0` | 158 | UnwindData |  |
| 1115 | `ERR_get_error` | `0x87560` | 152 | UnwindData |  |
| 1116 | `ERR_get_error_line` | `0x87600` | 245 | UnwindData |  |
| 1117 | `ERR_get_error_line_data` | `0x87700` | 299 | UnwindData |  |
| 1118 | `ERR_get_next_error_library` | `0x87830` | 125 | UnwindData |  |
| 1119 | `ERR_get_state` | `0x878B0` | 658 | UnwindData |  |
| 1120 | `ERR_lib_error_string` | `0x87B50` | 81 | UnwindData |  |
| 1131 | `ERR_load_ERR_strings` | `0x87BB0` | 67 | UnwindData |  |
| 1146 | `ERR_load_strings` | `0x87EB0` | 131 | UnwindData |  |
| 1147 | `ERR_peek_error` | `0x87F40` | 60 | UnwindData |  |
| 1148 | `ERR_peek_error_line` | `0x87F80` | 154 | UnwindData |  |
| 1149 | `ERR_peek_error_line_data` | `0x88020` | 222 | UnwindData |  |
| 1150 | `ERR_peek_last_error` | `0x88100` | 43 | UnwindData |  |
| 1151 | `ERR_peek_last_error_line` | `0x88130` | 129 | UnwindData |  |
| 1152 | `ERR_peek_last_error_line_data` | `0x881C0` | 204 | UnwindData |  |
| 1153 | `ERR_pop_to_mark` | `0x88290` | 34 | UnwindData |  |
| 1157 | `ERR_put_error` | `0x88390` | 293 | UnwindData |  |
| 1158 | `ERR_reason_error_string` | `0x884C0` | 225 | UnwindData |  |
| 1159 | `ERR_remove_state` | `0x885B0` | 200 | UnwindData |  |
| 1160 | `ERR_remove_thread_state` | `0x88680` | 220 | UnwindData |  |
| 1161 | `ERR_set_error_data` | `0x88760` | 119 | UnwindData |  |
| 1162 | `ERR_set_mark` | `0x887E0` | 49 | UnwindData |  |
| 1163 | `ERR_unload_strings` | `0x88820` | 83 | UnwindData |  |
| 1145 | `ERR_load_crypto_strings` | `0x889C0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1154 | `ERR_print_errors` | `0x88A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1155 | `ERR_print_errors_cb` | `0x88A80` | 319 | UnwindData |  |
| 1156 | `ERR_print_errors_fp` | `0x88BC0` | 3,136 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 260 | `BIO_f_base64` | `0x89800` | 1,728 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 262 | `BIO_f_cipher` | `0x89EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 343 | `BIO_set_cipher` | `0x89ED0` | 263 | UnwindData |  |
| 263 | `BIO_f_md` | `0x8A3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1887 | `OPENSSL_add_all_algorithms_conf` | `0x8A3F0` | 75 | UnwindData |  |
| 1888 | `OPENSSL_add_all_algorithms_noconf` | `0x8A440` | 69 | UnwindData |  |
| 1907 | `OpenSSL_add_all_ciphers` | `0x8A490` | 2,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1908 | `OpenSSL_add_all_digests` | `0x8ACC0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1222 | `EVP_CIPHER_meth_dup` | `0x8AE90` | 89 | UnwindData |  |
| 1224 | `EVP_CIPHER_meth_new` | `0x8AEF0` | 82 | UnwindData |  |
| 1228 | `EVP_CIPHER_meth_set_flags` | `0x8AF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1230 | `EVP_CIPHER_meth_set_impl_ctx_size` | `0x8AF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1232 | `EVP_CIPHER_meth_set_iv_length` | `0x8AF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1305 | `EVP_MD_meth_set_flags` | `0x8AF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1253 | `EVP_Digest` | `0x8AF80` | 426 | UnwindData |  |
| 1254 | `EVP_DigestFinal` | `0x8B130` | 41 | UnwindData |  |
| 1255 | `EVP_DigestFinal_ex` | `0x8B160` | 174 | UnwindData |  |
| 1256 | `EVP_DigestInit` | `0x8B210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1257 | `EVP_DigestInit_ex` | `0x8B230` | 317 | UnwindData |  |
| 1261 | `EVP_DigestUpdate` | `0x8B370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1276 | `EVP_MD_CTX_cleanup` | `0x8B380` | 159 | UnwindData |  |
| 1278 | `EVP_MD_CTX_copy` | `0x8B420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1279 | `EVP_MD_CTX_copy_ex` | `0x8B440` | 37 | UnwindData |  |
| 1281 | `EVP_MD_CTX_ctrl` | `0x8B5E0` | 107 | UnwindData |  |
| 1282 | `EVP_MD_CTX_destroy` | `0x8B650` | 32 | UnwindData |  |
| 1283 | `EVP_MD_CTX_free` | `0x8B650` | 32 | UnwindData |  |
| 1284 | `EVP_MD_CTX_init` | `0x8B670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1289 | `EVP_MD_CTX_reset` | `0x8B680` | 8,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1460 | `EVP_aead_aes_128_gcm` | `0x8D780` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1461 | `EVP_aead_aes_256_gcm` | `0x8D790` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1464 | `EVP_aes_128_cbc` | `0x8D7A0` | 37 | UnwindData |  |
| 1466 | `EVP_aes_128_ccm` | `0x8D7D0` | 37 | UnwindData |  |
| 1467 | `EVP_aes_128_cfb1` | `0x8D800` | 37 | UnwindData |  |
| 1468 | `EVP_aes_128_cfb128` | `0x8D830` | 37 | UnwindData |  |
| 1469 | `EVP_aes_128_cfb8` | `0x8D860` | 37 | UnwindData |  |
| 1470 | `EVP_aes_128_ctr` | `0x8D890` | 37 | UnwindData |  |
| 1471 | `EVP_aes_128_ecb` | `0x8D8C0` | 37 | UnwindData |  |
| 1472 | `EVP_aes_128_gcm` | `0x8D8F0` | 37 | UnwindData |  |
| 1473 | `EVP_aes_128_ofb` | `0x8D920` | 37 | UnwindData |  |
| 1474 | `EVP_aes_128_wrap` | `0x8D950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1475 | `EVP_aes_128_xts` | `0x8D960` | 37 | UnwindData |  |
| 1476 | `EVP_aes_192_cbc` | `0x8D990` | 37 | UnwindData |  |
| 1477 | `EVP_aes_192_ccm` | `0x8D9C0` | 37 | UnwindData |  |
| 1478 | `EVP_aes_192_cfb1` | `0x8D9F0` | 37 | UnwindData |  |
| 1479 | `EVP_aes_192_cfb128` | `0x8DA20` | 37 | UnwindData |  |
| 1480 | `EVP_aes_192_cfb8` | `0x8DA50` | 37 | UnwindData |  |
| 1481 | `EVP_aes_192_ctr` | `0x8DA80` | 37 | UnwindData |  |
| 1482 | `EVP_aes_192_ecb` | `0x8DAB0` | 37 | UnwindData |  |
| 1483 | `EVP_aes_192_gcm` | `0x8DAE0` | 37 | UnwindData |  |
| 1484 | `EVP_aes_192_ofb` | `0x8DB10` | 37 | UnwindData |  |
| 1485 | `EVP_aes_192_wrap` | `0x8DB40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1486 | `EVP_aes_256_cbc` | `0x8DB50` | 37 | UnwindData |  |
| 1488 | `EVP_aes_256_ccm` | `0x8DB80` | 37 | UnwindData |  |
| 1489 | `EVP_aes_256_cfb1` | `0x8DBB0` | 37 | UnwindData |  |
| 1490 | `EVP_aes_256_cfb128` | `0x8DBE0` | 37 | UnwindData |  |
| 1491 | `EVP_aes_256_cfb8` | `0x8DC10` | 37 | UnwindData |  |
| 1492 | `EVP_aes_256_ctr` | `0x8DC40` | 37 | UnwindData |  |
| 1493 | `EVP_aes_256_ecb` | `0x8DC70` | 37 | UnwindData |  |
| 1494 | `EVP_aes_256_gcm` | `0x8DCA0` | 37 | UnwindData |  |
| 1495 | `EVP_aes_256_ofb` | `0x8DCD0` | 37 | UnwindData |  |
| 1496 | `EVP_aes_256_wrap` | `0x8DD00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1497 | `EVP_aes_256_xts` | `0x8DD10` | 37 | UnwindData |  |
| 1465 | `EVP_aes_128_cbc_hmac_sha1` | `0x8EC60` | 35 | UnwindData |  |
| 1487 | `EVP_aes_256_cbc_hmac_sha1` | `0x8EC90` | 35 | UnwindData |  |
| 1498 | `EVP_bf_cbc` | `0x8F0C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1499 | `EVP_bf_cfb64` | `0x8F0D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1500 | `EVP_bf_ecb` | `0x8F0E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1501 | `EVP_bf_ofb` | `0x8F0F0` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1502 | `EVP_camellia_128_cbc` | `0x8F5D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1503 | `EVP_camellia_128_cfb1` | `0x8F5E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1504 | `EVP_camellia_128_cfb128` | `0x8F5F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1505 | `EVP_camellia_128_cfb8` | `0x8F600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1506 | `EVP_camellia_128_ecb` | `0x8F610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1507 | `EVP_camellia_128_ofb` | `0x8F620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1508 | `EVP_camellia_192_cbc` | `0x8F630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1509 | `EVP_camellia_192_cfb1` | `0x8F640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1510 | `EVP_camellia_192_cfb128` | `0x8F650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1511 | `EVP_camellia_192_cfb8` | `0x8F660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1512 | `EVP_camellia_192_ecb` | `0x8F670` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1513 | `EVP_camellia_192_ofb` | `0x8F680` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1514 | `EVP_camellia_256_cbc` | `0x8F690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1515 | `EVP_camellia_256_cfb1` | `0x8F6A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1516 | `EVP_camellia_256_cfb128` | `0x8F6B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1517 | `EVP_camellia_256_cfb8` | `0x8F6C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1518 | `EVP_camellia_256_ecb` | `0x8F6D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1519 | `EVP_camellia_256_ofb` | `0x8F6E0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1520 | `EVP_cast5_cbc` | `0x8FA40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1521 | `EVP_cast5_cfb64` | `0x8FA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1522 | `EVP_cast5_ecb` | `0x8FA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1523 | `EVP_cast5_ofb` | `0x8FA70` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1524 | `EVP_chacha20` | `0x8FB00` | 4,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1462 | `EVP_aead_chacha20_poly1305` | `0x90D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1463 | `EVP_aead_xchacha20_poly1305` | `0x90D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1525 | `EVP_chacha20_poly1305` | `0x90DA0` | 1,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1527 | `EVP_des_cbc` | `0x913A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1528 | `EVP_des_cfb1` | `0x913B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1529 | `EVP_des_cfb64` | `0x913C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1530 | `EVP_des_cfb8` | `0x913D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1531 | `EVP_des_ecb` | `0x913E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1544 | `EVP_des_ofb` | `0x913F0` | 2,000 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1532 | `EVP_des_ede` | `0x91BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1542 | `EVP_des_ede_ecb` | `0x91BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1533 | `EVP_des_ede3` | `0x91BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1538 | `EVP_des_ede3_ecb` | `0x91BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1534 | `EVP_des_ede3_cbc` | `0x91BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1535 | `EVP_des_ede3_cfb1` | `0x91BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1536 | `EVP_des_ede3_cfb64` | `0x91C00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1537 | `EVP_des_ede3_cfb8` | `0x91C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1539 | `EVP_des_ede3_ofb` | `0x91C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1540 | `EVP_des_ede_cbc` | `0x91C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1541 | `EVP_des_ede_cfb64` | `0x91C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1543 | `EVP_des_ede_ofb` | `0x91C50` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1550 | `EVP_gost2814789_cfb64` | `0x921A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1551 | `EVP_gost2814789_cnt` | `0x921B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1552 | `EVP_gost2814789_ecb` | `0x921C0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1555 | `EVP_idea_cbc` | `0x925A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1556 | `EVP_idea_cfb64` | `0x925B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1557 | `EVP_idea_ecb` | `0x925C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1558 | `EVP_idea_ofb` | `0x925D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1546 | `EVP_enc_null` | `0x92610` | 1,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1563 | `EVP_rc2_40_cbc` | `0x92C10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1564 | `EVP_rc2_64_cbc` | `0x92C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1565 | `EVP_rc2_cbc` | `0x92C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1566 | `EVP_rc2_cfb64` | `0x92C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1567 | `EVP_rc2_ecb` | `0x92C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1568 | `EVP_rc2_ofb` | `0x92C60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1569 | `EVP_rc4` | `0x92CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1570 | `EVP_rc4_40` | `0x92CE0` | 1,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1571 | `EVP_rc4_hmac_md5` | `0x93240` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1588 | `EVP_sm4_cbc` | `0x93620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1589 | `EVP_sm4_cfb128` | `0x93630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1590 | `EVP_sm4_ctr` | `0x93640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1591 | `EVP_sm4_ecb` | `0x93650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1592 | `EVP_sm4_ofb` | `0x93660` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1545 | `EVP_desx_cbc` | `0x937B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1244 | `EVP_DecodeBlock` | `0x937C0` | 345 | UnwindData |  |
| 1245 | `EVP_DecodeFinal` | `0x93920` | 90 | UnwindData |  |
| 1246 | `EVP_DecodeInit` | `0x93980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1247 | `EVP_DecodeUpdate` | `0x93990` | 107 | UnwindData |  |
| 1266 | `EVP_ENCODE_CTX_new` | `0x93B40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1267 | `EVP_EncodeBlock` | `0x93B50` | 19 | UnwindData |  |
| 1268 | `EVP_EncodeFinal` | `0x93C80` | 102 | UnwindData |  |
| 1269 | `EVP_EncodeInit` | `0x93CF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1270 | `EVP_EncodeUpdate` | `0x93D00` | 54 | UnwindData |  |
| 1176 | `EVP_AEAD_CTX_cleanup` | `0x93E80` | 40 | UnwindData |  |
| 1177 | `EVP_AEAD_CTX_free` | `0x93EB0` | 52 | UnwindData |  |
| 1178 | `EVP_AEAD_CTX_init` | `0x93EF0` | 97 | UnwindData |  |
| 1180 | `EVP_AEAD_CTX_open` | `0x93F60` | 237 | UnwindData |  |
| 1181 | `EVP_AEAD_CTX_seal` | `0x94050` | 293 | UnwindData |  |
| 1182 | `EVP_AEAD_key_length` | `0x94180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1183 | `EVP_AEAD_max_overhead` | `0x94190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1184 | `EVP_AEAD_max_tag_len` | `0x941A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1185 | `EVP_AEAD_nonce_length` | `0x941B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1190 | `EVP_CIPHER_CTX_cleanup` | `0x941C0` | 86 | UnwindData |  |
| 1206 | `EVP_CIPHER_CTX_reset` | `0x941C0` | 86 | UnwindData |  |
| 1192 | `EVP_CIPHER_CTX_copy` | `0x94220` | 347 | UnwindData |  |
| 1193 | `EVP_CIPHER_CTX_ctrl` | `0x94380` | 107 | UnwindData |  |
| 1196 | `EVP_CIPHER_CTX_free` | `0x943F0` | 93 | UnwindData |  |
| 1200 | `EVP_CIPHER_CTX_init` | `0x94450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1203 | `EVP_CIPHER_CTX_new` | `0x94460` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1205 | `EVP_CIPHER_CTX_rand_key` | `0x94470` | 152 | UnwindData |  |
| 1211 | `EVP_CIPHER_CTX_set_key_length` | `0x94510` | 171 | UnwindData |  |
| 1212 | `EVP_CIPHER_CTX_set_padding` | `0x945C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1239 | `EVP_CipherFinal` | `0x945E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1240 | `EVP_CipherFinal_ex` | `0x945E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1241 | `EVP_CipherInit` | `0x945F0` | 154 | UnwindData |  |
| 1242 | `EVP_CipherInit_ex` | `0x94690` | 900 | UnwindData |  |
| 1243 | `EVP_CipherUpdate` | `0x94A20` | 38 | UnwindData |  |
| 1248 | `EVP_DecryptFinal` | `0x94A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1249 | `EVP_DecryptFinal_ex` | `0x94A60` | 472 | UnwindData |  |
| 1250 | `EVP_DecryptInit` | `0x94C40` | 154 | UnwindData |  |
| 1251 | `EVP_DecryptInit_ex` | `0x94CE0` | 32 | UnwindData |  |
| 1252 | `EVP_DecryptUpdate` | `0x94D00` | 465 | UnwindData |  |
| 1271 | `EVP_EncryptFinal` | `0x94EE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1272 | `EVP_EncryptFinal_ex` | `0x94EF0` | 273 | UnwindData |  |
| 1273 | `EVP_EncryptInit` | `0x95010` | 154 | UnwindData |  |
| 1274 | `EVP_EncryptInit_ex` | `0x950B0` | 32 | UnwindData |  |
| 1275 | `EVP_EncryptUpdate` | `0x950D0` | 548 | UnwindData |  |
| 1132 | `ERR_load_EVP_strings` | `0x95300` | 57 | UnwindData |  |
| 1186 | `EVP_BytesToKey` | `0x95340` | 226 | UnwindData |  |
| 1549 | `EVP_get_pw_prompt` | `0x955E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1572 | `EVP_read_pw_string` | `0x95600` | 65 | UnwindData |  |
| 1573 | `EVP_read_pw_string_min` | `0x95720` | 265 | UnwindData |  |
| 1575 | `EVP_set_pw_prompt` | `0x95830` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1187 | `EVP_CIPHER_CTX_block_size` | `0x95860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1188 | `EVP_CIPHER_CTX_buf_noconst` | `0x95870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1191 | `EVP_CIPHER_CTX_clear_flags` | `0x95880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2259 | `RSA_clear_flags` | `0x95880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1195 | `EVP_CIPHER_CTX_flags` | `0x95890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1197 | `EVP_CIPHER_CTX_get_app_data` | `0x958A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2295 | `RSA_meth_get_verify` | `0x958A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1198 | `EVP_CIPHER_CTX_get_cipher_data` | `0x958B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1199 | `EVP_CIPHER_CTX_get_iv` | `0x958C0` | 168 | UnwindData |  |
| 1201 | `EVP_CIPHER_CTX_iv_length` | `0x95970` | 72 | UnwindData |  |
| 1202 | `EVP_CIPHER_CTX_key_length` | `0x959C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1207 | `EVP_CIPHER_CTX_set_app_data` | `0x959D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1208 | `EVP_CIPHER_CTX_set_cipher_data` | `0x959E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1209 | `EVP_CIPHER_CTX_set_flags` | `0x959F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2338 | `RSA_set_flags` | `0x959F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1210 | `EVP_CIPHER_CTX_set_iv` | `0x95A00` | 168 | UnwindData |  |
| 1213 | `EVP_CIPHER_CTX_test_flags` | `0x95AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2343 | `RSA_test_flags` | `0x95AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1214 | `EVP_CIPHER_asn1_to_param` | `0x95AC0` | 43 | UnwindData |  |
| 1219 | `EVP_CIPHER_get_asn1_iv` | `0x95BE0` | 199 | UnwindData |  |
| 1235 | `EVP_CIPHER_param_to_asn1` | `0x95CB0` | 59 | UnwindData |  |
| 1236 | `EVP_CIPHER_set_asn1_iv` | `0x95D90` | 154 | UnwindData |  |
| 1237 | `EVP_CIPHER_type` | `0x95E30` | 643 | UnwindData |  |
| 1238 | `EVP_Cipher` | `0x960C0` | 25 | UnwindData |  |
| 1277 | `EVP_MD_CTX_clear_flags` | `0x960E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1285 | `EVP_MD_CTX_md` | `0x960F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2702 | `X509_ATTRIBUTE_get0_object` | `0x960F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2773 | `X509_EXTENSION_get_object` | `0x960F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2800 | `X509_NAME_ENTRY_get_object` | `0x960F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1290 | `EVP_MD_CTX_set_flags` | `0x96100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1291 | `EVP_MD_CTX_set_pkey_ctx` | `0x96110` | 70 | UnwindData |  |
| 1292 | `EVP_MD_CTX_test_flags` | `0x96160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1293 | `EVP_MD_block_size` | `0x96170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1297 | `EVP_MD_meth_dup` | `0x96180` | 120 | UnwindData |  |
| 1298 | `EVP_MD_meth_free` | `0x96200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1299 | `EVP_MD_meth_new` | `0x96210` | 61 | UnwindData |  |
| 1300 | `EVP_MD_meth_set_app_datasize` | `0x96250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1307 | `EVP_MD_meth_set_input_blocksize` | `0x96260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1308 | `EVP_MD_meth_set_result_size` | `0x96270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1311 | `EVP_MD_size` | `0x96280` | 63 | UnwindData |  |
| 1315 | `EVP_PBE_CipherInit` | `0x962C0` | 177 | UnwindData |  |
| 1316 | `EVP_PBE_alg_add` | `0x96530` | 265 | UnwindData |  |
| 1317 | `EVP_PBE_alg_add_type` | `0x96640` | 114 | UnwindData |  |
| 1318 | `EVP_PBE_cleanup` | `0x96750` | 39 | UnwindData |  |
| 1319 | `EVP_PBE_find` | `0x96780` | 199 | UnwindData |  |
| 1320 | `EVP_PKCS82PKEY` | `0x96880` | 64 | UnwindData |  |
| 1321 | `EVP_PKEY2PKCS8` | `0x969F0` | 207 | UnwindData |  |
| 1553 | `EVP_gost2814789imit` | `0x96B20` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1554 | `EVP_gostr341194` | `0x96B60` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1559 | `EVP_md4` | `0x96BA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1560 | `EVP_md5` | `0x96BD0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1561 | `EVP_md5_sha1` | `0x96CD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1562 | `EVP_md_null` | `0x96CE0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1574 | `EVP_ripemd160` | `0x96D20` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1576 | `EVP_sha1` | `0x96E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1577 | `EVP_sha224` | `0x96E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1578 | `EVP_sha256` | `0x96E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1579 | `EVP_sha384` | `0x96E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1584 | `EVP_sha512` | `0x96E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1585 | `EVP_sha512_224` | `0x96E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1586 | `EVP_sha512_256` | `0x96E80` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1580 | `EVP_sha3_224` | `0x96EF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1581 | `EVP_sha3_256` | `0x96F00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1582 | `EVP_sha3_384` | `0x96F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1583 | `EVP_sha3_512` | `0x96F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1258 | `EVP_DigestSign` | `0x96F30` | 144 | UnwindData |  |
| 1259 | `EVP_DigestSignFinal` | `0x96FC0` | 424 | UnwindData |  |
| 1260 | `EVP_DigestSignInit` | `0x97170` | 32 | UnwindData |  |
| 1262 | `EVP_DigestVerify` | `0x97190` | 92 | UnwindData |  |
| 1263 | `EVP_DigestVerifyFinal` | `0x972E0` | 251 | UnwindData |  |
| 1264 | `EVP_DigestVerifyInit` | `0x973E0` | 32 | UnwindData |  |
| 1593 | `EVP_streebog256` | `0x97660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1594 | `EVP_streebog512` | `0x97670` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1587 | `EVP_sm3` | `0x976B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1595 | `EVP_whirlpool` | `0x976F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1216 | `EVP_CIPHER_do_all` | `0x97700` | 68 | UnwindData |  |
| 1217 | `EVP_CIPHER_do_all_sorted` | `0x97750` | 68 | UnwindData |  |
| 1294 | `EVP_MD_do_all` | `0x977A0` | 68 | UnwindData |  |
| 1295 | `EVP_MD_do_all_sorted` | `0x977F0` | 68 | UnwindData |  |
| 1458 | `EVP_add_cipher` | `0x97840` | 84 | UnwindData |  |
| 1459 | `EVP_add_digest` | `0x978A0` | 168 | UnwindData |  |
| 1526 | `EVP_cleanup` | `0x97950` | 72 | UnwindData |  |
| 1547 | `EVP_get_cipherbyname` | `0x979A0` | 48 | UnwindData |  |
| 1548 | `EVP_get_digestbyname` | `0x979D0` | 48 | UnwindData |  |
| 2097 | `PKCS5_PBE_keyivgen` | `0x97A40` | 108 | UnwindData |  |
| 2098 | `PKCS5_PBKDF2_HMAC` | `0x97E00` | 100 | UnwindData |  |
| 2099 | `PKCS5_PBKDF2_HMAC_SHA1` | `0x981D0` | 109 | UnwindData |  |
| 2105 | `PKCS5_v2_PBE_keyivgen` | `0x98240` | 406 | UnwindData |  |
| 1371 | `EVP_PKEY_decrypt_old` | `0x986F0` | 87 | UnwindData |  |
| 1378 | `EVP_PKEY_encrypt_old` | `0x98750` | 84 | UnwindData |  |
| 1362 | `EVP_PKEY_assign` | `0x987B0` | 204 | UnwindData |  |
| 1363 | `EVP_PKEY_base_id` | `0x98880` | 33 | UnwindData |  |
| 1364 | `EVP_PKEY_bits` | `0x988B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1366 | `EVP_PKEY_cmp` | `0x988E0` | 135 | UnwindData |  |
| 1367 | `EVP_PKEY_cmp_parameters` | `0x98970` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1368 | `EVP_PKEY_copy_parameters` | `0x989A0` | 198 | UnwindData |  |
| 1379 | `EVP_PKEY_free` | `0x98A70` | 124 | UnwindData |  |
| 1381 | `EVP_PKEY_get0_DH` | `0x98AF0` | 61 | UnwindData |  |
| 1382 | `EVP_PKEY_get0_DSA` | `0x98B30` | 61 | UnwindData |  |
| 1383 | `EVP_PKEY_get0_EC_KEY` | `0x98B70` | 64 | UnwindData |  |
| 1384 | `EVP_PKEY_get0_RSA` | `0x98BB0` | 70 | UnwindData |  |
| 1386 | `EVP_PKEY_get0_hmac` | `0x98C00` | 74 | UnwindData |  |
| 1387 | `EVP_PKEY_get1_DH` | `0x98C50` | 89 | UnwindData |  |
| 1388 | `EVP_PKEY_get1_DSA` | `0x98CB0` | 89 | UnwindData |  |
| 1389 | `EVP_PKEY_get1_EC_KEY` | `0x98D10` | 92 | UnwindData |  |
| 1390 | `EVP_PKEY_get1_RSA` | `0x98D70` | 98 | UnwindData |  |
| 1395 | `EVP_PKEY_get_default_digest_nid` | `0x98DE0` | 57 | UnwindData |  |
| 1396 | `EVP_PKEY_get_raw_private_key` | `0x98E20` | 126 | UnwindData |  |
| 1397 | `EVP_PKEY_get_raw_public_key` | `0x98EA0` | 126 | UnwindData |  |
| 1424 | `EVP_PKEY_missing_parameters` | `0x98F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1425 | `EVP_PKEY_new` | `0x98F40` | 102 | UnwindData |  |
| 1426 | `EVP_PKEY_new_CMAC_key` | `0x98FB0` | 452 | UnwindData |  |
| 1428 | `EVP_PKEY_new_raw_private_key` | `0x99180` | 409 | UnwindData |  |
| 1429 | `EVP_PKEY_new_raw_public_key` | `0x99320` | 409 | UnwindData |  |
| 1433 | `EVP_PKEY_print_params` | `0x994C0` | 134 | UnwindData |  |
| 1434 | `EVP_PKEY_print_private` | `0x99550` | 131 | UnwindData |  |
| 1435 | `EVP_PKEY_print_public` | `0x995E0` | 131 | UnwindData |  |
| 1437 | `EVP_PKEY_save_parameters` | `0x99670` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1438 | `EVP_PKEY_security_bits` | `0x99690` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1439 | `EVP_PKEY_set1_DH` | `0x996C0` | 230 | UnwindData |  |
| 1440 | `EVP_PKEY_set1_DSA` | `0x997B0` | 230 | UnwindData |  |
| 1441 | `EVP_PKEY_set1_EC_KEY` | `0x998A0` | 233 | UnwindData |  |
| 1442 | `EVP_PKEY_set1_RSA` | `0x99990` | 230 | UnwindData |  |
| 1443 | `EVP_PKEY_set_type` | `0x99A80` | 193 | UnwindData |  |
| 1444 | `EVP_PKEY_set_type_str` | `0x99B50` | 235 | UnwindData |  |
| 1447 | `EVP_PKEY_size` | `0x99C40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1448 | `EVP_PKEY_type` | `0x99C70` | 33 | UnwindData |  |
| 1449 | `EVP_PKEY_up_ref` | `0x99CA0` | 49 | UnwindData |  |
| 1313 | `EVP_OpenFinal` | `0x99CE0` | 49 | UnwindData |  |
| 1314 | `EVP_OpenInit` | `0x99D20` | 343 | UnwindData |  |
| 1454 | `EVP_SealFinal` | `0x99E80` | 49 | UnwindData |  |
| 1455 | `EVP_SealInit` | `0x99EC0` | 335 | UnwindData |  |
| 1456 | `EVP_SignFinal` | `0x9A010` | 303 | UnwindData |  |
| 1457 | `EVP_VerifyFinal` | `0x9A140` | 270 | UnwindData |  |
| 1369 | `EVP_PKEY_decrypt` | `0x9A250` | 302 | UnwindData |  |
| 1370 | `EVP_PKEY_decrypt_init` | `0x9A380` | 132 | UnwindData |  |
| 1373 | `EVP_PKEY_derive` | `0x9A410` | 329 | UnwindData |  |
| 1374 | `EVP_PKEY_derive_init` | `0x9A560` | 132 | UnwindData |  |
| 1375 | `EVP_PKEY_derive_set_peer` | `0x9A5F0` | 590 | UnwindData |  |
| 1376 | `EVP_PKEY_encrypt` | `0x9A840` | 302 | UnwindData |  |
| 1377 | `EVP_PKEY_encrypt_init` | `0x9A970` | 132 | UnwindData |  |
| 1445 | `EVP_PKEY_sign` | `0x9AA00` | 293 | UnwindData |  |
| 1446 | `EVP_PKEY_sign_init` | `0x9AB30` | 126 | UnwindData |  |
| 1450 | `EVP_PKEY_verify` | `0x9ABB0` | 154 | UnwindData |  |
| 1451 | `EVP_PKEY_verify_init` | `0x9AC50` | 126 | UnwindData |  |
| 1452 | `EVP_PKEY_verify_recover` | `0x9ACD0` | 293 | UnwindData |  |
| 1453 | `EVP_PKEY_verify_recover_init` | `0x9AE00` | 126 | UnwindData |  |
| 1331 | `EVP_PKEY_CTX_get_keygen_info` | `0x9AE80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1365 | `EVP_PKEY_check` | `0x9AEB0` | 152 | UnwindData |  |
| 1399 | `EVP_PKEY_keygen` | `0x9AF50` | 232 | UnwindData |  |
| 1400 | `EVP_PKEY_keygen_init` | `0x9B040` | 126 | UnwindData |  |
| 1427 | `EVP_PKEY_new_mac_key` | `0x9B0C0` | 315 | UnwindData |  |
| 1430 | `EVP_PKEY_param_check` | `0x9B200` | 152 | UnwindData |  |
| 1431 | `EVP_PKEY_paramgen` | `0x9B2A0` | 232 | UnwindData |  |
| 1432 | `EVP_PKEY_paramgen_init` | `0x9B390` | 126 | UnwindData |  |
| 1436 | `EVP_PKEY_public_check` | `0x9B410` | 152 | UnwindData |  |
| 1322 | `EVP_PKEY_CTX_ctrl` | `0x9B4E0` | 179 | UnwindData |  |
| 1323 | `EVP_PKEY_CTX_ctrl_str` | `0x9B610` | 479 | UnwindData |  |
| 1324 | `EVP_PKEY_CTX_dup` | `0x9B7F0` | 261 | UnwindData |  |
| 1325 | `EVP_PKEY_CTX_free` | `0x9B900` | 68 | UnwindData |  |
| 1333 | `EVP_PKEY_CTX_new` | `0x9BB70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1334 | `EVP_PKEY_CTX_new_id` | `0x9BB80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1335 | `EVP_PKEY_CTX_set0_keygen_info` | `0x9BB90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1336 | `EVP_PKEY_CTX_set_app_data` | `0x9BBA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2989 | `X509_STORE_set_check_issued` | `0x9BBA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1338 | `EVP_PKEY_CTX_set_data` | `0x9BBB0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2955 | `X509_STORE_CTX_set0_crls` | `0x9BBB0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1401 | `EVP_PKEY_meth_add0` | `0x9BC30` | 72 | UnwindData |  |
| 1402 | `EVP_PKEY_meth_copy` | `0x9BC80` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1403 | `EVP_PKEY_meth_find` | `0x9BD20` | 141 | UnwindData |  |
| 1404 | `EVP_PKEY_meth_free` | `0x9BDB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1405 | `EVP_PKEY_meth_get0_info` | `0x9BDC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1406 | `EVP_PKEY_meth_new` | `0x9BDE0` | 64 | UnwindData |  |
| 1410 | `EVP_PKEY_meth_set_ctrl` | `0x9BE20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1411 | `EVP_PKEY_meth_set_decrypt` | `0x9BE30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1412 | `EVP_PKEY_meth_set_derive` | `0x9BE40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1413 | `EVP_PKEY_meth_set_encrypt` | `0x9BE50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1415 | `EVP_PKEY_meth_set_keygen` | `0x9BE60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1416 | `EVP_PKEY_meth_set_param_check` | `0x9BE70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1417 | `EVP_PKEY_meth_set_paramgen` | `0x9BE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1419 | `EVP_PKEY_meth_set_sign` | `0x9BE90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1420 | `EVP_PKEY_meth_set_signctx` | `0x9BEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2499 | `TS_RESP_CTX_set_extension_cb` | `0x9BEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1421 | `EVP_PKEY_meth_set_verify` | `0x9BEB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2500 | `TS_RESP_CTX_set_serial_cb` | `0x9BEB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1422 | `EVP_PKEY_meth_set_verify_recover` | `0x9BEC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2505 | `TS_RESP_CTX_set_time_cb` | `0x9BEC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1423 | `EVP_PKEY_meth_set_verifyctx` | `0x9BED0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1617 | `GOST2814789IMIT` | `0x9C070` | 714 | UnwindData |  |
| 1618 | `GOST2814789IMIT_Final` | `0x9C340` | 164 | UnwindData |  |
| 1619 | `GOST2814789IMIT_Init` | `0x9C3F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1620 | `GOST2814789IMIT_Transform` | `0x9C410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1621 | `GOST2814789IMIT_Update` | `0x9C420` | 291 | UnwindData |  |
| 1643 | `Gost2814789_cfb64_encrypt` | `0x9C600` | 1,037 | UnwindData |  |
| 1644 | `Gost2814789_cnt_encrypt` | `0x9CA10` | 718 | UnwindData |  |
| 1645 | `Gost2814789_ecb_encrypt` | `0x9D6D0` | 119 | UnwindData |  |
| 1646 | `Gost2814789_set_key` | `0x9EA40` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1647 | `Gost2814789_set_sbox` | `0x9EC00` | 283 | UnwindData |  |
| 1627 | `GOST_CIPHER_PARAMS_free` | `0x9F240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1629 | `GOST_CIPHER_PARAMS_new` | `0x9F250` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3296 | `d2i_GOST_CIPHER_PARAMS` | `0x9F2A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3499 | `i2d_GOST_CIPHER_PARAMS` | `0x9F2D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1133 | `ERR_load_GOST_strings` | `0x9F300` | 57 | UnwindData |  |
| 1630 | `GOST_KEY_check_key` | `0xA1450` | 651 | UnwindData |  |
| 1631 | `GOST_KEY_free` | `0xA16E0` | 96 | UnwindData |  |
| 1635 | `GOST_KEY_get_digest` | `0xA1740` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1636 | `GOST_KEY_get_size` | `0xA1750` | 117 | UnwindData |  |
| 1637 | `GOST_KEY_new` | `0xA17D0` | 88 | UnwindData |  |
| 1638 | `GOST_KEY_set_digest` | `0xA1830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1639 | `GOST_KEY_set_group` | `0xA1850` | 56 | UnwindData |  |
| 1640 | `GOST_KEY_set_private_key` | `0xA1890` | 58 | UnwindData |  |
| 1641 | `GOST_KEY_set_public_key` | `0xA18D0` | 61 | UnwindData |  |
| 1642 | `GOST_KEY_set_public_key_affine_coordinates` | `0xA1910` | 62 | UnwindData |  |
| 1622 | `GOSTR341194` | `0xA2EA0` | 396 | UnwindData |  |
| 1623 | `GOSTR341194_Final` | `0xA3030` | 701 | UnwindData |  |
| 1624 | `GOSTR341194_Init` | `0xA32F0` | 49 | UnwindData |  |
| 1625 | `GOSTR341194_Transform` | `0xA3330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1626 | `GOSTR341194_Update` | `0xA3340` | 293 | UnwindData |  |
| 2415 | `STREEBOG256` | `0xA43F0` | 183 | UnwindData |  |
| 2416 | `STREEBOG256_Final` | `0xA44B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2417 | `STREEBOG256_Init` | `0xA44C0` | 64 | UnwindData |  |
| 2418 | `STREEBOG256_Update` | `0xA4500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2419 | `STREEBOG512` | `0xA4510` | 128 | UnwindData |  |
| 2420 | `STREEBOG512_Final` | `0xA4640` | 15 | UnwindData |  |
| 2421 | `STREEBOG512_Init` | `0xA4DC0` | 40 | UnwindData |  |
| 2422 | `STREEBOG512_Transform` | `0xA4DF0` | 83 | UnwindData |  |
| 2423 | `STREEBOG512_Update` | `0xA4E50` | 69 | UnwindData |  |
| 1648 | `HKDF` | `0xA5B60` | 231 | UnwindData |  |
| 1649 | `HKDF_expand` | `0xA5C50` | 115 | UnwindData |  |
| 1650 | `HKDF_extract` | `0xA5EA0` | 129 | UnwindData |  |
| 1651 | `HMAC` | `0xA64F0` | 433 | UnwindData |  |
| 1652 | `HMAC_CTX_copy` | `0xA66F0` | 252 | UnwindData |  |
| 1653 | `HMAC_CTX_free` | `0xA67F0` | 67 | UnwindData |  |
| 1655 | `HMAC_CTX_new` | `0xA6880` | 78 | UnwindData |  |
| 1656 | `HMAC_CTX_reset` | `0xA68D0` | 125 | UnwindData |  |
| 1657 | `HMAC_CTX_set_flags` | `0xA6950` | 56 | UnwindData |  |
| 1658 | `HMAC_Final` | `0xA6990` | 168 | UnwindData |  |
| 1659 | `HMAC_Init` | `0xA6A40` | 123 | UnwindData |  |
| 1660 | `HMAC_Init_ex` | `0xA6AC0` | 652 | UnwindData |  |
| 1661 | `HMAC_Update` | `0xA6D50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3635 | `idea_cbc_encrypt` | `0xA6D70` | 629 | UnwindData |  |
| 3638 | `idea_encrypt` | `0xA7270` | 2,143 | UnwindData |  |
| 3636 | `idea_cfb64_encrypt` | `0xA7AD0` | 58 | UnwindData |  |
| 3637 | `idea_ecb_encrypt` | `0xA7CE0` | 166 | UnwindData |  |
| 3639 | `idea_ofb64_encrypt` | `0xA7D90` | 455 | UnwindData |  |
| 3640 | `idea_set_decrypt_key` | `0xA7F60` | 331 | UnwindData |  |
| 3641 | `idea_set_encrypt_key` | `0xA80B0` | 395 | UnwindData |  |
| 3648 | `lh_node_stats` | `0xA88A0` | 157 | UnwindData |  |
| 3649 | `lh_node_stats_bio` | `0xA8940` | 101 | UnwindData |  |
| 3650 | `lh_node_usage_stats` | `0xA89B0` | 50 | UnwindData |  |
| 3651 | `lh_node_usage_stats_bio` | `0xA8AE0` | 236 | UnwindData |  |
| 3654 | `lh_stats` | `0xA8BD0` | 393 | UnwindData |  |
| 3655 | `lh_stats_bio` | `0xA8D60` | 330 | UnwindData |  |
| 3642 | `lh_delete` | `0xA8F60` | 55 | UnwindData |  |
| 3643 | `lh_doall` | `0xA90A0` | 25 | UnwindData |  |
| 3644 | `lh_doall_arg` | `0xA9120` | 30 | UnwindData |  |
| 3645 | `lh_free` | `0xA91A0` | 10 | UnwindData |  |
| 3646 | `lh_insert` | `0xA9210` | 169 | UnwindData |  |
| 3647 | `lh_new` | `0xA9390` | 183 | UnwindData |  |
| 3652 | `lh_num_items` | `0xA9450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3653 | `lh_retrieve` | `0xA9460` | 55 | UnwindData |  |
| 3656 | `lh_strhash` | `0xA94A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1678 | `MD4` | `0xA9500` | 131 | UnwindData |  |
| 1679 | `MD4_Final` | `0xA9620` | 341 | UnwindData |  |
| 1680 | `MD4_Init` | `0xA9780` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1685 | `MD5_Init` | `0xA9780` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1681 | `MD4_Transform` | `0xA97C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1682 | `MD4_Update` | `0xA97D0` | 305 | UnwindData |  |
| 1683 | `MD5` | `0xAA150` | 445 | UnwindData |  |
| 1684 | `MD5_Final` | `0xAA310` | 214 | UnwindData |  |
| 1686 | `MD5_Transform` | `0xAA3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1687 | `MD5_Update` | `0xAA400` | 305 | UnwindData |  |
| 664 | `CRYPTO_cbc128_decrypt` | `0xAA540` | 734 | UnwindData |  |
| 665 | `CRYPTO_cbc128_encrypt` | `0xAA9F0` | 677 | UnwindData |  |
| 666 | `CRYPTO_ccm128_aad` | `0xAACA0` | 53 | UnwindData |  |
| 667 | `CRYPTO_ccm128_decrypt` | `0xAAE40` | 541 | UnwindData |  |
| 668 | `CRYPTO_ccm128_decrypt_ccm64` | `0xAB060` | 570 | UnwindData |  |
| 669 | `CRYPTO_ccm128_encrypt` | `0xAB2A0` | 248 | UnwindData |  |
| 670 | `CRYPTO_ccm128_encrypt_ccm64` | `0xAB610` | 939 | UnwindData |  |
| 671 | `CRYPTO_ccm128_init` | `0xAB9C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 672 | `CRYPTO_ccm128_setiv` | `0xABA00` | 157 | UnwindData |  |
| 673 | `CRYPTO_ccm128_tag` | `0xABAA0` | 62 | UnwindData |  |
| 674 | `CRYPTO_cfb128_1_encrypt` | `0xABAE0` | 26 | UnwindData |  |
| 675 | `CRYPTO_cfb128_8_encrypt` | `0xABBE0` | 21 | UnwindData |  |
| 676 | `CRYPTO_cfb128_encrypt` | `0xABC80` | 860 | UnwindData |  |
| 679 | `CRYPTO_ctr128_encrypt` | `0xAC420` | 544 | UnwindData |  |
| 680 | `CRYPTO_ctr128_encrypt_ctr32` | `0xAC640` | 537 | UnwindData |  |
| 691 | `CRYPTO_gcm128_aad` | `0xAC860` | 92 | UnwindData |  |
| 692 | `CRYPTO_gcm128_decrypt` | `0xAC9B0` | 112 | UnwindData |  |
| 693 | `CRYPTO_gcm128_decrypt_ctr32` | `0xACD30` | 106 | UnwindData |  |
| 694 | `CRYPTO_gcm128_encrypt` | `0xACFF0` | 107 | UnwindData |  |
| 695 | `CRYPTO_gcm128_encrypt_ctr32` | `0xAD360` | 106 | UnwindData |  |
| 696 | `CRYPTO_gcm128_finish` | `0xAD610` | 20 | UnwindData |  |
| 697 | `CRYPTO_gcm128_init` | `0xAD760` | 260 | UnwindData |  |
| 698 | `CRYPTO_gcm128_new` | `0xADA70` | 72 | UnwindData |  |
| 699 | `CRYPTO_gcm128_release` | `0xADAC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 700 | `CRYPTO_gcm128_setiv` | `0xADAD0` | 98 | UnwindData |  |
| 701 | `CRYPTO_gcm128_tag` | `0xADD90` | 40 | UnwindData |  |
| 732 | `CRYPTO_ofb128_encrypt` | `0xADEC0` | 210 | UnwindData |  |
| 758 | `CRYPTO_xts128_encrypt` | `0xAE090` | 76 | UnwindData |  |
| 1721 | `OBJ_NAME_add` | `0xAE330` | 258 | UnwindData |  |
| 1722 | `OBJ_NAME_cleanup` | `0xAE440` | 20 | UnwindData |  |
| 1723 | `OBJ_NAME_do_all` | `0xAE4D0` | 47 | UnwindData |  |
| 1724 | `OBJ_NAME_do_all_sorted` | `0xAE500` | 240 | UnwindData |  |
| 1725 | `OBJ_NAME_get` | `0xAE5F0` | 195 | UnwindData |  |
| 1726 | `OBJ_NAME_init` | `0xAE6C0` | 65 | UnwindData |  |
| 1727 | `OBJ_NAME_new_index` | `0xAE710` | 61 | UnwindData |  |
| 1728 | `OBJ_NAME_remove` | `0xAE860` | 64 | UnwindData |  |
| 1729 | `OBJ_add_object` | `0xAEB00` | 511 | UnwindData |  |
| 1730 | `OBJ_bsearch_` | `0xAED00` | 31 | UnwindData |  |
| 1731 | `OBJ_cleanup` | `0xAEEB0` | 125 | UnwindData |  |
| 1733 | `OBJ_create` | `0xAEF30` | 70 | UnwindData |  |
| 1734 | `OBJ_create_objects` | `0xAF040` | 588 | UnwindData |  |
| 1738 | `OBJ_get0_data` | `0xAF290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2613 | `UI_method_get_flusher` | `0xAF290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1739 | `OBJ_length` | `0xAF2A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1740 | `OBJ_ln2nid` | `0xAF2C0` | 77 | UnwindData |  |
| 1741 | `OBJ_new_nid` | `0xAF3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1742 | `OBJ_nid2ln` | `0xAF3E0` | 175 | UnwindData |  |
| 1743 | `OBJ_nid2obj` | `0xAF490` | 170 | UnwindData |  |
| 1744 | `OBJ_nid2sn` | `0xAF540` | 173 | UnwindData |  |
| 1745 | `OBJ_obj2nid` | `0xAF5F0` | 107 | UnwindData |  |
| 1746 | `OBJ_obj2txt` | `0xAF700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1747 | `OBJ_sn2nid` | `0xAF720` | 77 | UnwindData |  |
| 1748 | `OBJ_txt2nid` | `0xAF830` | 103 | UnwindData |  |
| 1749 | `OBJ_txt2obj` | `0xAF940` | 678 | UnwindData |  |
| 1134 | `ERR_load_OBJ_strings` | `0xAFF30` | 57 | UnwindData |  |
| 1732 | `OBJ_cmp` | `0xAFF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1735 | `OBJ_dup` | `0xAFF90` | 135 | UnwindData |  |
| 1736 | `OBJ_find_sigid_algs` | `0xB0100` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1737 | `OBJ_find_sigid_by_algs` | `0xB0150` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1753 | `OCSP_BASICRESP_free` | `0xB01A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1761 | `OCSP_BASICRESP_new` | `0xB01B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1763 | `OCSP_CERTID_free` | `0xB01C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1765 | `OCSP_CERTID_new` | `0xB01D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1766 | `OCSP_CERTSTATUS_free` | `0xB01E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1768 | `OCSP_CERTSTATUS_new` | `0xB01F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1769 | `OCSP_CRLID_free` | `0xB0200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1771 | `OCSP_CRLID_new` | `0xB0210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1775 | `OCSP_ONEREQ_free` | `0xB0220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1783 | `OCSP_ONEREQ_new` | `0xB0230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1784 | `OCSP_REQINFO_free` | `0xB0240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1786 | `OCSP_REQINFO_new` | `0xB0250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1790 | `OCSP_REQUEST_free` | `0xB0260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1798 | `OCSP_REQUEST_new` | `0xB0270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1803 | `OCSP_RESPBYTES_free` | `0xB0280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1805 | `OCSP_RESPBYTES_new` | `0xB0290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1806 | `OCSP_RESPDATA_free` | `0xB02A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1808 | `OCSP_RESPDATA_new` | `0xB02B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1809 | `OCSP_RESPID_free` | `0xB02C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1811 | `OCSP_RESPID_new` | `0xB02D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1812 | `OCSP_RESPONSE_free` | `0xB02E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1814 | `OCSP_RESPONSE_new` | `0xB02F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1816 | `OCSP_REVOKEDINFO_free` | `0xB0300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1818 | `OCSP_REVOKEDINFO_new` | `0xB0310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1819 | `OCSP_SERVICELOC_free` | `0xB0320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1821 | `OCSP_SERVICELOC_new` | `0xB0330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1822 | `OCSP_SIGNATURE_free` | `0xB0340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1824 | `OCSP_SIGNATURE_new` | `0xB0350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1828 | `OCSP_SINGLERESP_free` | `0xB0360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1837 | `OCSP_SINGLERESP_new` | `0xB0370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3305 | `d2i_OCSP_BASICRESP` | `0xB0380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3306 | `d2i_OCSP_CERTID` | `0xB0390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3307 | `d2i_OCSP_CERTSTATUS` | `0xB03A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3308 | `d2i_OCSP_CRLID` | `0xB03B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3309 | `d2i_OCSP_ONEREQ` | `0xB03C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3310 | `d2i_OCSP_REQINFO` | `0xB03D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3311 | `d2i_OCSP_REQUEST` | `0xB03E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3312 | `d2i_OCSP_REQUEST_bio` | `0xB03F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3313 | `d2i_OCSP_RESPBYTES` | `0xB0410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3314 | `d2i_OCSP_RESPDATA` | `0xB0420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3315 | `d2i_OCSP_RESPID` | `0xB0430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3316 | `d2i_OCSP_RESPONSE` | `0xB0440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3317 | `d2i_OCSP_RESPONSE_bio` | `0xB0450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3318 | `d2i_OCSP_REVOKEDINFO` | `0xB0470` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3319 | `d2i_OCSP_SERVICELOC` | `0xB0480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3320 | `d2i_OCSP_SIGNATURE` | `0xB0490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3321 | `d2i_OCSP_SINGLERESP` | `0xB04A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3508 | `i2d_OCSP_BASICRESP` | `0xB04B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3509 | `i2d_OCSP_CERTID` | `0xB04C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3510 | `i2d_OCSP_CERTSTATUS` | `0xB04D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3511 | `i2d_OCSP_CRLID` | `0xB04E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3512 | `i2d_OCSP_ONEREQ` | `0xB04F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3513 | `i2d_OCSP_REQINFO` | `0xB0500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3514 | `i2d_OCSP_REQUEST` | `0xB0510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3515 | `i2d_OCSP_REQUEST_bio` | `0xB0520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3516 | `i2d_OCSP_RESPBYTES` | `0xB0540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3517 | `i2d_OCSP_RESPDATA` | `0xB0550` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3518 | `i2d_OCSP_RESPID` | `0xB0560` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3519 | `i2d_OCSP_RESPONSE` | `0xB0570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3520 | `i2d_OCSP_RESPONSE_bio` | `0xB0580` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3521 | `i2d_OCSP_REVOKEDINFO` | `0xB05A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3522 | `i2d_OCSP_SERVICELOC` | `0xB05B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3523 | `i2d_OCSP_SIGNATURE` | `0xB05C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3524 | `i2d_OCSP_SINGLERESP` | `0xB05D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1849 | `OCSP_check_validity` | `0xB05E0` | 566 | UnwindData |  |
| 1858 | `OCSP_request_add0_id` | `0xB0820` | 114 | UnwindData |  |
| 1859 | `OCSP_request_add1_cert` | `0xB08A0` | 137 | UnwindData |  |
| 1864 | `OCSP_request_set1_name` | `0xB0930` | 127 | UnwindData |  |
| 1865 | `OCSP_request_sign` | `0xB09B0` | 478 | UnwindData |  |
| 1867 | `OCSP_resp_count` | `0xB0B90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1868 | `OCSP_resp_find` | `0xB0BB0` | 142 | UnwindData |  |
| 1869 | `OCSP_resp_find_status` | `0xB0C40` | 284 | UnwindData |  |
| 1870 | `OCSP_resp_get0` | `0xB0D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1872 | `OCSP_resp_get0_id` | `0xB0D80` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1879 | `OCSP_response_get1_basic` | `0xB0DC0` | 139 | UnwindData |  |
| 1880 | `OCSP_response_status` | `0xB0E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1885 | `OCSP_single_get0_status` | `0xB0E60` | 162 | UnwindData |  |
| 1135 | `ERR_load_OCSP_strings` | `0xB0F10` | 57 | UnwindData |  |
| 1750 | `OCSP_BASICRESP_add1_ext_i2d` | `0xB0F50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1751 | `OCSP_BASICRESP_add_ext` | `0xB0F60` | 31 | UnwindData |  |
| 1752 | `OCSP_BASICRESP_delete_ext` | `0xB0F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1754 | `OCSP_BASICRESP_get1_ext_d2i` | `0xB0F90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1755 | `OCSP_BASICRESP_get_ext` | `0xB0FA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1756 | `OCSP_BASICRESP_get_ext_by_NID` | `0xB0FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1757 | `OCSP_BASICRESP_get_ext_by_OBJ` | `0xB0FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1758 | `OCSP_BASICRESP_get_ext_by_critical` | `0xB0FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1759 | `OCSP_BASICRESP_get_ext_count` | `0xB0FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1772 | `OCSP_ONEREQ_add1_ext_i2d` | `0xB0FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1773 | `OCSP_ONEREQ_add_ext` | `0xB1000` | 28 | UnwindData |  |
| 1774 | `OCSP_ONEREQ_delete_ext` | `0xB1020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1776 | `OCSP_ONEREQ_get1_ext_d2i` | `0xB1030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1777 | `OCSP_ONEREQ_get_ext` | `0xB1040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1778 | `OCSP_ONEREQ_get_ext_by_NID` | `0xB1050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1779 | `OCSP_ONEREQ_get_ext_by_OBJ` | `0xB1060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1780 | `OCSP_ONEREQ_get_ext_by_critical` | `0xB1070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1781 | `OCSP_ONEREQ_get_ext_count` | `0xB1080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1787 | `OCSP_REQUEST_add1_ext_i2d` | `0xB1090` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1788 | `OCSP_REQUEST_add_ext` | `0xB10A0` | 31 | UnwindData |  |
| 1789 | `OCSP_REQUEST_delete_ext` | `0xB10C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1791 | `OCSP_REQUEST_get1_ext_d2i` | `0xB10D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1792 | `OCSP_REQUEST_get_ext` | `0xB10E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1793 | `OCSP_REQUEST_get_ext_by_NID` | `0xB10F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1794 | `OCSP_REQUEST_get_ext_by_OBJ` | `0xB1100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1795 | `OCSP_REQUEST_get_ext_by_critical` | `0xB1110` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1796 | `OCSP_REQUEST_get_ext_count` | `0xB1120` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1825 | `OCSP_SINGLERESP_add1_ext_i2d` | `0xB1130` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1826 | `OCSP_SINGLERESP_add_ext` | `0xB1140` | 28 | UnwindData |  |
| 1827 | `OCSP_SINGLERESP_delete_ext` | `0xB1160` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1830 | `OCSP_SINGLERESP_get1_ext_d2i` | `0xB1170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1831 | `OCSP_SINGLERESP_get_ext` | `0xB1180` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1832 | `OCSP_SINGLERESP_get_ext_by_NID` | `0xB1190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1833 | `OCSP_SINGLERESP_get_ext_by_OBJ` | `0xB11A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1834 | `OCSP_SINGLERESP_get_ext_by_critical` | `0xB11B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1835 | `OCSP_SINGLERESP_get_ext_count` | `0xB11C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1838 | `OCSP_accept_responses_new` | `0xB11D0` | 157 | UnwindData |  |
| 1839 | `OCSP_archive_cutoff_new` | `0xB1270` | 109 | UnwindData |  |
| 1841 | `OCSP_basic_add1_nonce` | `0xB12E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1848 | `OCSP_check_nonce` | `0xB12F0` | 177 | UnwindData |  |
| 1850 | `OCSP_copy_nonce` | `0xB13B0` | 118 | UnwindData |  |
| 1851 | `OCSP_crlID_new` | `0xB1430` | 216 | UnwindData |  |
| 1860 | `OCSP_request_add1_nonce` | `0xB1510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1886 | `OCSP_url_svcloc_new` | `0xB1520` | 66 | UnwindData |  |
| 1800 | `OCSP_REQ_CTX_add1_header` | `0xB1750` | 138 | UnwindData |  |
| 1801 | `OCSP_REQ_CTX_free` | `0xB17E0` | 45 | UnwindData |  |
| 1802 | `OCSP_REQ_CTX_set1_req` | `0xB1810` | 126 | UnwindData |  |
| 1882 | `OCSP_sendreq_bio` | `0xB1890` | 395 | UnwindData |  |
| 1883 | `OCSP_sendreq_nbio` | `0xB1A20` | 892 | UnwindData |  |
| 1884 | `OCSP_sendreq_new` | `0xB1DA0` | 52 | UnwindData |  |
| 1762 | `OCSP_CERTID_dup` | `0xB20E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1845 | `OCSP_cert_id_new` | `0xB20F0` | 402 | UnwindData |  |
| 1847 | `OCSP_cert_to_id` | `0xB2290` | 129 | UnwindData |  |
| 1853 | `OCSP_id_cmp` | `0xB2490` | 95 | UnwindData |  |
| 1855 | `OCSP_id_issuer_cmp` | `0xB24F0` | 78 | UnwindData |  |
| 1857 | `OCSP_parse_url` | `0xB2540` | 188 | UnwindData |  |
| 1799 | `OCSP_REQUEST_print` | `0xB2730` | 491 | UnwindData |  |
| 1815 | `OCSP_RESPONSE_print` | `0xB2920` | 269 | UnwindData |  |
| 1846 | `OCSP_cert_status_str` | `0xB2DE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1852 | `OCSP_crl_reason_str` | `0xB2E10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1881 | `OCSP_response_status_str` | `0xB2E40` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1840 | `OCSP_basic_add1_cert` | `0xB2F70` | 91 | UnwindData |  |
| 1842 | `OCSP_basic_add1_status` | `0xB2FD0` | 371 | UnwindData |  |
| 1843 | `OCSP_basic_sign` | `0xB3150` | 485 | UnwindData |  |
| 1854 | `OCSP_id_get0_info` | `0xB3340` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1861 | `OCSP_request_is_signed` | `0xB3390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2081 | `PKCS12_mac_present` | `0xB3390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1862 | `OCSP_request_onereq_count` | `0xB33A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1863 | `OCSP_request_onereq_get0` | `0xB33B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1878 | `OCSP_response_create` | `0xB33C0` | 155 | UnwindData |  |
| 1844 | `OCSP_basic_verify` | `0xB3460` | 748 | UnwindData |  |
| 1866 | `OCSP_request_verify` | `0xB3750` | 106 | UnwindData |  |
| 1876 | `OCSP_resp_get0_signer` | `0xB39D0` | 120 | UnwindData |  |
| 1938 | `PEM_read_DHparams` | `0xB3E50` | 44 | UnwindData |  |
| 1939 | `PEM_read_DSAPrivateKey` | `0xB3E80` | 42 | UnwindData |  |
| 1940 | `PEM_read_DSA_PUBKEY` | `0xB3F00` | 44 | UnwindData |  |
| 1941 | `PEM_read_DSAparams` | `0xB3F30` | 44 | UnwindData |  |
| 1942 | `PEM_read_ECPKParameters` | `0xB3F60` | 44 | UnwindData |  |
| 1943 | `PEM_read_ECPrivateKey` | `0xB3F90` | 42 | UnwindData |  |
| 1944 | `PEM_read_EC_PUBKEY` | `0xB4010` | 44 | UnwindData |  |
| 1945 | `PEM_read_PKCS7` | `0xB4040` | 44 | UnwindData |  |
| 1948 | `PEM_read_PUBKEY` | `0xB4070` | 44 | UnwindData |  |
| 1950 | `PEM_read_RSAPrivateKey` | `0xB40A0` | 42 | UnwindData |  |
| 1951 | `PEM_read_RSAPublicKey` | `0xB4120` | 44 | UnwindData |  |
| 1952 | `PEM_read_RSA_PUBKEY` | `0xB4150` | 44 | UnwindData |  |
| 1955 | `PEM_read_X509_CRL` | `0xB4180` | 44 | UnwindData |  |
| 1956 | `PEM_read_X509_REQ` | `0xB41B0` | 44 | UnwindData |  |
| 1959 | `PEM_read_bio_DHparams` | `0xB41E0` | 44 | UnwindData |  |
| 1960 | `PEM_read_bio_DSAPrivateKey` | `0xB4210` | 42 | UnwindData |  |
| 1961 | `PEM_read_bio_DSA_PUBKEY` | `0xB4290` | 44 | UnwindData |  |
| 1962 | `PEM_read_bio_DSAparams` | `0xB42C0` | 44 | UnwindData |  |
| 1963 | `PEM_read_bio_ECPKParameters` | `0xB42F0` | 44 | UnwindData |  |
| 1964 | `PEM_read_bio_ECPrivateKey` | `0xB4320` | 42 | UnwindData |  |
| 1965 | `PEM_read_bio_EC_PUBKEY` | `0xB43A0` | 44 | UnwindData |  |
| 1966 | `PEM_read_bio_PKCS7` | `0xB43D0` | 44 | UnwindData |  |
| 1969 | `PEM_read_bio_PUBKEY` | `0xB4400` | 44 | UnwindData |  |
| 1972 | `PEM_read_bio_RSAPrivateKey` | `0xB4430` | 42 | UnwindData |  |
| 1973 | `PEM_read_bio_RSAPublicKey` | `0xB44B0` | 44 | UnwindData |  |
| 1974 | `PEM_read_bio_RSA_PUBKEY` | `0xB44E0` | 44 | UnwindData |  |
| 1977 | `PEM_read_bio_X509_CRL` | `0xB4510` | 44 | UnwindData |  |
| 1978 | `PEM_read_bio_X509_REQ` | `0xB4540` | 44 | UnwindData |  |
| 1981 | `PEM_write_DHparams` | `0xB4570` | 60 | UnwindData |  |
| 1982 | `PEM_write_DSAPrivateKey` | `0xB45B0` | 81 | UnwindData |  |
| 1983 | `PEM_write_DSA_PUBKEY` | `0xB4610` | 60 | UnwindData |  |
| 1984 | `PEM_write_DSAparams` | `0xB4650` | 60 | UnwindData |  |
| 1985 | `PEM_write_ECPKParameters` | `0xB4690` | 60 | UnwindData |  |
| 1986 | `PEM_write_ECPrivateKey` | `0xB46D0` | 81 | UnwindData |  |
| 1987 | `PEM_write_EC_PUBKEY` | `0xB4730` | 60 | UnwindData |  |
| 1988 | `PEM_write_PKCS7` | `0xB4770` | 60 | UnwindData |  |
| 1993 | `PEM_write_PUBKEY` | `0xB47B0` | 60 | UnwindData |  |
| 1995 | `PEM_write_RSAPrivateKey` | `0xB47F0` | 81 | UnwindData |  |
| 1996 | `PEM_write_RSAPublicKey` | `0xB4850` | 60 | UnwindData |  |
| 1997 | `PEM_write_RSA_PUBKEY` | `0xB4890` | 60 | UnwindData |  |
| 2000 | `PEM_write_X509_CRL` | `0xB48D0` | 60 | UnwindData |  |
| 2001 | `PEM_write_X509_REQ` | `0xB4910` | 60 | UnwindData |  |
| 2002 | `PEM_write_X509_REQ_NEW` | `0xB4950` | 60 | UnwindData |  |
| 2006 | `PEM_write_bio_DHparams` | `0xB4990` | 60 | UnwindData |  |
| 2007 | `PEM_write_bio_DSAPrivateKey` | `0xB49D0` | 81 | UnwindData |  |
| 2008 | `PEM_write_bio_DSA_PUBKEY` | `0xB4A30` | 60 | UnwindData |  |
| 2009 | `PEM_write_bio_DSAparams` | `0xB4A70` | 60 | UnwindData |  |
| 2010 | `PEM_write_bio_ECPKParameters` | `0xB4AB0` | 60 | UnwindData |  |
| 2011 | `PEM_write_bio_ECPrivateKey` | `0xB4AF0` | 81 | UnwindData |  |
| 2012 | `PEM_write_bio_EC_PUBKEY` | `0xB4B50` | 60 | UnwindData |  |
| 2013 | `PEM_write_bio_PKCS7` | `0xB4B90` | 60 | UnwindData |  |
| 2019 | `PEM_write_bio_PUBKEY` | `0xB4BD0` | 60 | UnwindData |  |
| 2023 | `PEM_write_bio_RSAPrivateKey` | `0xB4C10` | 81 | UnwindData |  |
| 2024 | `PEM_write_bio_RSAPublicKey` | `0xB4C70` | 60 | UnwindData |  |
| 2025 | `PEM_write_bio_RSA_PUBKEY` | `0xB4CB0` | 60 | UnwindData |  |
| 2028 | `PEM_write_bio_X509_CRL` | `0xB4CF0` | 60 | UnwindData |  |
| 2029 | `PEM_write_bio_X509_REQ` | `0xB4D30` | 60 | UnwindData |  |
| 2030 | `PEM_write_bio_X509_REQ_NEW` | `0xB4D70` | 60 | UnwindData |  |
| 1136 | `ERR_load_PEM_strings` | `0xB4DB0` | 57 | UnwindData |  |
| 1927 | `PEM_X509_INFO_read` | `0xB4DF0` | 176 | UnwindData |  |
| 1928 | `PEM_X509_INFO_read_bio` | `0xB4EA0` | 131 | UnwindData |  |
| 1929 | `PEM_X509_INFO_write_bio` | `0xB53C0` | 144 | UnwindData |  |
| 1920 | `PEM_ASN1_read` | `0xB5630` | 196 | UnwindData |  |
| 1922 | `PEM_ASN1_write` | `0xB5700` | 237 | UnwindData |  |
| 1923 | `PEM_ASN1_write_bio` | `0xB57F0` | 1,452 | UnwindData |  |
| 1930 | `PEM_bytes_read_bio` | `0xB5DA0` | 266 | UnwindData |  |
| 1931 | `PEM_def_callback` | `0xB6170` | 277 | UnwindData |  |
| 1932 | `PEM_dek_info` | `0xB6290` | 223 | UnwindData |  |
| 1933 | `PEM_do_header` | `0xB6370` | 84 | UnwindData |  |
| 1934 | `PEM_get_EVP_CIPHER_INFO` | `0xB6670` | 631 | UnwindData |  |
| 1935 | `PEM_proc_type` | `0xB68F0` | 128 | UnwindData |  |
| 1936 | `PEM_read` | `0xB6970` | 184 | UnwindData |  |
| 1957 | `PEM_read_bio` | `0xB6A30` | 147 | UnwindData |  |
| 1979 | `PEM_write` | `0xB7070` | 182 | UnwindData |  |
| 2003 | `PEM_write_bio` | `0xB7130` | 624 | UnwindData |  |
| 1921 | `PEM_ASN1_read_bio` | `0xB76D0` | 190 | UnwindData |  |
| 1946 | `PEM_read_PKCS8` | `0xB7790` | 44 | UnwindData |  |
| 1947 | `PEM_read_PKCS8_PRIV_KEY_INFO` | `0xB77C0` | 44 | UnwindData |  |
| 1967 | `PEM_read_bio_PKCS8` | `0xB77F0` | 44 | UnwindData |  |
| 1968 | `PEM_read_bio_PKCS8_PRIV_KEY_INFO` | `0xB7820` | 44 | UnwindData |  |
| 1989 | `PEM_write_PKCS8` | `0xB7850` | 60 | UnwindData |  |
| 1990 | `PEM_write_PKCS8PrivateKey` | `0xB7890` | 70 | UnwindData |  |
| 1991 | `PEM_write_PKCS8PrivateKey_nid` | `0xB78E0` | 71 | UnwindData |  |
| 1992 | `PEM_write_PKCS8_PRIV_KEY_INFO` | `0xB7930` | 60 | UnwindData |  |
| 2015 | `PEM_write_bio_PKCS8` | `0xB7970` | 60 | UnwindData |  |
| 2016 | `PEM_write_bio_PKCS8PrivateKey` | `0xB79B0` | 70 | UnwindData |  |
| 2017 | `PEM_write_bio_PKCS8PrivateKey_nid` | `0xB7A00` | 71 | UnwindData |  |
| 2018 | `PEM_write_bio_PKCS8_PRIV_KEY_INFO` | `0xB7A50` | 60 | UnwindData |  |
| 3344 | `d2i_PKCS8PrivateKey_bio` | `0xB7A90` | 255 | UnwindData |  |
| 3345 | `d2i_PKCS8PrivateKey_fp` | `0xB7B90` | 100 | UnwindData |  |
| 3550 | `i2d_PKCS8PrivateKey_bio` | `0xB8000` | 73 | UnwindData |  |
| 3551 | `i2d_PKCS8PrivateKey_fp` | `0xB8050` | 73 | UnwindData |  |
| 3552 | `i2d_PKCS8PrivateKey_nid_bio` | `0xB80A0` | 74 | UnwindData |  |
| 3553 | `i2d_PKCS8PrivateKey_nid_fp` | `0xB80F0` | 74 | UnwindData |  |
| 1949 | `PEM_read_PrivateKey` | `0xB8140` | 176 | UnwindData |  |
| 1970 | `PEM_read_bio_Parameters` | `0xB81F0` | 298 | UnwindData |  |
| 1971 | `PEM_read_bio_PrivateKey` | `0xB8320` | 117 | UnwindData |  |
| 1994 | `PEM_write_PrivateKey` | `0xB8590` | 297 | UnwindData |  |
| 2020 | `PEM_write_bio_Parameters` | `0xB86C0` | 166 | UnwindData |  |
| 2021 | `PEM_write_bio_PrivateKey` | `0xB8770` | 221 | UnwindData |  |
| 2022 | `PEM_write_bio_PrivateKey_traditional` | `0xB8850` | 178 | UnwindData |  |
| 1924 | `PEM_SignFinal` | `0xB8910` | 188 | UnwindData |  |
| 1925 | `PEM_SignInit` | `0xB89D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1926 | `PEM_SignUpdate` | `0xB89E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1953 | `PEM_read_X509` | `0xB89F0` | 44 | UnwindData |  |
| 1975 | `PEM_read_bio_X509` | `0xB8A20` | 44 | UnwindData |  |
| 1998 | `PEM_write_X509` | `0xB8A50` | 60 | UnwindData |  |
| 2026 | `PEM_write_bio_X509` | `0xB8A90` | 60 | UnwindData |  |
| 1954 | `PEM_read_X509_AUX` | `0xB8AD0` | 44 | UnwindData |  |
| 1976 | `PEM_read_bio_X509_AUX` | `0xB8B00` | 44 | UnwindData |  |
| 1999 | `PEM_write_X509_AUX` | `0xB8B30` | 60 | UnwindData |  |
| 2027 | `PEM_write_bio_X509_AUX` | `0xB8B70` | 60 | UnwindData |  |
| 3219 | `b2i_PVK_bio` | `0xB8BB0` | 121 | UnwindData |  |
| 3220 | `b2i_PrivateKey` | `0xB8E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3221 | `b2i_PrivateKey_bio` | `0xB8E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3222 | `b2i_PublicKey` | `0xB8E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3223 | `b2i_PublicKey_bio` | `0xB8E60` | 6,416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3425 | `i2b_PVK_bio` | `0xBA770` | 151 | UnwindData |  |
| 3426 | `i2b_PrivateKey_bio` | `0xBA810` | 109 | UnwindData |  |
| 3427 | `i2b_PublicKey_bio` | `0xBA880` | 112 | UnwindData |  |
| 2068 | `PKCS12_decrypt_skey` | `0xBAA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2078 | `PKCS12_item_pack_safebag` | `0xBAA70` | 236 | UnwindData |  |
| 2084 | `PKCS12_pack_authsafes` | `0xBAB60` | 45 | UnwindData |  |
| 2085 | `PKCS12_pack_p7data` | `0xBAB90` | 212 | UnwindData |  |
| 2086 | `PKCS12_pack_p7encdata` | `0xBAC70` | 377 | UnwindData |  |
| 2091 | `PKCS12_unpack_authsafes` | `0xBADF0` | 96 | UnwindData |  |
| 2092 | `PKCS12_unpack_p7data` | `0xBAE50` | 88 | UnwindData |  |
| 2093 | `PKCS12_unpack_p7encdata` | `0xBAEB0` | 119 | UnwindData |  |
| 2032 | `PKCS12_BAGS_free` | `0xBAF30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2034 | `PKCS12_BAGS_new` | `0xBAF40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2035 | `PKCS12_MAC_DATA_free` | `0xBAF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2037 | `PKCS12_MAC_DATA_new` | `0xBAF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2046 | `PKCS12_SAFEBAG_free` | `0xBAF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2058 | `PKCS12_SAFEBAG_new` | `0xBAF80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2069 | `PKCS12_free` | `0xBAF90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2082 | `PKCS12_new` | `0xBAFA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3326 | `d2i_PKCS12` | `0xBAFB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3327 | `d2i_PKCS12_BAGS` | `0xBAFC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3328 | `d2i_PKCS12_MAC_DATA` | `0xBAFD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3329 | `d2i_PKCS12_SAFEBAG` | `0xBAFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3529 | `i2d_PKCS12` | `0xBAFF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3530 | `i2d_PKCS12_BAGS` | `0xBB000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3531 | `i2d_PKCS12_MAC_DATA` | `0xBB010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3532 | `i2d_PKCS12_SAFEBAG` | `0xBB020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2059 | `PKCS12_add_CSPName_asc` | `0xBB030` | 47 | UnwindData |  |
| 2061 | `PKCS12_add_friendlyname_asc` | `0xBB060` | 47 | UnwindData |  |
| 2062 | `PKCS12_add_friendlyname_uni` | `0xBB090` | 47 | UnwindData |  |
| 2064 | `PKCS12_add_localkeyid` | `0xBB0C0` | 47 | UnwindData |  |
| 2072 | `PKCS12_get_attr_gen` | `0xBB0F0` | 126 | UnwindData |  |
| 2073 | `PKCS12_get_friendlyname` | `0xBB170` | 50 | UnwindData |  |
| 2192 | `PKCS8_add_keyusage` | `0xBB1B0` | 42 | UnwindData |  |
| 2039 | `PKCS12_PBE_keyivgen` | `0xBB1E0` | 110 | UnwindData |  |
| 2060 | `PKCS12_add_cert` | `0xBB4A0` | 247 | UnwindData |  |
| 2063 | `PKCS12_add_key` | `0xBB5A0` | 207 | UnwindData |  |
| 2065 | `PKCS12_add_safe` | `0xBB670` | 223 | UnwindData |  |
| 2066 | `PKCS12_add_safes` | `0xBB750` | 86 | UnwindData |  |
| 2067 | `PKCS12_create` | `0xBB7B0` | 1,618 | UnwindData |  |
| 2076 | `PKCS12_item_decrypt_d2i` | `0xBBF10` | 252 | UnwindData |  |
| 2077 | `PKCS12_item_i2d_encrypt` | `0xBC010` | 317 | UnwindData |  |
| 2088 | `PKCS12_pbe_crypt` | `0xBC150` | 458 | UnwindData |  |
| 2074 | `PKCS12_init` | `0xBC320` | 238 | UnwindData |  |
| 2079 | `PKCS12_key_gen_asc` | `0xBC410` | 219 | UnwindData |  |
| 2080 | `PKCS12_key_gen_uni` | `0xBC4F0` | 1,058 | UnwindData |  |
| 2087 | `PKCS12_parse` | `0xBC920` | 817 | UnwindData |  |
| 2070 | `PKCS12_gen_mac` | `0xBCE50` | 128 | UnwindData |  |
| 2071 | `PKCS12_get0_mac` | `0xBD0D0` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2089 | `PKCS12_set_mac` | `0xBD150` | 314 | UnwindData |  |
| 2090 | `PKCS12_setup_mac` | `0xBD290` | 59 | UnwindData |  |
| 2094 | `PKCS12_verify_mac` | `0xBD410` | 207 | UnwindData |  |
| 2083 | `PKCS12_newpass` | `0xBD4E0` | 245 | UnwindData |  |
| 2193 | `PKCS8_decrypt` | `0xBDA50` | 47 | UnwindData |  |
| 2194 | `PKCS8_encrypt` | `0xBDA80` | 270 | UnwindData |  |
| 2041 | `PKCS12_SAFEBAG_create0_p8inf` | `0xBDB90` | 106 | UnwindData |  |
| 2042 | `PKCS12_SAFEBAG_create0_pkcs8` | `0xBDC00` | 106 | UnwindData |  |
| 2043 | `PKCS12_SAFEBAG_create_cert` | `0xBDC70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2044 | `PKCS12_SAFEBAG_create_crl` | `0xBDC90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2045 | `PKCS12_SAFEBAG_create_pkcs8_encrypt` | `0xBDCB0` | 215 | UnwindData |  |
| 2047 | `PKCS12_SAFEBAG_get0_attr` | `0xBDD90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2049 | `PKCS12_SAFEBAG_get0_p8inf` | `0xBDDA0` | 42 | UnwindData |  |
| 2050 | `PKCS12_SAFEBAG_get0_pkcs8` | `0xBDDD0` | 42 | UnwindData |  |
| 2051 | `PKCS12_SAFEBAG_get0_safes` | `0xBDE00` | 42 | UnwindData |  |
| 2053 | `PKCS12_SAFEBAG_get1_cert` | `0xBDE30` | 76 | UnwindData |  |
| 2054 | `PKCS12_SAFEBAG_get1_crl` | `0xBDE80` | 76 | UnwindData |  |
| 2055 | `PKCS12_SAFEBAG_get_bag_nid` | `0xBDED0` | 55 | UnwindData |  |
| 2056 | `PKCS12_SAFEBAG_get_nid` | `0xBDF10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2195 | `PKCS8_get_attr` | `0xBDF20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1889 | `OPENSSL_asc2uni` | `0xBDF30` | 196 | UnwindData |  |
| 1901 | `OPENSSL_uni2asc` | `0xBE000` | 137 | UnwindData |  |
| 3330 | `d2i_PKCS12_bio` | `0xBE090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3331 | `d2i_PKCS12_fp` | `0xBE0B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3533 | `i2d_PKCS12_bio` | `0xBE0D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3534 | `i2d_PKCS12_fp` | `0xBE0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1137 | `ERR_load_PKCS12_strings` | `0xBE110` | 57 | UnwindData |  |
| 2108 | `PKCS7_DIGEST_free` | `0xBE220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2110 | `PKCS7_DIGEST_new` | `0xBE230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2111 | `PKCS7_ENCRYPT_free` | `0xBE240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2113 | `PKCS7_ENCRYPT_new` | `0xBE250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2114 | `PKCS7_ENC_CONTENT_free` | `0xBE260` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2116 | `PKCS7_ENC_CONTENT_new` | `0xBE270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2117 | `PKCS7_ENVELOPE_free` | `0xBE280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2119 | `PKCS7_ENVELOPE_new` | `0xBE290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2120 | `PKCS7_ISSUER_AND_SERIAL_digest` | `0xBE2A0` | 32 | UnwindData |  |
| 2121 | `PKCS7_ISSUER_AND_SERIAL_free` | `0xBE2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2123 | `PKCS7_ISSUER_AND_SERIAL_new` | `0xBE2D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2124 | `PKCS7_RECIP_INFO_free` | `0xBE2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2127 | `PKCS7_RECIP_INFO_new` | `0xBE2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2129 | `PKCS7_SIGNED_free` | `0xBE300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2131 | `PKCS7_SIGNED_new` | `0xBE310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2132 | `PKCS7_SIGNER_INFO_free` | `0xBE320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2135 | `PKCS7_SIGNER_INFO_new` | `0xBE330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2138 | `PKCS7_SIGN_ENVELOPE_free` | `0xBE340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2140 | `PKCS7_SIGN_ENVELOPE_new` | `0xBE350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2162 | `PKCS7_dup` | `0xBE360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2165 | `PKCS7_free` | `0xBE370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2173 | `PKCS7_new` | `0xBE380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2174 | `PKCS7_print_ctx` | `0xBE390` | 26 | UnwindData |  |
| 3332 | `d2i_PKCS7` | `0xBE3B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3333 | `d2i_PKCS7_DIGEST` | `0xBE3C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3334 | `d2i_PKCS7_ENCRYPT` | `0xBE3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3335 | `d2i_PKCS7_ENC_CONTENT` | `0xBE3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3336 | `d2i_PKCS7_ENVELOPE` | `0xBE3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3337 | `d2i_PKCS7_ISSUER_AND_SERIAL` | `0xBE400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3338 | `d2i_PKCS7_RECIP_INFO` | `0xBE410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3339 | `d2i_PKCS7_SIGNED` | `0xBE420` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3340 | `d2i_PKCS7_SIGNER_INFO` | `0xBE430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3341 | `d2i_PKCS7_SIGN_ENVELOPE` | `0xBE440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3342 | `d2i_PKCS7_bio` | `0xBE450` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3343 | `d2i_PKCS7_fp` | `0xBE470` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3535 | `i2d_PKCS7` | `0xBE490` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3536 | `i2d_PKCS7_DIGEST` | `0xBE4A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3537 | `i2d_PKCS7_ENCRYPT` | `0xBE4B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3538 | `i2d_PKCS7_ENC_CONTENT` | `0xBE4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3539 | `i2d_PKCS7_ENVELOPE` | `0xBE4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3540 | `i2d_PKCS7_ISSUER_AND_SERIAL` | `0xBE4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3541 | `i2d_PKCS7_RECIP_INFO` | `0xBE4F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3542 | `i2d_PKCS7_SIGNED` | `0xBE500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3543 | `i2d_PKCS7_SIGNER_INFO` | `0xBE510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3544 | `i2d_PKCS7_SIGN_ENVELOPE` | `0xBE520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3545 | `i2d_PKCS7_bio` | `0xBE530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3547 | `i2d_PKCS7_fp` | `0xBE550` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2141 | `PKCS7_add0_attrib_signing_time` | `0xBE570` | 100 | UnwindData |  |
| 2142 | `PKCS7_add1_attrib_digest` | `0xBE5E0` | 124 | UnwindData |  |
| 2143 | `PKCS7_add_attrib_content_type` | `0xBE660` | 94 | UnwindData |  |
| 2144 | `PKCS7_add_attrib_smimecap` | `0xBE6C0` | 146 | UnwindData |  |
| 2171 | `PKCS7_get_smimecap` | `0xBE760` | 75 | UnwindData |  |
| 2185 | `PKCS7_simple_smimecap` | `0xBE7B0` | 267 | UnwindData |  |
| 2137 | `PKCS7_SIGNER_INFO_sign` | `0xBE8C0` | 449 | UnwindData |  |
| 2145 | `PKCS7_add_attribute` | `0xBEA90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2151 | `PKCS7_add_signed_attribute` | `0xBEAA0` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2156 | `PKCS7_dataDecode` | `0xBEBA0` | 190 | UnwindData |  |
| 2157 | `PKCS7_dataFinal` | `0xBF290` | 142 | UnwindData |  |
| 2158 | `PKCS7_dataInit` | `0xBF8F0` | 185 | UnwindData |  |
| 2159 | `PKCS7_dataVerify` | `0xBFF50` | 460 | UnwindData |  |
| 2161 | `PKCS7_digest_from_attributes` | `0xC0120` | 159 | UnwindData |  |
| 2167 | `PKCS7_get_attribute` | `0xC02A0` | 34 | UnwindData |  |
| 2168 | `PKCS7_get_issuer_and_serial` | `0xC0340` | 110 | UnwindData |  |
| 2169 | `PKCS7_get_signed_attribute` | `0xC0430` | 34 | UnwindData |  |
| 2176 | `PKCS7_set_attributes` | `0xC04D0` | 165 | UnwindData |  |
| 2180 | `PKCS7_set_signed_attributes` | `0xC0580` | 165 | UnwindData |  |
| 2184 | `PKCS7_signatureVerify` | `0xC0630` | 133 | UnwindData |  |
| 2125 | `PKCS7_RECIP_INFO_get0_alg` | `0xC0C90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2128 | `PKCS7_RECIP_INFO_set` | `0xC0CA0` | 111 | UnwindData |  |
| 2133 | `PKCS7_SIGNER_INFO_get0_algs` | `0xC0E00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2136 | `PKCS7_SIGNER_INFO_set` | `0xC0E30` | 333 | UnwindData |  |
| 2146 | `PKCS7_add_certificate` | `0xC0F80` | 244 | UnwindData |  |
| 2147 | `PKCS7_add_crl` | `0xC1080` | 244 | UnwindData |  |
| 2148 | `PKCS7_add_recipient` | `0xC1180` | 453 | UnwindData |  |
| 2149 | `PKCS7_add_recipient_info` | `0xC1350` | 130 | UnwindData |  |
| 2150 | `PKCS7_add_signature` | `0xC13E0` | 686 | UnwindData |  |
| 2152 | `PKCS7_add_signer` | `0xC1690` | 347 | UnwindData |  |
| 2153 | `PKCS7_cert_from_signer_info` | `0xC17F0` | 77 | UnwindData |  |
| 2154 | `PKCS7_content_new` | `0xC1840` | 276 | UnwindData |  |
| 2155 | `PKCS7_ctrl` | `0xC1960` | 278 | UnwindData |  |
| 2170 | `PKCS7_get_signer_info` | `0xC1A80` | 71 | UnwindData |  |
| 2175 | `PKCS7_set0_type_other` | `0xC1AD0` | 47 | UnwindData |  |
| 2177 | `PKCS7_set_cipher` | `0xC1B00` | 183 | UnwindData |  |
| 2178 | `PKCS7_set_content` | `0xC1BC0` | 216 | UnwindData |  |
| 2179 | `PKCS7_set_digest` | `0xC1CA0` | 217 | UnwindData |  |
| 2181 | `PKCS7_set_type` | `0xC1D80` | 464 | UnwindData |  |
| 2186 | `PKCS7_stream` | `0xC1F50` | 187 | UnwindData |  |
| 311 | `BIO_new_PKCS7` | `0xC2010` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2014 | `PEM_write_bio_PKCS7_stream` | `0xC2020` | 38 | UnwindData |  |
| 2409 | `SMIME_read_PKCS7` | `0xC2050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2412 | `SMIME_write_PKCS7` | `0xC2060` | 139 | UnwindData |  |
| 3546 | `i2d_PKCS7_bio_stream` | `0xC20F0` | 26 | UnwindData |  |
| 2160 | `PKCS7_decrypt` | `0xC2110` | 633 | UnwindData |  |
| 2163 | `PKCS7_encrypt` | `0xC2390` | 333 | UnwindData |  |
| 2164 | `PKCS7_final` | `0xC24E0` | 220 | UnwindData |  |
| 2166 | `PKCS7_get0_signers` | `0xC25C0` | 139 | UnwindData |  |
| 2182 | `PKCS7_sign` | `0xC27C0` | 89 | UnwindData |  |
| 2183 | `PKCS7_sign_add_signer` | `0xC2930` | 158 | UnwindData |  |
| 2188 | `PKCS7_verify` | `0xC2CA0` | 328 | UnwindData |  |
| 1138 | `ERR_load_PKCS7_strings` | `0xC3300` | 57 | UnwindData |  |
| 733 | `CRYPTO_poly1305_finish` | `0xC3340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 734 | `CRYPTO_poly1305_init` | `0xC3350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 735 | `CRYPTO_poly1305_update` | `0xC3360` | 2,832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1139 | `ERR_load_RAND_strings` | `0xC3E70` | 57 | UnwindData |  |
| 2218 | `RAND_bytes` | `0xC3EB0` | 29 | UnwindData |  |
| 2224 | `RAND_pseudo_bytes` | `0xC3EB0` | 29 | UnwindData |  |
| 2220 | `RAND_file_name` | `0xC3ED0` | 66 | UnwindData |  |
| 2222 | `RAND_load_file` | `0xC3F20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2228 | `RAND_write_file` | `0xC3F30` | 116 | UnwindData |  |
| 2229 | `RC2_cbc_encrypt` | `0xC40A0` | 614 | UnwindData |  |
| 2231 | `RC2_decrypt` | `0xC4590` | 339 | UnwindData |  |
| 2233 | `RC2_encrypt` | `0xC46F0` | 324 | UnwindData |  |
| 2232 | `RC2_ecb_encrypt` | `0xC4840` | 209 | UnwindData |  |
| 2235 | `RC2_set_key` | `0xC4920` | 650 | UnwindData |  |
| 2230 | `RC2_cfb64_encrypt` | `0xC4BB0` | 58 | UnwindData |  |
| 2234 | `RC2_ofb64_encrypt` | `0xC4DD0` | 439 | UnwindData |  |
| 2238 | `RIPEMD160` | `0xC4F90` | 138 | UnwindData |  |
| 2239 | `RIPEMD160_Final` | `0xC50B0` | 369 | UnwindData |  |
| 2240 | `RIPEMD160_Init` | `0xC5230` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2380 | `SHA1_Init` | `0xC5230` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2241 | `RIPEMD160_Transform` | `0xC5280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2242 | `RIPEMD160_Update` | `0xC5290` | 305 | UnwindData |  |
| 2243 | `RSAPrivateKey_dup` | `0xC8DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2245 | `RSAPublicKey_dup` | `0xC8DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2247 | `RSA_OAEP_PARAMS_free` | `0xC8DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2249 | `RSA_OAEP_PARAMS_new` | `0xC8DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2252 | `RSA_PSS_PARAMS_free` | `0xC8DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2254 | `RSA_PSS_PARAMS_new` | `0xC8E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3361 | `d2i_RSAPrivateKey` | `0xC8E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3364 | `d2i_RSAPublicKey` | `0xC8E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3367 | `d2i_RSA_OAEP_PARAMS` | `0xC8E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3368 | `d2i_RSA_PSS_PARAMS` | `0xC8E40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3569 | `i2d_RSAPrivateKey` | `0xC8E50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3572 | `i2d_RSAPublicKey` | `0xC8E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3575 | `i2d_RSA_OAEP_PARAMS` | `0xC8E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3576 | `i2d_RSA_PSS_PARAMS` | `0xC8E80` | 448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2256 | `RSA_blinding_off` | `0xC9040` | 97 | UnwindData |  |
| 2257 | `RSA_blinding_on` | `0xC90B0` | 155 | UnwindData |  |
| 2258 | `RSA_check_key` | `0xC9440` | 70 | UnwindData |  |
| 2250 | `RSA_PKCS1_OpenSSL` | `0xCABE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2251 | `RSA_PKCS1_SSLeay` | `0xCABE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2255 | `RSA_bits` | `0xCABF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2260 | `RSA_flags` | `0xCAC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2328 | `RSA_private_decrypt` | `0xCAC10` | 33 | UnwindData |  |
| 2329 | `RSA_private_encrypt` | `0xCAC40` | 33 | UnwindData |  |
| 2330 | `RSA_public_decrypt` | `0xCAC70` | 33 | UnwindData |  |
| 2331 | `RSA_public_encrypt` | `0xCACA0` | 33 | UnwindData |  |
| 2342 | `RSA_size` | `0xCACD0` | 30 | UnwindData |  |
| 1140 | `ERR_load_RSA_strings` | `0xCAE30` | 57 | UnwindData |  |
| 2262 | `RSA_generate_key` | `0xCAE70` | 217 | UnwindData |  |
| 2263 | `RSA_generate_key_ex` | `0xCAF50` | 37 | UnwindData |  |
| 2261 | `RSA_free` | `0xCB480` | 217 | UnwindData |  |
| 2264 | `RSA_get0_crt_params` | `0xCB560` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2269 | `RSA_get0_factors` | `0xCB590` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2271 | `RSA_get0_key` | `0xCB5B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2276 | `RSA_get_default_method` | `0xCB5E0` | 33 | UnwindData |  |
| 2278 | `RSA_get_ex_new_index` | `0xCB610` | 42 | UnwindData |  |
| 2311 | `RSA_new` | `0xCB640` | 80 | UnwindData |  |
| 2312 | `RSA_new_method` | `0xCB640` | 80 | UnwindData |  |
| 2325 | `RSA_pkey_ctx_ctrl` | `0xCB720` | 81 | UnwindData |  |
| 2332 | `RSA_security_bits` | `0xCB780` | 25 | UnwindData |  |
| 2333 | `RSA_set0_crt_params` | `0xCB7A0` | 150 | UnwindData |  |
| 2334 | `RSA_set0_factors` | `0xCB840` | 121 | UnwindData |  |
| 2335 | `RSA_set0_key` | `0xCB8C0` | 138 | UnwindData |  |
| 2336 | `RSA_set_default_method` | `0xCB950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2339 | `RSA_set_method` | `0xCB960` | 73 | UnwindData |  |
| 2344 | `RSA_up_ref` | `0xCB9B0` | 49 | UnwindData |  |
| 2280 | `RSA_meth_dup` | `0xCB9F0` | 141 | UnwindData |  |
| 2296 | `RSA_meth_new` | `0xCBA80` | 107 | UnwindData |  |
| 2297 | `RSA_meth_set0_app_data` | `0xCBAF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2298 | `RSA_meth_set1_name` | `0xCBB00` | 67 | UnwindData |  |
| 2301 | `RSA_meth_set_flags` | `0xCBB50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2303 | `RSA_meth_set_keygen` | `0xCBB60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2309 | `RSA_meth_set_sign` | `0xCBB70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2310 | `RSA_meth_set_verify` | `0xCBB80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2319 | `RSA_padding_add_none` | `0xCBB90` | 121 | UnwindData |  |
| 2324 | `RSA_padding_check_none` | `0xCBC10` | 139 | UnwindData |  |
| 2095 | `PKCS1_MGF1` | `0xCBCA0` | 366 | UnwindData |  |
| 2313 | `RSA_padding_add_PKCS1_OAEP` | `0xCBE10` | 44 | UnwindData |  |
| 2314 | `RSA_padding_add_PKCS1_OAEP_mgf1` | `0xCBE40` | 1,294 | UnwindData |  |
| 2320 | `RSA_padding_check_PKCS1_OAEP` | `0xCC350` | 61 | UnwindData |  |
| 2321 | `RSA_padding_check_PKCS1_OAEP_mgf1` | `0xCC390` | 1,792 | UnwindData |  |
| 2317 | `RSA_padding_add_PKCS1_type_1` | `0xCCA90` | 164 | UnwindData |  |
| 2318 | `RSA_padding_add_PKCS1_type_2` | `0xCCB40` | 199 | UnwindData |  |
| 2322 | `RSA_padding_check_PKCS1_type_1` | `0xCCC10` | 35 | UnwindData |  |
| 2323 | `RSA_padding_check_PKCS1_type_2` | `0xCCD50` | 35 | UnwindData |  |
| 2326 | `RSA_print` | `0xCE4C0` | 121 | UnwindData |  |
| 2327 | `RSA_print_fp` | `0xCE540` | 94 | UnwindData |  |
| 2315 | `RSA_padding_add_PKCS1_PSS` | `0xCE620` | 31 | UnwindData |  |
| 2316 | `RSA_padding_add_PKCS1_PSS_mgf1` | `0xCE640` | 111 | UnwindData |  |
| 2347 | `RSA_verify_PKCS1_PSS` | `0xCE9E0` | 30 | UnwindData |  |
| 2348 | `RSA_verify_PKCS1_PSS_mgf1` | `0xCEA00` | 132 | UnwindData |  |
| 2341 | `RSA_sign_ASN1_OCTET_STRING` | `0xCEEF0` | 296 | UnwindData |  |
| 2346 | `RSA_verify_ASN1_OCTET_STRING` | `0xCF020` | 341 | UnwindData |  |
| 2340 | `RSA_sign` | `0xCF180` | 98 | UnwindData |  |
| 2345 | `RSA_verify` | `0xCF2E0` | 100 | UnwindData |  |
| 2378 | `SHA1` | `0xCF990` | 138 | UnwindData |  |
| 2379 | `SHA1_Final` | `0xCFAB0` | 379 | UnwindData |  |
| 2381 | `SHA1_Transform` | `0xCFC30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2382 | `SHA1_Update` | `0xCFC40` | 305 | UnwindData |  |
| 2383 | `SHA224` | `0xCFD80` | 220 | UnwindData |  |
| 2384 | `SHA224_Final` | `0xCFE60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2385 | `SHA224_Init` | `0xCFE70` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2386 | `SHA224_Update` | `0xCFED0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2387 | `SHA256` | `0xCFEE0` | 220 | UnwindData |  |
| 2388 | `SHA256_Final` | `0xCFFC0` | 474 | UnwindData |  |
| 2389 | `SHA256_Init` | `0xD01A0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2390 | `SHA256_Transform` | `0xD0200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2391 | `SHA256_Update` | `0xD0210` | 305 | UnwindData |  |
| 2392 | `SHA384` | `0xD0B30` | 303 | UnwindData |  |
| 2393 | `SHA384_Final` | `0xD0C60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2394 | `SHA384_Init` | `0xD0C70` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2395 | `SHA384_Update` | `0xD0D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2396 | `SHA512` | `0xD0D40` | 303 | UnwindData |  |
| 2397 | `SHA512_Final` | `0xD0FF0` | 1,548 | UnwindData |  |
| 2398 | `SHA512_Init` | `0xD1600` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2399 | `SHA512_Transform` | `0xD16C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2400 | `SHA512_Update` | `0xD16D0` | 258 | UnwindData |  |
| 2401 | `SM3_Final` | `0xD17E0` | 469 | UnwindData |  |
| 2402 | `SM3_Init` | `0xD19C0` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2403 | `SM3_Update` | `0xD1A20` | 305 | UnwindData |  |
| 2404 | `SM4_decrypt` | `0xD4560` | 3,441 | UnwindData |  |
| 2405 | `SM4_encrypt` | `0xD52E0` | 3,441 | UnwindData |  |
| 2406 | `SM4_set_key` | `0xD6060` | 939 | UnwindData |  |
| 3677 | `sk_delete` | `0xD6410` | 29 | UnwindData |  |
| 3678 | `sk_delete_ptr` | `0xD6490` | 121 | UnwindData |  |
| 3679 | `sk_dup` | `0xD6510` | 145 | UnwindData |  |
| 3680 | `sk_find` | `0xD65B0` | 175 | UnwindData |  |
| 3681 | `sk_find_ex` | `0xD6660` | 175 | UnwindData |  |
| 3682 | `sk_free` | `0xD6710` | 36 | UnwindData |  |
| 3683 | `sk_insert` | `0xD6740` | 100 | UnwindData |  |
| 3684 | `sk_is_sorted` | `0xD6820` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3685 | `sk_new` | `0xD6840` | 138 | UnwindData |  |
| 3686 | `sk_new_null` | `0xD68D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3687 | `sk_num` | `0xD68E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3688 | `sk_pop` | `0xD68F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3689 | `sk_pop_free` | `0xD6920` | 15 | UnwindData |  |
| 3690 | `sk_push` | `0xD69A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3691 | `sk_set` | `0xD69B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3692 | `sk_set_cmp_func` | `0xD69E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3693 | `sk_shift` | `0xD6A00` | 24 | UnwindData |  |
| 3694 | `sk_sort` | `0xD6A50` | 54 | UnwindData |  |
| 3695 | `sk_unshift` | `0xD6A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3696 | `sk_value` | `0xD6AA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3697 | `sk_zero` | `0xD6AC0` | 50 | UnwindData |  |
| 1164 | `ESS_CERT_ID_dup` | `0xD6B60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1165 | `ESS_CERT_ID_free` | `0xD6B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1167 | `ESS_CERT_ID_new` | `0xD6B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1168 | `ESS_ISSUER_SERIAL_dup` | `0xD6B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1169 | `ESS_ISSUER_SERIAL_free` | `0xD6BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1171 | `ESS_ISSUER_SERIAL_new` | `0xD6BB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1172 | `ESS_SIGNING_CERT_dup` | `0xD6BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1173 | `ESS_SIGNING_CERT_free` | `0xD6BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1175 | `ESS_SIGNING_CERT_new` | `0xD6BF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2187 | `PKCS7_to_TS_TST_INFO` | `0xD6C00` | 241 | UnwindData |  |
| 2424 | `TS_ACCURACY_dup` | `0xD6D00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2425 | `TS_ACCURACY_free` | `0xD6D10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2430 | `TS_ACCURACY_new` | `0xD6D20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2451 | `TS_MSG_IMPRINT_dup` | `0xD6D30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2452 | `TS_MSG_IMPRINT_free` | `0xD6D40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2456 | `TS_MSG_IMPRINT_new` | `0xD6D50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2463 | `TS_REQ_dup` | `0xD6D60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2465 | `TS_REQ_free` | `0xD6D70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2479 | `TS_REQ_new` | `0xD6D80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2507 | `TS_RESP_dup` | `0xD6D90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2508 | `TS_RESP_free` | `0xD6DA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2513 | `TS_RESP_new` | `0xD6DB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2520 | `TS_STATUS_INFO_dup` | `0xD6DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2521 | `TS_STATUS_INFO_free` | `0xD6DD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2526 | `TS_STATUS_INFO_new` | `0xD6DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2531 | `TS_TST_INFO_dup` | `0xD6DF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2533 | `TS_TST_INFO_free` | `0xD6E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2551 | `TS_TST_INFO_new` | `0xD6E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3290 | `d2i_ESS_CERT_ID` | `0xD6E20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3291 | `d2i_ESS_ISSUER_SERIAL` | `0xD6E30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3292 | `d2i_ESS_SIGNING_CERT` | `0xD6E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3373 | `d2i_TS_ACCURACY` | `0xD6E60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3374 | `d2i_TS_MSG_IMPRINT` | `0xD6E70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3375 | `d2i_TS_MSG_IMPRINT_bio` | `0xD6E80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3376 | `d2i_TS_MSG_IMPRINT_fp` | `0xD6EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3377 | `d2i_TS_REQ` | `0xD6EC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3378 | `d2i_TS_REQ_bio` | `0xD6ED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3379 | `d2i_TS_REQ_fp` | `0xD6EF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3380 | `d2i_TS_RESP` | `0xD6F10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3381 | `d2i_TS_RESP_bio` | `0xD6F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3382 | `d2i_TS_RESP_fp` | `0xD6F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3383 | `d2i_TS_STATUS_INFO` | `0xD6F60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3384 | `d2i_TS_TST_INFO` | `0xD6F70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3385 | `d2i_TS_TST_INFO_bio` | `0xD6F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3386 | `d2i_TS_TST_INFO_fp` | `0xD6FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3493 | `i2d_ESS_CERT_ID` | `0xD6FC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3494 | `i2d_ESS_ISSUER_SERIAL` | `0xD6FD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3495 | `i2d_ESS_SIGNING_CERT` | `0xD6FE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3581 | `i2d_TS_ACCURACY` | `0xD6FF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3582 | `i2d_TS_MSG_IMPRINT` | `0xD7000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3583 | `i2d_TS_MSG_IMPRINT_bio` | `0xD7010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3584 | `i2d_TS_MSG_IMPRINT_fp` | `0xD7030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3585 | `i2d_TS_REQ` | `0xD7050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3586 | `i2d_TS_REQ_bio` | `0xD7060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3587 | `i2d_TS_REQ_fp` | `0xD7080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3588 | `i2d_TS_RESP` | `0xD70A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3589 | `i2d_TS_RESP_bio` | `0xD70B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3590 | `i2d_TS_RESP_fp` | `0xD70D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3591 | `i2d_TS_STATUS_INFO` | `0xD70F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3592 | `i2d_TS_TST_INFO` | `0xD7100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3593 | `i2d_TS_TST_INFO_bio` | `0xD7110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3594 | `i2d_TS_TST_INFO_fp` | `0xD7130` | 640 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2435 | `TS_CONF_get_tsa_section` | `0xD73B0` | 16 | UnwindData |  |
| 2436 | `TS_CONF_load_cert` | `0xD7420` | 119 | UnwindData |  |
| 2437 | `TS_CONF_load_certs` | `0xD74A0` | 267 | UnwindData |  |
| 2438 | `TS_CONF_load_key` | `0xD75B0` | 132 | UnwindData |  |
| 2439 | `TS_CONF_set_accuracy` | `0xD7640` | 115 | UnwindData |  |
| 2440 | `TS_CONF_set_certs` | `0xD77E0` | 390 | UnwindData |  |
| 2441 | `TS_CONF_set_clock_precision_digits` | `0xD7970` | 178 | UnwindData |  |
| 2442 | `TS_CONF_set_def_policy` | `0xD7A30` | 199 | UnwindData |  |
| 2443 | `TS_CONF_set_digests` | `0xD7B00` | 153 | UnwindData |  |
| 2444 | `TS_CONF_set_ess_cert_id_chain` | `0xD7C50` | 32 | UnwindData |  |
| 2445 | `TS_CONF_set_ordering` | `0xD7C70` | 32 | UnwindData |  |
| 2446 | `TS_CONF_set_policies` | `0xD7C90` | 94 | UnwindData |  |
| 2447 | `TS_CONF_set_serial` | `0xD7DC0` | 129 | UnwindData |  |
| 2448 | `TS_CONF_set_signer_cert` | `0xD7E50` | 252 | UnwindData |  |
| 2449 | `TS_CONF_set_signer_key` | `0xD7F50` | 254 | UnwindData |  |
| 2450 | `TS_CONF_set_tsa_name` | `0xD8050` | 32 | UnwindData |  |
| 1141 | `ERR_load_TS_strings` | `0xD8070` | 57 | UnwindData |  |
| 2434 | `TS_ASN1_INTEGER_print_bio` | `0xD80B0` | 159 | UnwindData |  |
| 2457 | `TS_MSG_IMPRINT_print_bio` | `0xD8150` | 160 | UnwindData |  |
| 2460 | `TS_OBJ_print_bio` | `0xD81F0` | 131 | UnwindData |  |
| 2571 | `TS_X509_ALGOR_print_bio` | `0xD8280` | 60 | UnwindData |  |
| 2572 | `TS_ext_print_bio` | `0xD82C0` | 51 | UnwindData |  |
| 2480 | `TS_REQ_print_bio` | `0xD83D0` | 284 | UnwindData |  |
| 2458 | `TS_MSG_IMPRINT_set_algo` | `0xD84F0` | 28 | UnwindData |  |
| 2459 | `TS_MSG_IMPRINT_set_msg` | `0xD8570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2461 | `TS_REQ_add_ext` | `0xD8580` | 28 | UnwindData |  |
| 2462 | `TS_REQ_delete_ext` | `0xD85A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2464 | `TS_REQ_ext_free` | `0xD85B0` | 43 | UnwindData |  |
| 2466 | `TS_REQ_get_cert_req` | `0xD85E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2467 | `TS_REQ_get_ext` | `0xD85F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2468 | `TS_REQ_get_ext_by_NID` | `0xD8600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2469 | `TS_REQ_get_ext_by_OBJ` | `0xD8610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2470 | `TS_REQ_get_ext_by_critical` | `0xD8620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2471 | `TS_REQ_get_ext_count` | `0xD8630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2472 | `TS_REQ_get_ext_d2i` | `0xD8640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2477 | `TS_REQ_get_version` | `0xD8650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2549 | `TS_TST_INFO_get_version` | `0xD8650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2481 | `TS_REQ_set_cert_req` | `0xD8660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2482 | `TS_REQ_set_msg_imprint` | `0xD8670` | 29 | UnwindData |  |
| 2483 | `TS_REQ_set_nonce` | `0xD86F0` | 29 | UnwindData |  |
| 2484 | `TS_REQ_set_policy_id` | `0xD8770` | 29 | UnwindData |  |
| 2485 | `TS_REQ_set_version` | `0xD87F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2528 | `TS_STATUS_INFO_set_status` | `0xD87F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2561 | `TS_TST_INFO_set_version` | `0xD87F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2514 | `TS_RESP_print_bio` | `0xD8800` | 488 | UnwindData |  |
| 2527 | `TS_STATUS_INFO_print_bio` | `0xD89F0` | 404 | UnwindData |  |
| 2552 | `TS_TST_INFO_print_bio` | `0xD8B90` | 290 | UnwindData |  |
| 2487 | `TS_RESP_CTX_add_failure_info` | `0xD9010` | 135 | UnwindData |  |
| 2488 | `TS_RESP_CTX_add_flags` | `0xD90A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2489 | `TS_RESP_CTX_add_md` | `0xD90B0` | 119 | UnwindData |  |
| 2490 | `TS_RESP_CTX_add_policy` | `0xD9130` | 158 | UnwindData |  |
| 2491 | `TS_RESP_CTX_free` | `0xD91D0` | 121 | UnwindData |  |
| 2493 | `TS_RESP_CTX_get_tst_info` | `0xD9250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2494 | `TS_RESP_CTX_new` | `0xD9260` | 105 | UnwindData |  |
| 2495 | `TS_RESP_CTX_set_accuracy` | `0xD92D0` | 361 | UnwindData |  |
| 2496 | `TS_RESP_CTX_set_certs` | `0xD9440` | 218 | UnwindData |  |
| 2497 | `TS_RESP_CTX_set_clock_precision_digits` | `0xD9520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2498 | `TS_RESP_CTX_set_def_policy` | `0xD9540` | 112 | UnwindData |  |
| 2501 | `TS_RESP_CTX_set_signer_cert` | `0xD95B0` | 144 | UnwindData |  |
| 2502 | `TS_RESP_CTX_set_signer_key` | `0xD9640` | 76 | UnwindData |  |
| 2503 | `TS_RESP_CTX_set_status_info` | `0xD9690` | 254 | UnwindData |  |
| 2504 | `TS_RESP_CTX_set_status_info_cond` | `0xD9790` | 96 | UnwindData |  |
| 2506 | `TS_RESP_create_response` | `0xD9B80` | 995 | UnwindData |  |
| 2431 | `TS_ACCURACY_set_micros` | `0xDAF30` | 120 | UnwindData |  |
| 2432 | `TS_ACCURACY_set_millis` | `0xDAFB0` | 120 | UnwindData |  |
| 2433 | `TS_ACCURACY_set_seconds` | `0xDB030` | 28 | UnwindData |  |
| 2515 | `TS_RESP_set_status_info` | `0xDB0B0` | 28 | UnwindData |  |
| 2516 | `TS_RESP_set_tst_info` | `0xDB130` | 66 | UnwindData |  |
| 2529 | `TS_TST_INFO_add_ext` | `0xDB180` | 28 | UnwindData |  |
| 2530 | `TS_TST_INFO_delete_ext` | `0xDB1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2532 | `TS_TST_INFO_ext_free` | `0xDB1B0` | 43 | UnwindData |  |
| 2535 | `TS_TST_INFO_get_ext` | `0xDB1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2536 | `TS_TST_INFO_get_ext_by_NID` | `0xDB1F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2537 | `TS_TST_INFO_get_ext_by_OBJ` | `0xDB200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2538 | `TS_TST_INFO_get_ext_by_critical` | `0xDB210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2539 | `TS_TST_INFO_get_ext_count` | `0xDB220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2540 | `TS_TST_INFO_get_ext_d2i` | `0xDB230` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2544 | `TS_TST_INFO_get_ordering` | `0xDB240` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2553 | `TS_TST_INFO_set_accuracy` | `0xDB250` | 29 | UnwindData |  |
| 2554 | `TS_TST_INFO_set_msg_imprint` | `0xDB2D0` | 29 | UnwindData |  |
| 2555 | `TS_TST_INFO_set_nonce` | `0xDB350` | 29 | UnwindData |  |
| 2556 | `TS_TST_INFO_set_ordering` | `0xDB3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2557 | `TS_TST_INFO_set_policy_id` | `0xDB3E0` | 29 | UnwindData |  |
| 2558 | `TS_TST_INFO_set_serial` | `0xDB460` | 29 | UnwindData |  |
| 2559 | `TS_TST_INFO_set_time` | `0xDB4E0` | 29 | UnwindData |  |
| 2560 | `TS_TST_INFO_set_tsa` | `0xDB560` | 29 | UnwindData |  |
| 2517 | `TS_RESP_verify_response` | `0xDB5E0` | 121 | UnwindData |  |
| 2518 | `TS_RESP_verify_signature` | `0xDB660` | 171 | UnwindData |  |
| 2519 | `TS_RESP_verify_token` | `0xDB980` | 95 | UnwindData |  |
| 2486 | `TS_REQ_to_TS_VERIFY_CTX` | `0xDC840` | 984 | UnwindData |  |
| 2562 | `TS_VERIFY_CTX_add_flags` | `0xDCC20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2563 | `TS_VERIFY_CTX_cleanup` | `0xDCC30` | 120 | UnwindData |  |
| 2564 | `TS_VERIFY_CTX_free` | `0xDCCB0` | 128 | UnwindData |  |
| 2565 | `TS_VERIFY_CTX_new` | `0xDCD30` | 74 | UnwindData |  |
| 2566 | `TS_VERIFY_CTX_set_certs` | `0xDCD80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2567 | `TS_VERIFY_CTX_set_data` | `0xDCD90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2568 | `TS_VERIFY_CTX_set_flags` | `0xDCDA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2569 | `TS_VERIFY_CTX_set_imprint` | `0xDCDB0` | 59 | UnwindData |  |
| 2570 | `TS_VERIFY_CTX_set_store` | `0xDCDF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2573 | `TXT_DB_create_index` | `0xDCE00` | 49 | UnwindData |  |
| 2574 | `TXT_DB_free` | `0xDCF40` | 22 | UnwindData |  |
| 2575 | `TXT_DB_get_by_index` | `0xDD080` | 83 | UnwindData |  |
| 2576 | `TXT_DB_insert` | `0xDD0E0` | 271 | UnwindData |  |
| 2577 | `TXT_DB_read` | `0xDD1F0` | 967 | UnwindData |  |
| 2578 | `TXT_DB_write` | `0xDD5C0` | 54 | UnwindData |  |
| 1142 | `ERR_load_UI_strings` | `0xDD720` | 57 | UnwindData |  |
| 2582 | `UI_add_error_string` | `0xDD760` | 47 | UnwindData |  |
| 2583 | `UI_add_info_string` | `0xDD790` | 47 | UnwindData |  |
| 2584 | `UI_add_input_boolean` | `0xDD7C0` | 386 | UnwindData |  |
| 2585 | `UI_add_input_string` | `0xDD950` | 64 | UnwindData |  |
| 2586 | `UI_add_user_data` | `0xDD990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2587 | `UI_add_verify_string` | `0xDD9A0` | 68 | UnwindData |  |
| 2588 | `UI_construct_prompt` | `0xDD9F0` | 99 | UnwindData |  |
| 2589 | `UI_create_method` | `0xDDA60` | 100 | UnwindData |  |
| 2590 | `UI_ctrl` | `0xDDAD0` | 161 | UnwindData |  |
| 2592 | `UI_dup_error_string` | `0xDDB80` | 50 | UnwindData |  |
| 2593 | `UI_dup_info_string` | `0xDDBC0` | 50 | UnwindData |  |
| 2594 | `UI_dup_input_boolean` | `0xDDC00` | 67 | UnwindData |  |
| 2595 | `UI_dup_input_string` | `0xDDC50` | 64 | UnwindData |  |
| 2596 | `UI_dup_verify_string` | `0xDDC90` | 71 | UnwindData |  |
| 2597 | `UI_free` | `0xDDCE0` | 60 | UnwindData |  |
| 2598 | `UI_get0_action_string` | `0xDDD20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2599 | `UI_get0_output_string` | `0xDDD40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2614 | `UI_method_get_opener` | `0xDDD40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2799 | `X509_NAME_ENTRY_get_data` | `0xDDD40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2600 | `UI_get0_result` | `0xDDD50` | 179 | UnwindData |  |
| 2601 | `UI_get0_result_string` | `0xDDE10` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2602 | `UI_get0_test_string` | `0xDDE30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2604 | `UI_get_default_method` | `0xDDE50` | 33 | UnwindData |  |
| 2605 | `UI_get_ex_data` | `0xDDE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2606 | `UI_get_ex_new_index` | `0xDDE90` | 42 | UnwindData |  |
| 2607 | `UI_get_input_flags` | `0xDDEC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2609 | `UI_get_result_maxsize` | `0xDDED0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2610 | `UI_get_result_minsize` | `0xDDF00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2611 | `UI_get_string_type` | `0xDDF30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2612 | `UI_method_get_closer` | `0xDDF40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2615 | `UI_method_get_prompt_constructor` | `0xDDF50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2616 | `UI_method_get_reader` | `0xDDF60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2617 | `UI_method_get_writer` | `0xDDF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2772 | `X509_EXTENSION_get_data` | `0xDDF70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2618 | `UI_method_set_closer` | `0xDDF80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2619 | `UI_method_set_flusher` | `0xDDFA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2620 | `UI_method_set_opener` | `0xDDFC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2621 | `UI_method_set_prompt_constructor` | `0xDDFE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2622 | `UI_method_set_reader` | `0xDE000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2623 | `UI_method_set_writer` | `0xDE020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2624 | `UI_new` | `0xDE040` | 133 | UnwindData |  |
| 2625 | `UI_new_method` | `0xDE0D0` | 151 | UnwindData |  |
| 2627 | `UI_process` | `0xDE170` | 72 | UnwindData |  |
| 2628 | `UI_set_default_method` | `0xDE2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2629 | `UI_set_ex_data` | `0xDE300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2630 | `UI_set_method` | `0xDE310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2631 | `UI_set_result` | `0xDE320` | 446 | UnwindData |  |
| 2626 | `UI_null` | `0xDEA40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2580 | `UI_UTIL_read_pw` | `0xDEA50` | 57 | UnwindData |  |
| 2581 | `UI_UTIL_read_pw_string` | `0xDEB30` | 80 | UnwindData |  |
| 2635 | `WHIRLPOOL` | `0xDEC40` | 126 | UnwindData |  |
| 2636 | `WHIRLPOOL_BitUpdate` | `0xDECC0` | 672 | UnwindData |  |
| 2637 | `WHIRLPOOL_Final` | `0xDEF60` | 351 | UnwindData |  |
| 2638 | `WHIRLPOOL_Init` | `0xDF0C0` | 27 | UnwindData |  |
| 2639 | `WHIRLPOOL_Update` | `0xDF0E0` | 33 | UnwindData |  |
| 2788 | `X509_LOOKUP_hash_dir` | `0xDF9D0` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2786 | `X509_LOOKUP_file` | `0xDFD00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3118 | `X509_load_cert_crl_file` | `0xDFD10` | 41 | UnwindData |  |
| 3119 | `X509_load_cert_file` | `0xDFEA0` | 419 | UnwindData |  |
| 3120 | `X509_load_crl_file` | `0xE0050` | 419 | UnwindData |  |
| 2790 | `X509_LOOKUP_mem` | `0xE0360` | 3,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1662 | `IPAddressChoice_free` | `0xE0FB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1664 | `IPAddressChoice_new` | `0xE0FC0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1665 | `IPAddressFamily_free` | `0xE1190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1667 | `IPAddressFamily_new` | `0xE11A0` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1668 | `IPAddressOrRange_free` | `0xE13C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1670 | `IPAddressOrRange_new` | `0xE13D0` | 800 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1671 | `IPAddressRange_free` | `0xE16F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1673 | `IPAddressRange_new` | `0xE1700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3166 | `X509v3_addr_add_inherit` | `0xE1710` | 149 | UnwindData |  |
| 3167 | `X509v3_addr_add_prefix` | `0xE17B0` | 132 | UnwindData |  |
| 3168 | `X509v3_addr_add_range` | `0xE1840` | 160 | UnwindData |  |
| 3169 | `X509v3_addr_canonize` | `0xE18E0` | 307 | UnwindData |  |
| 3170 | `X509v3_addr_get_afi` | `0xE1A20` | 143 | UnwindData |  |
| 3171 | `X509v3_addr_get_range` | `0xE1AB0` | 183 | UnwindData |  |
| 3172 | `X509v3_addr_inherits` | `0xE1B70` | 125 | UnwindData |  |
| 3173 | `X509v3_addr_is_canonical` | `0xE1BF0` | 1,033 | UnwindData |  |
| 3174 | `X509v3_addr_subset` | `0xE2000` | 337 | UnwindData |  |
| 3175 | `X509v3_addr_validate_path` | `0xE2160` | 73 | UnwindData |  |
| 3176 | `X509v3_addr_validate_resource_set` | `0xE21B0` | 124 | UnwindData |  |
| 3297 | `d2i_IPAddressChoice` | `0xE2A50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3298 | `d2i_IPAddressFamily` | `0xE2A60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3299 | `d2i_IPAddressOrRange` | `0xE2A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3300 | `d2i_IPAddressRange` | `0xE2A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3500 | `i2d_IPAddressChoice` | `0xE2A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3501 | `i2d_IPAddressFamily` | `0xE2AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3502 | `i2d_IPAddressOrRange` | `0xE2AB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3503 | `i2d_IPAddressRange` | `0xE2AC0` | 4,448 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 225 | `AUTHORITY_KEYID_free` | `0xE3C20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 227 | `AUTHORITY_KEYID_new` | `0xE3C30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3252 | `d2i_AUTHORITY_KEYID` | `0xE3C40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3455 | `i2d_AUTHORITY_KEYID` | `0xE3C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3634 | `i2v_GENERAL_NAMES` | `0xE3C60` | 180 | UnwindData |  |
| 1611 | `GENERAL_NAME_print` | `0xE4180` | 800 | UnwindData |  |
| 3211 | `a2i_GENERAL_NAME` | `0xE44A0` | 86 | UnwindData |  |
| 3633 | `i2v_GENERAL_NAME` | `0xE49C0` | 1,216 | UnwindData |  |
| 3709 | `v2i_GENERAL_NAME` | `0xE4E80` | 33 | UnwindData |  |
| 3710 | `v2i_GENERAL_NAMES` | `0xE4EB0` | 89 | UnwindData |  |
| 3711 | `v2i_GENERAL_NAME_ex` | `0xE4FC0` | 294 | UnwindData |  |
| 18 | `ASIdOrRange_free` | `0xE59C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `ASIdOrRange_new` | `0xE59D0` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `ASIdentifierChoice_free` | `0xE5DD0` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `ASIdentifierChoice_new` | `0xE6040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `ASIdentifiers_free` | `0xE6050` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `ASIdentifiers_new` | `0xE6060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | `ASRange_free` | `0xE6070` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `ASRange_new` | `0xE6080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3177 | `X509v3_asid_add_id_or_range` | `0xE6090` | 297 | UnwindData |  |
| 3178 | `X509v3_asid_add_inherit` | `0xE61C0` | 115 | UnwindData |  |
| 3179 | `X509v3_asid_canonize` | `0xE6240` | 57 | UnwindData |  |
| 3180 | `X509v3_asid_inherits` | `0xE6280` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3181 | `X509v3_asid_is_canonical` | `0xE62B0` | 58 | UnwindData |  |
| 3182 | `X509v3_asid_subset` | `0xE62F0` | 184 | UnwindData |  |
| 3183 | `X509v3_asid_validate_path` | `0xE63B0` | 73 | UnwindData |  |
| 3184 | `X509v3_asid_validate_resource_set` | `0xE6400` | 88 | UnwindData |  |
| 3225 | `d2i_ASIdOrRange` | `0xE6B80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3226 | `d2i_ASIdentifierChoice` | `0xE6B90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3227 | `d2i_ASIdentifiers` | `0xE6BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3250 | `d2i_ASRange` | `0xE6BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3429 | `i2d_ASIdOrRange` | `0xE6BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3430 | `i2d_ASIdentifierChoice` | `0xE6BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3431 | `i2d_ASIdentifiers` | `0xE6BE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3453 | `i2d_ASRange` | `0xE6BF0` | 416 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2694 | `X509_ATTRIBUTE_count` | `0xE6D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2696 | `X509_ATTRIBUTE_create_by_NID` | `0xE6DB0` | 149 | UnwindData |  |
| 2697 | `X509_ATTRIBUTE_create_by_OBJ` | `0xE6E50` | 97 | UnwindData |  |
| 2698 | `X509_ATTRIBUTE_create_by_txt` | `0xE7060` | 177 | UnwindData |  |
| 2701 | `X509_ATTRIBUTE_get0_data` | `0xE7120` | 111 | UnwindData |  |
| 2703 | `X509_ATTRIBUTE_get0_type` | `0xE7190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2706 | `X509_ATTRIBUTE_set1_data` | `0xE71B0` | 51 | UnwindData |  |
| 2707 | `X509_ATTRIBUTE_set1_object` | `0xE7310` | 79 | UnwindData |  |
| 2778 | `X509_EXTENSION_set_object` | `0xE7310` | 79 | UnwindData |  |
| 3155 | `X509at_add1_attr` | `0xE7360` | 82 | UnwindData |  |
| 3156 | `X509at_add1_attr_by_NID` | `0xE7460` | 174 | UnwindData |  |
| 3157 | `X509at_add1_attr_by_OBJ` | `0xE7510` | 83 | UnwindData |  |
| 3158 | `X509at_add1_attr_by_txt` | `0xE7570` | 207 | UnwindData |  |
| 3159 | `X509at_delete_attr` | `0xE7640` | 69 | UnwindData |  |
| 3185 | `X509v3_delete_ext` | `0xE7640` | 69 | UnwindData |  |
| 3160 | `X509at_get0_data_by_OBJ` | `0xE7690` | 402 | UnwindData |  |
| 3161 | `X509at_get_attr` | `0xE7830` | 69 | UnwindData |  |
| 3186 | `X509v3_get_ext` | `0xE7830` | 69 | UnwindData |  |
| 3162 | `X509at_get_attr_by_NID` | `0xE7880` | 176 | UnwindData |  |
| 3187 | `X509v3_get_ext_by_NID` | `0xE7880` | 176 | UnwindData |  |
| 3163 | `X509at_get_attr_by_OBJ` | `0xE7930` | 125 | UnwindData |  |
| 3188 | `X509v3_get_ext_by_OBJ` | `0xE7930` | 125 | UnwindData |  |
| 3164 | `X509at_get_attr_count` | `0xE79B0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 228 | `BASIC_CONSTRAINTS_free` | `0xE7BA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 230 | `BASIC_CONSTRAINTS_new` | `0xE7BB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3254 | `d2i_BASIC_CONSTRAINTS` | `0xE7BC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3456 | `i2d_BASIC_CONSTRAINTS` | `0xE7BD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3708 | `v2i_ASN1_BIT_STRING` | `0xE7BE0` | 78 | UnwindData |  |
| 3632 | `i2v_ASN1_BIT_STRING` | `0xE7D80` | 74 | UnwindData |  |
| 2723 | `X509_CRL_cmp` | `0xE7E40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2749 | `X509_CRL_match` | `0xE7E60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2811 | `X509_NAME_cmp` | `0xE7E80` | 120 | UnwindData |  |
| 2823 | `X509_NAME_hash` | `0xE7F00` | 144 | UnwindData |  |
| 2824 | `X509_NAME_hash_old` | `0xE7F90` | 193 | UnwindData |  |
| 3049 | `X509_chain_up_ref` | `0xE8060` | 86 | UnwindData |  |
| 3057 | `X509_check_private_key` | `0xE80C0` | 147 | UnwindData |  |
| 3060 | `X509_cmp` | `0xE8160` | 80 | UnwindData |  |
| 3067 | `X509_find_by_issuer_and_serial` | `0xE81B0` | 149 | UnwindData |  |
| 3068 | `X509_find_by_subject` | `0xE8250` | 202 | UnwindData |  |
| 3073 | `X509_get0_pubkey` | `0xE8320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3074 | `X509_get0_pubkey_bitstr` | `0xE8340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3100 | `X509_get_pubkey` | `0xE8360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3110 | `X509_issuer_and_serial_cmp` | `0xE8380` | 57 | UnwindData |  |
| 3111 | `X509_issuer_and_serial_hash` | `0xE83C0` | 273 | UnwindData |  |
| 3112 | `X509_issuer_name_cmp` | `0xE84E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3113 | `X509_issuer_name_hash` | `0xE8500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3114 | `X509_issuer_name_hash_old` | `0xE8510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3143 | `X509_subject_name_cmp` | `0xE8520` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3144 | `X509_subject_name_hash` | `0xE8540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3145 | `X509_subject_name_hash_old` | `0xE8550` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2642 | `X509V3_EXT_CRL_add_conf` | `0xE85A0` | 84 | UnwindData |  |
| 2643 | `X509V3_EXT_CRL_add_nconf` | `0xE8600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2644 | `X509V3_EXT_REQ_add_conf` | `0xE8620` | 144 | UnwindData |  |
| 2645 | `X509V3_EXT_REQ_add_nconf` | `0xE86B0` | 94 | UnwindData |  |
| 2648 | `X509V3_EXT_add_conf` | `0xE8710` | 84 | UnwindData |  |
| 2650 | `X509V3_EXT_add_nconf` | `0xE8770` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2651 | `X509V3_EXT_add_nconf_sk` | `0xE8790` | 555 | UnwindData |  |
| 2653 | `X509V3_EXT_conf` | `0xE89C0` | 72 | UnwindData |  |
| 2654 | `X509V3_EXT_conf_nid` | `0xE8A10` | 356 | UnwindData |  |
| 2658 | `X509V3_EXT_i2d` | `0xE8B80` | 117 | UnwindData |  |
| 2659 | `X509V3_EXT_nconf` | `0xE8C00` | 422 | UnwindData |  |
| 2660 | `X509V3_EXT_nconf_nid` | `0xE8DB0` | 357 | UnwindData |  |
| 2675 | `X509V3_get_section` | `0xE8F20` | 88 | UnwindData |  |
| 2676 | `X509V3_get_string` | `0xE8F80` | 87 | UnwindData |  |
| 2680 | `X509V3_section_free` | `0xE8FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2681 | `X509V3_set_conf_lhash` | `0xE9000` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2682 | `X509V3_set_ctx` | `0xE9010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2683 | `X509V3_set_nconf` | `0xE9030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2684 | `X509V3_string_free` | `0xE9040` | 11,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 498 | `CERTIFICATEPOLICIES_free` | `0xEBB70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 500 | `CERTIFICATEPOLICIES_new` | `0xEBB80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1718 | `NOTICEREF_free` | `0xEBB90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1720 | `NOTICEREF_new` | `0xEBBA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2203 | `POLICYINFO_free` | `0xEBBB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2205 | `POLICYINFO_new` | `0xEBBC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2206 | `POLICYQUALINFO_free` | `0xEBBD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2208 | `POLICYQUALINFO_new` | `0xEBBE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2632 | `USERNOTICE_free` | `0xEBBF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2634 | `USERNOTICE_new` | `0xEBC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3255 | `d2i_CERTIFICATEPOLICIES` | `0xEBC10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3304 | `d2i_NOTICEREF` | `0xEBC20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3352 | `d2i_POLICYINFO` | `0xEBC30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3353 | `d2i_POLICYQUALINFO` | `0xEBC40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3387 | `d2i_USERNOTICE` | `0xEBC50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3457 | `i2d_CERTIFICATEPOLICIES` | `0xEBC60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3507 | `i2d_NOTICEREF` | `0xEBC70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3560 | `i2d_POLICYINFO` | `0xEBC80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3561 | `i2d_POLICYQUALINFO` | `0xEBC90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3595 | `i2d_USERNOTICE` | `0xEBCA0` | 3,472 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 652 | `CRL_DIST_POINTS_free` | `0xECA30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 654 | `CRL_DIST_POINTS_new` | `0xECA40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 875 | `DIST_POINT_NAME_free` | `0xECA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 877 | `DIST_POINT_NAME_new` | `0xECA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 878 | `DIST_POINT_free` | `0xECA70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 880 | `DIST_POINT_new` | `0xECA80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 881 | `DIST_POINT_set_dpname` | `0xECA90` | 192 | UnwindData |  |
| 1674 | `ISSUING_DIST_POINT_free` | `0xECB50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1676 | `ISSUING_DIST_POINT_new` | `0xECB60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3259 | `d2i_CRL_DIST_POINTS` | `0xECB70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3265 | `d2i_DIST_POINT` | `0xECB80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3266 | `d2i_DIST_POINT_NAME` | `0xECB90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3301 | `d2i_ISSUING_DIST_POINT` | `0xECBA0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3462 | `i2d_CRL_DIST_POINTS` | `0xECC70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3468 | `i2d_DIST_POINT` | `0xECC80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3469 | `i2d_DIST_POINT_NAME` | `0xECC90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3504 | `i2d_ISSUING_DIST_POINT` | `0xECCA0` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2985 | `X509_STORE_load_locations` | `0xED1F0` | 180 | UnwindData |  |
| 2986 | `X509_STORE_load_mem` | `0xED2B0` | 126 | UnwindData |  |
| 2990 | `X509_STORE_set_default_paths` | `0xED330` | 137 | UnwindData |  |
| 3082 | `X509_get_default_cert_area` | `0xED3C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3083 | `X509_get_default_cert_dir` | `0xED3D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3084 | `X509_get_default_cert_dir_env` | `0xED3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3085 | `X509_get_default_cert_file` | `0xED3F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3086 | `X509_get_default_cert_file_env` | `0xED400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3087 | `X509_get_default_private_dir` | `0xED410` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1143 | `ERR_load_X509V3_strings` | `0xED420` | 57 | UnwindData |  |
| 1144 | `ERR_load_X509_strings` | `0xED460` | 57 | UnwindData |  |
| 2721 | `X509_CRL_add1_ext_i2d` | `0xED4A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2722 | `X509_CRL_add_ext` | `0xED4B0` | 31 | UnwindData |  |
| 2724 | `X509_CRL_delete_ext` | `0xED4D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2736 | `X509_CRL_get_ext` | `0xED4E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2737 | `X509_CRL_get_ext_by_NID` | `0xED4F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2738 | `X509_CRL_get_ext_by_OBJ` | `0xED500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2739 | `X509_CRL_get_ext_by_critical` | `0xED510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2740 | `X509_CRL_get_ext_count` | `0xED520` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2741 | `X509_CRL_get_ext_d2i` | `0xED530` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2903 | `X509_REVOKED_add1_ext_i2d` | `0xED540` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2904 | `X509_REVOKED_add_ext` | `0xED550` | 28 | UnwindData |  |
| 2905 | `X509_REVOKED_delete_ext` | `0xED570` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2911 | `X509_REVOKED_get_ext` | `0xED580` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2912 | `X509_REVOKED_get_ext_by_NID` | `0xED590` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2913 | `X509_REVOKED_get_ext_by_OBJ` | `0xED5A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2914 | `X509_REVOKED_get_ext_by_critical` | `0xED5B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2915 | `X509_REVOKED_get_ext_count` | `0xED5C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2916 | `X509_REVOKED_get_ext_d2i` | `0xED5D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3042 | `X509_add1_ext_i2d` | `0xED5E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3045 | `X509_add_ext` | `0xED5F0` | 31 | UnwindData |  |
| 3063 | `X509_delete_ext` | `0xED610` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3090 | `X509_get_ext` | `0xED620` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3091 | `X509_get_ext_by_NID` | `0xED630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3092 | `X509_get_ext_by_OBJ` | `0xED640` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3093 | `X509_get_ext_by_critical` | `0xED650` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3094 | `X509_get_ext_count` | `0xED660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3095 | `X509_get_ext_d2i` | `0xED670` | 624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1596 | `EXTENDED_KEY_USAGE_free` | `0xED8E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1598 | `EXTENDED_KEY_USAGE_new` | `0xED8F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3293 | `d2i_EXTENDED_KEY_USAGE` | `0xED900` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3496 | `i2d_EXTENDED_KEY_USAGE` | `0xED910` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1085 | `EDIPARTYNAME_free` | `0xED920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1087 | `EDIPARTYNAME_new` | `0xED930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1601 | `GENERAL_NAMES_free` | `0xED940` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1603 | `GENERAL_NAMES_new` | `0xED950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1604 | `GENERAL_NAME_cmp` | `0xED960` | 52 | UnwindData |  |
| 1605 | `GENERAL_NAME_dup` | `0xEDAE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1606 | `GENERAL_NAME_free` | `0xEDAF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1607 | `GENERAL_NAME_get0_otherName` | `0xEDB00` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1608 | `GENERAL_NAME_get0_value` | `0xEDB40` | 96 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1610 | `GENERAL_NAME_new` | `0xEDBA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1612 | `GENERAL_NAME_set0_othername` | `0xEDBB0` | 95 | UnwindData |  |
| 1613 | `GENERAL_NAME_set0_value` | `0xEDC10` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1902 | `OTHERNAME_cmp` | `0xEDC60` | 80 | UnwindData |  |
| 1903 | `OTHERNAME_free` | `0xEDCB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1905 | `OTHERNAME_new` | `0xEDCC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3289 | `d2i_EDIPARTYNAME` | `0xEDCD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3294 | `d2i_GENERAL_NAME` | `0xEDCE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3295 | `d2i_GENERAL_NAMES` | `0xEDCF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3322 | `d2i_OTHERNAME` | `0xEDD00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3492 | `i2d_EDIPARTYNAME` | `0xEDD10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3497 | `i2d_GENERAL_NAME` | `0xEDD20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3498 | `i2d_GENERAL_NAMES` | `0xEDD30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3525 | `i2d_OTHERNAME` | `0xEDD40` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `ACCESS_DESCRIPTION_free` | `0xEE270` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `ACCESS_DESCRIPTION_new` | `0xEE280` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `AUTHORITY_INFO_ACCESS_free` | `0xEE290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `AUTHORITY_INFO_ACCESS_new` | `0xEE2A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3224 | `d2i_ACCESS_DESCRIPTION` | `0xEE2B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3251 | `d2i_AUTHORITY_INFO_ACCESS` | `0xEE2C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3420 | `i2a_ACCESS_DESCRIPTION` | `0xEE2D0` | 22 | UnwindData |  |
| 3428 | `i2d_ACCESS_DESCRIPTION` | `0xEE2F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3454 | `i2d_AUTHORITY_INFO_ACCESS` | `0xEE300` | 2,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2646 | `X509V3_EXT_add` | `0xEEE70` | 125 | UnwindData |  |
| 2647 | `X509V3_EXT_add_alias` | `0xEEEF0` | 81 | UnwindData |  |
| 2649 | `X509V3_EXT_add_list` | `0xEF010` | 139 | UnwindData |  |
| 2652 | `X509V3_EXT_cleanup` | `0xEF0A0` | 39 | UnwindData |  |
| 2655 | `X509V3_EXT_d2i` | `0xEF0D0` | 100 | UnwindData |  |
| 2656 | `X509V3_EXT_get` | `0xEF140` | 34 | UnwindData |  |
| 2657 | `X509V3_EXT_get_nid` | `0xEF170` | 141 | UnwindData |  |
| 2665 | `X509V3_add1_i2d` | `0xEF200` | 409 | UnwindData |  |
| 2674 | `X509V3_get_d2i` | `0xEF3A0` | 368 | UnwindData |  |
| 2781 | `X509_LOOKUP_by_alias` | `0xEF520` | 56 | UnwindData |  |
| 2782 | `X509_LOOKUP_by_fingerprint` | `0xEF560` | 56 | UnwindData |  |
| 2783 | `X509_LOOKUP_by_issuer_serial` | `0xEF5A0` | 56 | UnwindData |  |
| 2784 | `X509_LOOKUP_by_subject` | `0xEF5E0` | 40 | UnwindData |  |
| 2785 | `X509_LOOKUP_ctrl` | `0xEF610` | 69 | UnwindData |  |
| 2787 | `X509_LOOKUP_free` | `0xEF660` | 51 | UnwindData |  |
| 2789 | `X509_LOOKUP_init` | `0xEF6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2791 | `X509_LOOKUP_new` | `0xEF6C0` | 146 | UnwindData |  |
| 2792 | `X509_LOOKUP_shutdown` | `0xEF760` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2832 | `X509_OBJECT_free` | `0xEF780` | 70 | UnwindData |  |
| 2833 | `X509_OBJECT_get0_X509` | `0xEF7D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2834 | `X509_OBJECT_get0_X509_CRL` | `0xEF7F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2836 | `X509_OBJECT_idx_by_subject` | `0xEF810` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2837 | `X509_OBJECT_new` | `0xEF820` | 78 | UnwindData |  |
| 2838 | `X509_OBJECT_retrieve_by_subject` | `0xEF870` | 45 | UnwindData |  |
| 2839 | `X509_OBJECT_retrieve_match` | `0xEF8A0` | 273 | UnwindData |  |
| 2840 | `X509_OBJECT_up_ref_count` | `0xEF9C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2936 | `X509_STORE_CTX_get1_certs` | `0xEF9F0` | 150 | UnwindData |  |
| 2938 | `X509_STORE_CTX_get1_crls` | `0xEFA90` | 97 | UnwindData |  |
| 2939 | `X509_STORE_CTX_get1_issuer` | `0xEFBF0` | 673 | UnwindData |  |
| 2940 | `X509_STORE_CTX_get_by_subject` | `0xEFEA0` | 362 | UnwindData |  |
| 2949 | `X509_STORE_CTX_get_obj_by_subject` | `0xF0010` | 195 | UnwindData |  |
| 2975 | `X509_STORE_add_cert` | `0xF00E0` | 239 | UnwindData |  |
| 2976 | `X509_STORE_add_crl` | `0xF01D0` | 239 | UnwindData |  |
| 2977 | `X509_STORE_add_lookup` | `0xF02C0` | 302 | UnwindData |  |
| 2978 | `X509_STORE_free` | `0xF05E0` | 18 | UnwindData |  |
| 2987 | `X509_STORE_new` | `0xF06F0` | 159 | UnwindData |  |
| 2988 | `X509_STORE_set1_param` | `0xF0890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2991 | `X509_STORE_set_depth` | `0xF08A0` | 23 | UnwindData |  |
| 2993 | `X509_STORE_set_flags` | `0xF08C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2994 | `X509_STORE_set_purpose` | `0xF08D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2995 | `X509_STORE_set_trust` | `0xF08E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2998 | `X509_STORE_up_ref` | `0xF08F0` | 49 | UnwindData |  |
| 1614 | `GENERAL_SUBTREE_free` | `0xF0E00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1616 | `GENERAL_SUBTREE_new` | `0xF0E10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1688 | `NAME_CONSTRAINTS_check` | `0xF0E20` | 209 | UnwindData |  |
| 1689 | `NAME_CONSTRAINTS_free` | `0xF1040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1691 | `NAME_CONSTRAINTS_new` | `0xF1050` | 1,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2827 | `X509_NAME_oneline` | `0xF1650` | 887 | UnwindData |  |
| 2209 | `POLICY_CONSTRAINTS_free` | `0xF20D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2211 | `POLICY_CONSTRAINTS_new` | `0xF20E0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2200 | `PKEY_USAGE_PERIOD_free` | `0xF21A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2202 | `PKEY_USAGE_PERIOD_new` | `0xF21B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3351 | `d2i_PKEY_USAGE_PERIOD` | `0xF21C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3559 | `i2d_PKEY_USAGE_PERIOD` | `0xF21D0` | 736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2213 | `POLICY_MAPPING_free` | `0xF24B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2215 | `POLICY_MAPPING_new` | `0xF24C0` | 4,544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2661 | `X509V3_EXT_print` | `0xF3680` | 808 | UnwindData |  |
| 2662 | `X509V3_EXT_print_fp` | `0xF39B0` | 94 | UnwindData |  |
| 2663 | `X509V3_EXT_val_prn` | `0xF3A10` | 30 | UnwindData |  |
| 2673 | `X509V3_extensions_print` | `0xF3B60` | 392 | UnwindData |  |
| 2851 | `X509_PURPOSE_add` | `0xF4050` | 58 | UnwindData |  |
| 2852 | `X509_PURPOSE_cleanup` | `0xF4250` | 39 | UnwindData |  |
| 2853 | `X509_PURPOSE_get0` | `0xF4280` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2856 | `X509_PURPOSE_get_by_id` | `0xF42C0` | 76 | UnwindData |  |
| 2857 | `X509_PURPOSE_get_by_sname` | `0xF4310` | 170 | UnwindData |  |
| 2858 | `X509_PURPOSE_get_count` | `0xF43C0` | 39 | UnwindData |  |
| 2861 | `X509_PURPOSE_set` | `0xF43F0` | 129 | UnwindData |  |
| 3050 | `X509_check_akid` | `0xF4480` | 261 | UnwindData |  |
| 3051 | `X509_check_ca` | `0xF4590` | 174 | UnwindData |  |
| 3056 | `X509_check_issued` | `0xF4640` | 246 | UnwindData |  |
| 3058 | `X509_check_purpose` | `0xF4740` | 235 | UnwindData |  |
| 3096 | `X509_get_extended_key_usage` | `0xF4830` | 107 | UnwindData |  |
| 3097 | `X509_get_extension_flags` | `0xF48A0` | 87 | UnwindData |  |
| 3099 | `X509_get_key_usage` | `0xF4900` | 107 | UnwindData |  |
| 3146 | `X509_supported_extension` | `0xF4970` | 88 | UnwindData |  |
| 2901 | `X509_REQ_to_X509` | `0xF5280` | 317 | UnwindData |  |
| 2865 | `X509_REQ_add1_attr` | `0xF53C0` | 31 | UnwindData |  |
| 2866 | `X509_REQ_add1_attr_by_NID` | `0xF53E0` | 39 | UnwindData |  |
| 2867 | `X509_REQ_add1_attr_by_OBJ` | `0xF5410` | 39 | UnwindData |  |
| 2868 | `X509_REQ_add1_attr_by_txt` | `0xF5440` | 39 | UnwindData |  |
| 2869 | `X509_REQ_add_extensions` | `0xF5470` | 108 | UnwindData |  |
| 2870 | `X509_REQ_add_extensions_nid` | `0xF54E0` | 132 | UnwindData |  |
| 2871 | `X509_REQ_check_private_key` | `0xF5570` | 235 | UnwindData |  |
| 2872 | `X509_REQ_delete_attr` | `0xF5660` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2875 | `X509_REQ_extension_nid` | `0xF5670` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2877 | `X509_REQ_get0_pubkey` | `0xF56A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2880 | `X509_REQ_get_attr` | `0xF56C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2881 | `X509_REQ_get_attr_by_NID` | `0xF56D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2882 | `X509_REQ_get_attr_by_OBJ` | `0xF56E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2883 | `X509_REQ_get_attr_count` | `0xF56F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2884 | `X509_REQ_get_extension_nids` | `0xF5700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2885 | `X509_REQ_get_extensions` | `0xF5710` | 206 | UnwindData |  |
| 2886 | `X509_REQ_get_pubkey` | `0xF57E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2895 | `X509_REQ_set_extension_nids` | `0xF5800` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3149 | `X509_to_X509_REQ` | `0xF5810` | 234 | UnwindData |  |
| 3622 | `i2d_re_X509_REQ_tbs` | `0xF5900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3070 | `X509_get0_extensions` | `0xF5920` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3071 | `X509_get0_notAfter` | `0xF5930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3107 | `X509_getm_notAfter` | `0xF5930` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3072 | `X509_get0_notBefore` | `0xF5950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3108 | `X509_getm_notBefore` | `0xF5950` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3078 | `X509_get0_uids` | `0xF5970` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3104 | `X509_get_signature_type` | `0xF5990` | 27 | UnwindData |  |
| 3129 | `X509_set1_notAfter` | `0xF59B0` | 124 | UnwindData |  |
| 3133 | `X509_set_notAfter` | `0xF59B0` | 124 | UnwindData |  |
| 3130 | `X509_set1_notBefore` | `0xF5A30` | 121 | UnwindData |  |
| 3134 | `X509_set_notBefore` | `0xF5A30` | 121 | UnwindData |  |
| 3132 | `X509_set_issuer_name` | `0xF5AB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3135 | `X509_set_pubkey` | `0xF5AE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3136 | `X509_set_serialNumber` | `0xF5B10` | 103 | UnwindData |  |
| 3137 | `X509_set_subject_name` | `0xF5B80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3138 | `X509_set_version` | `0xF5BB0` | 91 | UnwindData |  |
| 3630 | `i2s_ASN1_OCTET_STRING` | `0xF5C10` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3676 | `s2i_ASN1_OCTET_STRING` | `0xF5E00` | 138 | UnwindData |  |
| 2999 | `X509_TRUST_add` | `0xF6020` | 231 | UnwindData |  |
| 3000 | `X509_TRUST_cleanup` | `0xF6230` | 39 | UnwindData |  |
| 3001 | `X509_TRUST_get0` | `0xF6260` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3003 | `X509_TRUST_get_by_id` | `0xF62A0` | 76 | UnwindData |  |
| 3004 | `X509_TRUST_get_count` | `0xF62F0` | 39 | UnwindData |  |
| 3007 | `X509_TRUST_set` | `0xF6320` | 129 | UnwindData |  |
| 3008 | `X509_TRUST_set_default` | `0xF63B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3059 | `X509_check_trust` | `0xF63C0` | 258 | UnwindData |  |
| 3154 | `X509_verify_cert_error_string` | `0xF6500` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2664 | `X509V3_NAME_from_section` | `0xF6840` | 264 | UnwindData |  |
| 2667 | `X509V3_add_value` | `0xF6950` | 274 | UnwindData |  |
| 2668 | `X509V3_add_value_bool` | `0xF6A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2669 | `X509V3_add_value_bool_nf` | `0xF6A90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2670 | `X509V3_add_value_int` | `0xF6AB0` | 187 | UnwindData |  |
| 2671 | `X509V3_add_value_uchar` | `0xF6B70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2672 | `X509V3_conf_free` | `0xF6B80` | 53 | UnwindData |  |
| 2677 | `X509V3_get_value_bool` | `0xF6BC0` | 417 | UnwindData |  |
| 2678 | `X509V3_get_value_int` | `0xF6D70` | 87 | UnwindData |  |
| 2679 | `X509V3_parse_list` | `0xF6DD0` | 881 | UnwindData |  |
| 2879 | `X509_REQ_get1_email` | `0xF7150` | 119 | UnwindData |  |
| 3052 | `X509_check_email` | `0xF71D0` | 129 | UnwindData |  |
| 3053 | `X509_check_host` | `0xF7260` | 130 | UnwindData |  |
| 3054 | `X509_check_ip` | `0xF72F0` | 46 | UnwindData |  |
| 3055 | `X509_check_ip_asc` | `0xF7320` | 117 | UnwindData |  |
| 3066 | `X509_email_free` | `0xF73A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3079 | `X509_get1_email` | `0xF73B0` | 83 | UnwindData |  |
| 3080 | `X509_get1_ocsp` | `0xF7410` | 70 | UnwindData |  |
| 3212 | `a2i_IPADDRESS` | `0xF7540` | 116 | UnwindData |  |
| 3213 | `a2i_IPADDRESS_NC` | `0xF75C0` | 249 | UnwindData |  |
| 3214 | `a2i_ipadd` | `0xF76C0` | 55 | UnwindData |  |
| 3419 | `hex_to_string` | `0xF8270` | 320 | UnwindData |  |
| 3627 | `i2s_ASN1_ENUMERATED` | `0xF83B0` | 119 | UnwindData |  |
| 3628 | `i2s_ASN1_ENUMERATED_TABLE` | `0xF8430` | 168 | UnwindData |  |
| 3629 | `i2s_ASN1_INTEGER` | `0xF84E0` | 119 | UnwindData |  |
| 3675 | `s2i_ASN1_INTEGER` | `0xF8730` | 124 | UnwindData |  |
| 3699 | `string_to_hex` | `0xF8920` | 576 | UnwindData |  |
| 2767 | `X509_EXTENSION_create_by_NID` | `0xF8D60` | 88 | UnwindData |  |
| 2768 | `X509_EXTENSION_create_by_OBJ` | `0xF8E90` | 235 | UnwindData |  |
| 2771 | `X509_EXTENSION_get_critical` | `0xF8F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2776 | `X509_EXTENSION_set_critical` | `0xF8F90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2777 | `X509_EXTENSION_set_data` | `0xF8FC0` | 46 | UnwindData |  |
| 3165 | `X509v3_add_ext` | `0xF8FF0` | 267 | UnwindData |  |
| 3189 | `X509v3_get_ext_by_critical` | `0xF9100` | 124 | UnwindData |  |
| 3190 | `X509v3_get_ext_count` | `0xF9180` | 6,960 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2926 | `X509_STORE_CTX_cleanup` | `0xFACB0` | 131 | UnwindData |  |
| 2927 | `X509_STORE_CTX_free` | `0xFAD40` | 32 | UnwindData |  |
| 2929 | `X509_STORE_CTX_get0_chain` | `0xFAD60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2941 | `X509_STORE_CTX_get_chain` | `0xFAD60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2930 | `X509_STORE_CTX_get0_current_crl` | `0xFAD70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2931 | `X509_STORE_CTX_get0_current_issuer` | `0xFAD80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2933 | `X509_STORE_CTX_get0_parent_ctx` | `0xFAD90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2937 | `X509_STORE_CTX_get1_chain` | `0xFADA0` | 31 | UnwindData |  |
| 2943 | `X509_STORE_CTX_get_current_cert` | `0xFAE30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2944 | `X509_STORE_CTX_get_error` | `0xFAE40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2945 | `X509_STORE_CTX_get_error_depth` | `0xFAE50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2946 | `X509_STORE_CTX_get_ex_data` | `0xFAE60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2947 | `X509_STORE_CTX_get_ex_new_index` | `0xFAE70` | 42 | UnwindData |  |
| 2948 | `X509_STORE_CTX_get_num_untrusted` | `0xFAEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2952 | `X509_STORE_CTX_init` | `0xFAEB0` | 615 | UnwindData |  |
| 2953 | `X509_STORE_CTX_new` | `0xFB120` | 67 | UnwindData |  |
| 2954 | `X509_STORE_CTX_purpose_inherit` | `0xFB170` | 234 | UnwindData |  |
| 2956 | `X509_STORE_CTX_set0_param` | `0xFB260` | 45 | UnwindData |  |
| 2957 | `X509_STORE_CTX_set0_trusted_stack` | `0xFB290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2974 | `X509_STORE_CTX_trusted_stack` | `0xFB290` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2959 | `X509_STORE_CTX_set0_verified_chain` | `0xFB2A0` | 53 | UnwindData |  |
| 2962 | `X509_STORE_CTX_set_current_cert` | `0xFB2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2963 | `X509_STORE_CTX_set_default` | `0xFB2F0` | 45 | UnwindData |  |
| 2964 | `X509_STORE_CTX_set_depth` | `0xFB320` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2965 | `X509_STORE_CTX_set_error` | `0xFB330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2966 | `X509_STORE_CTX_set_error_depth` | `0xFB340` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2967 | `X509_STORE_CTX_set_ex_data` | `0xFB350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2968 | `X509_STORE_CTX_set_flags` | `0xFB360` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2969 | `X509_STORE_CTX_set_purpose` | `0xFB370` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2970 | `X509_STORE_CTX_set_time` | `0xFB380` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2971 | `X509_STORE_CTX_set_trust` | `0xFB390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3061 | `X509_cmp_current_time` | `0xFB3A0` | 82 | UnwindData |  |
| 3062 | `X509_cmp_time` | `0xFB400` | 6 | UnwindData |  |
| 3101 | `X509_get_pubkey_parameters` | `0xFB460` | 304 | UnwindData |  |
| 3109 | `X509_gmtime_adj` | `0xFB590` | 49 | UnwindData |  |
| 3147 | `X509_time_adj` | `0xFB5D0` | 59 | UnwindData |  |
| 3148 | `X509_time_adj_ex` | `0xFB610` | 72 | UnwindData |  |
| 3153 | `X509_verify_cert` | `0xFB660` | 162 | UnwindData |  |
| 3012 | `X509_VERIFY_PARAM_add0_policy` | `0xFE5A0` | 81 | UnwindData |  |
| 3013 | `X509_VERIFY_PARAM_add0_table` | `0xFE600` | 54 | UnwindData |  |
| 3014 | `X509_VERIFY_PARAM_add1_host` | `0xFE6B0` | 254 | UnwindData |  |
| 3015 | `X509_VERIFY_PARAM_clear_flags` | `0xFE7B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3016 | `X509_VERIFY_PARAM_free` | `0xFE7C0` | 32 | UnwindData |  |
| 3017 | `X509_VERIFY_PARAM_get0` | `0xFE7E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3020 | `X509_VERIFY_PARAM_get_count` | `0xFE810` | 39 | UnwindData |  |
| 3022 | `X509_VERIFY_PARAM_get_flags` | `0xFE840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3024 | `X509_VERIFY_PARAM_inherit` | `0xFE850` | 930 | UnwindData |  |
| 3025 | `X509_VERIFY_PARAM_lookup` | `0xFEC00` | 184 | UnwindData |  |
| 3026 | `X509_VERIFY_PARAM_new` | `0xFECC0` | 52 | UnwindData |  |
| 3027 | `X509_VERIFY_PARAM_set1` | `0xFED00` | 43 | UnwindData |  |
| 3028 | `X509_VERIFY_PARAM_set1_email` | `0xFED30` | 192 | UnwindData |  |
| 3029 | `X509_VERIFY_PARAM_set1_host` | `0xFEDF0` | 288 | UnwindData |  |
| 3030 | `X509_VERIFY_PARAM_set1_ip` | `0xFEF10` | 192 | UnwindData |  |
| 3031 | `X509_VERIFY_PARAM_set1_ip_asc` | `0xFEFD0` | 201 | UnwindData |  |
| 3032 | `X509_VERIFY_PARAM_set1_name` | `0xFF0A0` | 96 | UnwindData |  |
| 3033 | `X509_VERIFY_PARAM_set1_policies` | `0xFF100` | 209 | UnwindData |  |
| 3036 | `X509_VERIFY_PARAM_set_flags` | `0xFF1E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3037 | `X509_VERIFY_PARAM_set_hostflags` | `0xFF1F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3038 | `X509_VERIFY_PARAM_set_purpose` | `0xFF200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3039 | `X509_VERIFY_PARAM_set_time` | `0xFF210` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3040 | `X509_VERIFY_PARAM_set_trust` | `0xFF220` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3041 | `X509_VERIFY_PARAM_table_cleanup` | `0xFF230` | 44 | UnwindData |  |
| 2753 | `X509_CRL_set1_lastUpdate` | `0xFF320` | 93 | UnwindData |  |
| 2757 | `X509_CRL_set_lastUpdate` | `0xFF320` | 93 | UnwindData |  |
| 2754 | `X509_CRL_set1_nextUpdate` | `0xFF380` | 93 | UnwindData |  |
| 2759 | `X509_CRL_set_nextUpdate` | `0xFF380` | 93 | UnwindData |  |
| 2756 | `X509_CRL_set_issuer_name` | `0xFF3E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2760 | `X509_CRL_set_version` | `0xFF400` | 81 | UnwindData |  |
| 2763 | `X509_CRL_sort` | `0xFF460` | 109 | UnwindData |  |
| 2764 | `X509_CRL_up_ref` | `0xFF4D0` | 49 | UnwindData |  |
| 2919 | `X509_REVOKED_set_revocationDate` | `0xFF510` | 84 | UnwindData |  |
| 2920 | `X509_REVOKED_set_serialNumber` | `0xFF570` | 81 | UnwindData |  |
| 3621 | `i2d_re_X509_CRL_tbs` | `0xFF5D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2794 | `X509_NAME_ENTRY_create_by_NID` | `0xFF5F0` | 125 | UnwindData |  |
| 2795 | `X509_NAME_ENTRY_create_by_OBJ` | `0xFF760` | 344 | UnwindData |  |
| 2796 | `X509_NAME_ENTRY_create_by_txt` | `0xFF8C0` | 136 | UnwindData |  |
| 2804 | `X509_NAME_ENTRY_set_data` | `0xFFA30` | 214 | UnwindData |  |
| 2805 | `X509_NAME_ENTRY_set_object` | `0xFFB10` | 115 | UnwindData |  |
| 2807 | `X509_NAME_add_entry` | `0xFFB90` | 48 | UnwindData |  |
| 2808 | `X509_NAME_add_entry_by_NID` | `0xFFCE0` | 91 | UnwindData |  |
| 2809 | `X509_NAME_add_entry_by_OBJ` | `0xFFD40` | 340 | UnwindData |  |
| 2810 | `X509_NAME_add_entry_by_txt` | `0xFFEA0` | 91 | UnwindData |  |
| 2812 | `X509_NAME_delete_entry` | `0xFFF00` | 48 | UnwindData |  |
| 2815 | `X509_NAME_entry_count` | `0xFFFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2818 | `X509_NAME_get_entry` | `0xFFFF0` | 72 | UnwindData |  |
| 2819 | `X509_NAME_get_index_by_NID` | `0x100040` | 68 | UnwindData |  |
| 2820 | `X509_NAME_get_index_by_OBJ` | `0x100090` | 147 | UnwindData |  |
| 2821 | `X509_NAME_get_text_by_NID` | `0x100130` | 80 | UnwindData |  |
| 2822 | `X509_NAME_get_text_by_OBJ` | `0x1002A0` | 49 | UnwindData |  |
| 2889 | `X509_REQ_get_version` | `0x1003F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2896 | `X509_REQ_set_pubkey` | `0x100400` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2897 | `X509_REQ_set_subject_name` | `0x100430` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2898 | `X509_REQ_set_version` | `0x100460` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1708 | `NETSCAPE_SPKI_b64_decode` | `0x100480` | 238 | UnwindData |  |
| 1709 | `NETSCAPE_SPKI_b64_encode` | `0x100570` | 193 | UnwindData |  |
| 1711 | `NETSCAPE_SPKI_get_pubkey` | `0x100640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1715 | `NETSCAPE_SPKI_set_pubkey` | `0x100660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3048 | `X509_certificate_type` | `0x100680` | 285 | UnwindData |  |
| 1716 | `NETSCAPE_SPKI_sign` | `0x1007A0` | 50 | UnwindData |  |
| 1717 | `NETSCAPE_SPKI_verify` | `0x1007E0` | 37 | UnwindData |  |
| 2725 | `X509_CRL_digest` | `0x100810` | 32 | UnwindData |  |
| 2761 | `X509_CRL_sign` | `0x100830` | 64 | UnwindData |  |
| 2762 | `X509_CRL_sign_ctx` | `0x100870` | 59 | UnwindData |  |
| 2813 | `X509_NAME_digest` | `0x1008B0` | 32 | UnwindData |  |
| 2873 | `X509_REQ_digest` | `0x1008D0` | 32 | UnwindData |  |
| 2899 | `X509_REQ_sign` | `0x1008F0` | 50 | UnwindData |  |
| 2900 | `X509_REQ_sign_ctx` | `0x100930` | 45 | UnwindData |  |
| 2902 | `X509_REQ_verify` | `0x100960` | 37 | UnwindData |  |
| 3064 | `X509_digest` | `0x100990` | 32 | UnwindData |  |
| 3127 | `X509_pubkey_digest` | `0x1009B0` | 98 | UnwindData |  |
| 3139 | `X509_sign` | `0x100A20` | 64 | UnwindData |  |
| 3140 | `X509_sign_ctx` | `0x100A60` | 59 | UnwindData |  |
| 3151 | `X509_up_ref` | `0x100AA0` | 49 | UnwindData |  |
| 3152 | `X509_verify` | `0x100AE0` | 88 | UnwindData |  |
| 3268 | `d2i_DSAPrivateKey_bio` | `0x100B40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3269 | `d2i_DSAPrivateKey_fp` | `0x100B60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3283 | `d2i_ECPrivateKey_bio` | `0x100B80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3284 | `d2i_ECPrivateKey_fp` | `0x100BA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3347 | `d2i_PKCS8_PRIV_KEY_INFO_bio` | `0x100BC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3348 | `d2i_PKCS8_PRIV_KEY_INFO_fp` | `0x100BE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3349 | `d2i_PKCS8_bio` | `0x100C00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3350 | `d2i_PKCS8_fp` | `0x100C20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3358 | `d2i_PrivateKey_bio` | `0x100C40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3359 | `d2i_PrivateKey_fp` | `0x100C60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3362 | `d2i_RSAPrivateKey_bio` | `0x100C80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3363 | `d2i_RSAPrivateKey_fp` | `0x100CA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3365 | `d2i_RSAPublicKey_bio` | `0x100CC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3366 | `d2i_RSAPublicKey_fp` | `0x100CE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3397 | `d2i_X509_CRL_bio` | `0x100D00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3398 | `d2i_X509_CRL_fp` | `0x100D20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3406 | `d2i_X509_REQ_bio` | `0x100D40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3407 | `d2i_X509_REQ_fp` | `0x100D60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3411 | `d2i_X509_bio` | `0x100D80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3412 | `d2i_X509_fp` | `0x100DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3471 | `i2d_DSAPrivateKey_bio` | `0x100DC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3472 | `i2d_DSAPrivateKey_fp` | `0x100DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3486 | `i2d_ECPrivateKey_bio` | `0x100E00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3487 | `i2d_ECPrivateKey_fp` | `0x100E20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3548 | `i2d_PKCS8PrivateKeyInfo_bio` | `0x100E40` | 81 | UnwindData |  |
| 3549 | `i2d_PKCS8PrivateKeyInfo_fp` | `0x100EA0` | 81 | UnwindData |  |
| 3555 | `i2d_PKCS8_PRIV_KEY_INFO_bio` | `0x100F00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3556 | `i2d_PKCS8_PRIV_KEY_INFO_fp` | `0x100F20` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3557 | `i2d_PKCS8_bio` | `0x100F40` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3558 | `i2d_PKCS8_fp` | `0x100F60` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3566 | `i2d_PrivateKey_bio` | `0x100F80` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3567 | `i2d_PrivateKey_fp` | `0x100FA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3570 | `i2d_RSAPrivateKey_bio` | `0x100FC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3571 | `i2d_RSAPrivateKey_fp` | `0x100FE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3573 | `i2d_RSAPublicKey_bio` | `0x101000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3574 | `i2d_RSAPublicKey_fp` | `0x101020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3605 | `i2d_X509_CRL_bio` | `0x101040` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3606 | `i2d_X509_CRL_fp` | `0x101060` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3614 | `i2d_X509_REQ_bio` | `0x101080` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3615 | `i2d_X509_REQ_fp` | `0x1010A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3619 | `i2d_X509_bio` | `0x1010C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3620 | `i2d_X509_fp` | `0x1010E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 663 | `CRYPTO_add_lock` | `0x101100` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 722 | `CRYPTO_lock` | `0x101110` | 14 | UnwindData |  |
| 355 | `BIO_sock_init` | `0x1011C0` | 140 | UnwindData |  |
| 359 | `BIO_socket_nbio` | `0x101250` | 42 | UnwindData |  |
| 2579 | `UI_OpenSSL` | `0x101550` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3417 | `gettimeofday` | `0x101760` | 133 | UnwindData |  |
| 3662 | `posix_close` | `0x1017F0` | 121 | UnwindData |  |
| 3663 | `posix_connect` | `0x101870` | 40 | UnwindData |  |
| 3664 | `posix_fgets` | `0x1018A0` | 63 | UnwindData |  |
| 3665 | `posix_fopen` | `0x1018E0` | 138 | UnwindData |  |
| 3666 | `posix_getsockopt` | `0x101970` | 152 | UnwindData |  |
| 3667 | `posix_open` | `0x101A10` | 76 | UnwindData |  |
| 3668 | `posix_perror` | `0x101A60` | 83 | UnwindData |  |
| 3669 | `posix_read` | `0x101AC0` | 150 | UnwindData |  |
| 3670 | `posix_rename` | `0x101B60` | 29 | UnwindData |  |
| 3671 | `posix_setsockopt` | `0x101B80` | 150 | UnwindData |  |
| 3672 | `posix_write` | `0x101C20` | 150 | UnwindData |  |
| 3218 | `asprintf` | `0x101F00` | 268 | UnwindData |  |
| 3712 | `vasprintf` | `0x102010` | 264 | UnwindData |  |
| 3414 | `freezero` | `0x102190` | 32 | UnwindData |  |
| 3416 | `getopt` | `0x1021B0` | 28 | UnwindData |  |
| 3673 | `reallocarray` | `0x102C00` | 83 | UnwindData |  |
| 3674 | `recallocarray` | `0x102C60` | 257 | UnwindData |  |
| 3698 | `strcasecmp` | `0x102DE0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3700 | `strlcat` | `0x102EA0` | 120 | UnwindData |  |
| 3701 | `strlcpy` | `0x102F20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3702 | `strndup` | `0x102F70` | 80 | UnwindData |  |
| 3703 | `strsep` | `0x102FC0` | 25 | UnwindData |  |
| 3704 | `strtonum` | `0x103030` | 312 | UnwindData |  |
| 3705 | `timegm` | `0x103600` | 108 | UnwindData |  |
| 3413 | `explicit_bzero` | `0x103670` | 21 | UnwindData |  |
| 3215 | `arc4random` | `0x103B00` | 287 | UnwindData |  |
| 3216 | `arc4random_buf` | `0x103C20` | 146 | UnwindData |  |
| 3217 | `arc4random_uniform` | `0x104720` | 74 | UnwindData |  |
| 3415 | `getentropy` | `0x104770` | 64 | UnwindData |  |
| 3706 | `timingsafe_bcmp` | `0x1047B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3707 | `timingsafe_memcmp` | `0x1047F0` | 124 | UnwindData |  |
| 30 | `ASN1_BIT_STRING_it` | `0x1339D8` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `ASN1_ENUMERATED_it` | `0x133AC8` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `ASN1_INTEGER_it` | `0x133BD8` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `ASN1_OBJECT_it` | `0x133DD8` | 296 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `ASN1_OCTET_STRING_it` | `0x133F00` | 1,512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `ASN1_TIME_it` | `0x1344E8` | 8,776 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1915 | `PBEPARAM_it` | `0x136730` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1912 | `PBE2PARAM_it` | `0x136870` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1918 | `PBKDF2PARAM_it` | `0x1368A0` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2190 | `PKCS8_PRIV_KEY_INFO_it` | `0x136AA0` | 3,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `ASN1_SEQUENCE_ANY_it` | `0x137790` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `ASN1_SET_ANY_it` | `0x1377C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `ASN1_ANY_it` | `0x1377F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `ASN1_VISIBLESTRING_it` | `0x137820` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 160 | `ASN1_UNIVERSALSTRING_it` | `0x137850` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `ASN1_UTF8STRING_it` | `0x137880` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 72 | `ASN1_NULL_it` | `0x1378B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `ASN1_BMPSTRING_it` | `0x1378E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `ASN1_PRINTABLE_it` | `0x137910` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 870 | `DIRECTORYSTRING_it` | `0x137940` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 873 | `DISPLAYTEXT_it` | `0x137970` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `ASN1_PRINTABLESTRING_it` | `0x1379A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 131 | `ASN1_T61STRING_it` | `0x1379D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 57 | `ASN1_IA5STRING_it` | `0x137A00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 54 | `ASN1_GENERALSTRING_it` | `0x137A30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `ASN1_UTCTIME_it` | `0x137A60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `ASN1_GENERALIZEDTIME_it` | `0x137A90` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `ASN1_SEQUENCE_it` | `0x137B80` | 720 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2690 | `X509_ALGOR_it` | `0x137E50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2685 | `X509_ALGORS_it` | `0x137E80` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2704 | `X509_ATTRIBUTE_it` | `0x137F60` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `BIGNUM_it` | `0x137FF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 497 | `CBIGNUM_it` | `0x138020` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2917 | `X509_REVOKED_it` | `0x138060` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2716 | `X509_CRL_INFO_it` | `0x138090` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2748 | `X509_CRL_it` | `0x1380C0` | 912 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2774 | `X509_EXTENSION_it` | `0x138450` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2766 | `X509_EXTENSIONS_it` | `0x138480` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1677 | `LONG_it` | `0x138610` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3199 | `ZLONG_it` | `0x138640` | 256 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2801 | `X509_NAME_ENTRY_it` | `0x138740` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2825 | `X509_NAME_it` | `0x138770` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2793 | `X509_NAME_ENTRIES_it` | `0x138800` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2806 | `X509_NAME_INTERNAL_it` | `0x138850` | 560 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2847 | `X509_PUBKEY_it` | `0x138A80` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2863 | `X509_REQ_INFO_it` | `0x138DB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2890 | `X509_REQ_it` | `0x138DE0` | 432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2924 | `X509_SIG_it` | `0x138F90` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1712 | `NETSCAPE_SPKI_it` | `0x139020` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1706 | `NETSCAPE_SPKAC_it` | `0x139050` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3010 | `X509_VAL_it` | `0x139170` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2713 | `X509_CINF_it` | `0x139210` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3115 | `X509_it` | `0x139240` | 656 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2709 | `X509_CERT_AUX_it` | `0x1394D0` | 30,112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 511 | `CMS_ContentInfo_it` | `0x140A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 521 | `CMS_ReceiptRequest_it` | `0x140AA0` | 53,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 866 | `DHparams_it` | `0x14DCD0` | 3,456 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 883 | `DSAPublicKey_it` | `0x14EA50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 882 | `DSAPrivateKey_it` | `0x14EA80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 935 | `DSAparams_it` | `0x14EAB0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 887 | `DSA_SIG_it` | `0x14EB50` | 2,864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3197 | `X9_62_PENTANOMIAL_it` | `0x14F680` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3192 | `X9_62_CHARACTERISTIC_TWO_it` | `0x14F7D0` | 272 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3195 | `X9_62_FIELDID_it` | `0x14F8E0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3194 | `X9_62_CURVE_it` | `0x14F970` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 953 | `ECPARAMETERS_it` | `0x14FA60` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 956 | `ECPKPARAMETERS_it` | `0x14FAF0` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1077 | `EC_PRIVATEKEY_it` | `0x14FBA0` | 23,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 944 | `ECDSA_SIG_it` | `0x155620` | 25,936 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1628 | `GOST_CIPHER_PARAMS_it` | `0x15BB70` | 113,904 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1810 | `OCSP_RESPID_it` | `0x177860` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1836 | `OCSP_SINGLERESP_it` | `0x177890` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1767 | `OCSP_CERTSTATUS_it` | `0x1778C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1817 | `OCSP_REVOKEDINFO_it` | `0x1778F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1760 | `OCSP_BASICRESP_it` | `0x177920` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1807 | `OCSP_RESPDATA_it` | `0x177950` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1813 | `OCSP_RESPONSE_it` | `0x177980` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1804 | `OCSP_RESPBYTES_it` | `0x1779B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1782 | `OCSP_ONEREQ_it` | `0x1779E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1764 | `OCSP_CERTID_it` | `0x177A10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1797 | `OCSP_REQUEST_it` | `0x177A40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1823 | `OCSP_SIGNATURE_it` | `0x177A70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1785 | `OCSP_REQINFO_it` | `0x177AA0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1770 | `OCSP_CRLID_it` | `0x177AD0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1820 | `OCSP_SERVICELOC_it` | `0x177B00` | 7,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2075 | `PKCS12_it` | `0x179A30` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2036 | `PKCS12_MAC_DATA_it` | `0x179A60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2057 | `PKCS12_SAFEBAG_it` | `0x179A90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2033 | `PKCS12_BAGS_it` | `0x179AC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2040 | `PKCS12_SAFEBAGS_it` | `0x179AF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2031 | `PKCS12_AUTHSAFES_it` | `0x179B20` | 5,392 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2122 | `PKCS7_ISSUER_AND_SERIAL_it` | `0x17B030` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2134 | `PKCS7_SIGNER_INFO_it` | `0x17B060` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2126 | `PKCS7_RECIP_INFO_it` | `0x17B090` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2130 | `PKCS7_SIGNED_it` | `0x17B0C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2115 | `PKCS7_ENC_CONTENT_it` | `0x17B0F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2118 | `PKCS7_ENVELOPE_it` | `0x17B120` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2139 | `PKCS7_SIGN_ENVELOPE_it` | `0x17B150` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2109 | `PKCS7_DIGEST_it` | `0x17B180` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2112 | `PKCS7_ENCRYPT_it` | `0x17B1B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2172 | `PKCS7_it` | `0x17B1E0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2106 | `PKCS7_ATTR_SIGN_it` | `0x17B210` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2107 | `PKCS7_ATTR_VERIFY_it` | `0x17B240` | 4,992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2246 | `RSAPublicKey_it` | `0x17C5C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2244 | `RSAPrivateKey_it` | `0x17C5F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2253 | `RSA_PSS_PARAMS_it` | `0x17C620` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2248 | `RSA_OAEP_PARAMS_it` | `0x17C650` | 6,880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2455 | `TS_MSG_IMPRINT_it` | `0x17E130` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2478 | `TS_REQ_it` | `0x17E220` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2429 | `TS_ACCURACY_it` | `0x17E2B0` | 368 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2550 | `TS_TST_INFO_it` | `0x17E420` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2525 | `TS_STATUS_INFO_it` | `0x17E4B0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2512 | `TS_RESP_it` | `0x17E550` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1170 | `ESS_ISSUER_SERIAL_it` | `0x17E5C0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1166 | `ESS_CERT_ID_it` | `0x17E630` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1174 | `ESS_SIGNING_CERT_it` | `0x17E6A0` | 5,920 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1672 | `IPAddressRange_it` | `0x17FDC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1669 | `IPAddressOrRange_it` | `0x17FDF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1663 | `IPAddressChoice_it` | `0x17FE20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1666 | `IPAddressFamily_it` | `0x17FE50` | 1,568 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 226 | `AUTHORITY_KEYID_it` | `0x180470` | 1,120 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `ASRange_it` | `0x1808D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `ASIdOrRange_it` | `0x180900` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `ASIdentifierChoice_it` | `0x180930` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `ASIdentifiers_it` | `0x180960` | 1,328 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `BASIC_CONSTRAINTS_it` | `0x180E90` | 2,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 499 | `CERTIFICATEPOLICIES_it` | `0x181740` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2204 | `POLICYINFO_it` | `0x181770` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2207 | `POLICYQUALINFO_it` | `0x1817A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2633 | `USERNOTICE_it` | `0x1817D0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1719 | `NOTICEREF_it` | `0x181800` | 1,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 653 | `CRL_DIST_POINTS_it` | `0x181CE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 879 | `DIST_POINT_it` | `0x181D10` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 876 | `DIST_POINT_NAME_it` | `0x181D40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1675 | `ISSUING_DIST_POINT_it` | `0x181D70` | 4,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1597 | `EXTENDED_KEY_USAGE_it` | `0x182D50` | 512 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1609 | `GENERAL_NAME_it` | `0x182F50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1602 | `GENERAL_NAMES_it` | `0x182F80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1904 | `OTHERNAME_it` | `0x182FB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1086 | `EDIPARTYNAME_it` | `0x182FE0` | 1,808 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `ACCESS_DESCRIPTION_it` | `0x1836F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `AUTHORITY_INFO_ACCESS_it` | `0x183720` | 1,360 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1615 | `GENERAL_SUBTREE_it` | `0x183C70` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1690 | `NAME_CONSTRAINTS_it` | `0x183CA0` | 1,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2210 | `POLICY_CONSTRAINTS_it` | `0x184460` | 544 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2201 | `PKEY_USAGE_PERIOD_it` | `0x184680` | 288 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2214 | `POLICY_MAPPING_it` | `0x1847A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2212 | `POLICY_MAPPINGS_it` | `0x1847D0` | 230,624 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 822 | `DES_rw_mode` | `0x1BCCB0` | 14,268 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3661 | `optind` | `0x1C046C` | 3,604 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 797 | `DES_check_key` | `0x1C1280` | 13,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3660 | `optarg` | `0x1C46A0` | 0 | Indeterminate |  |

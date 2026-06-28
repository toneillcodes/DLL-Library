# Binary Specification: uwfcfgmgmt.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\uwfcfgmgmt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `76377725e2593a1d8d10135143418a5b3557ca8bd635b5745628cf7a3fe8c153`
* **Total Exported Functions:** 297

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `??0CUwfOverlayDevice@@QEAA@XZ` | `0x34E0` | 74 | UnwindData |  |
| 99 | `?IsCurrentSession@CUwfStaticConfiguration@@QEAA_NXZ` | `0x47A0` | 5,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0CUwfConfiguration@@QEAA@XZ` | `0x5D40` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0CUwfStaticConfiguration@@QEAA@XZ` | `0x5DB0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0CUwfStaticVolumeConfiguration@@QEAA@XZ` | `0x5DE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??1CUwfConfiguration@@UEAA@XZ` | `0x5E10` | 65 | UnwindData |  |
| 15 | `??1CUwfStaticConfiguration@@UEAA@XZ` | `0x5E60` | 55 | UnwindData |  |
| 16 | `??1CUwfStaticVolumeConfiguration@@UEAA@XZ` | `0x5EA0` | 41 | UnwindData |  |
| 19 | `?AddFileExclusion@CUwfStaticVolumeConfiguration@@QEAAJPEBG@Z` | `0x60D0` | 657 | UnwindData |  |
| 21 | `?AddRegKeyExclusion@CUwfStaticConfiguration@@QEAAJPEBG@Z` | `0x6370` | 596 | UnwindData |  |
| 29 | `?Close@CUwfConfiguration@@QEAAXXZ` | `0x6680` | 50 | UnwindData |  |
| 32 | `?Close@CUwfStaticConfiguration@@QEAAXXZ` | `0x66C0` | 52 | UnwindData |  |
| 33 | `?Close@CUwfStaticVolumeConfiguration@@QEAAXXZ` | `0x6700` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `?Compare@CUwfStaticVolumeConfiguration@@QEAAJAEAV1@PEA_N@Z` | `0x6710` | 102 | UnwindData |  |
| 43 | `?CopyTo@CUwfStaticConfiguration@@QEAAJPEAUHKEY__@@PEBG_N@Z` | `0x6F40` | 142 | UnwindData |  |
| 44 | `?CopyTree@CUwfConfiguration@@QEAAJAEAVCUwfRegKey@@PEBGPEAUHKEY__@@_N@Z` | `0x6FE0` | 50 | UnwindData |  |
| 49 | `?CreateKey@CUwfConfiguration@@QEAAJPEAUHKEY__@@PEBGKKPEAKAEAVCUwfRegKey@@@Z` | `0x7020` | 120 | UnwindData |  |
| 50 | `?CreateOverlayFile@CUwfStaticConfiguration@@QEAAJK@Z` | `0x70A0` | 200 | UnwindData |  |
| 53 | `?CreateVolume@CUwfStaticConfiguration@@QEAAJPEBG0PEAPEAVCUwfStaticVolumeConfiguration@@@Z` | `0x7170` | 1,217 | UnwindData |  |
| 54 | `?DeleteBindingConfiguration@CUwfStaticVolumeConfiguration@@QEAAJXZ` | `0x7640` | 81 | UnwindData |  |
| 55 | `?DeleteFileW@CUwfConfiguration@@QEAAJPEBG@Z` | `0x76A0` | 92 | UnwindData |  |
| 56 | `?DeleteOverlayFile@CUwfStaticConfiguration@@QEAAJXZ` | `0x7780` | 93 | UnwindData |  |
| 57 | `?DeleteTree@CUwfConfiguration@@QEAAJAEAVCUwfRegKey@@PEBG@Z` | `0x78B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `?DeleteTreeFromRoot@CUwfConfiguration@@QEAAJAEAVCUwfRegKey@@PEBG@Z` | `0x78E0` | 165 | UnwindData |  |
| 62 | `?DeleteVolume@CUwfStaticConfiguration@@QEAAJK@Z` | `0x7990` | 455 | UnwindData |  |
| 69 | `?FindFileExclusion@CUwfStaticVolumeConfiguration@@QEAAJPEBG@Z` | `0x7CA0` | 364 | UnwindData |  |
| 70 | `?FindRegKeyExclusion@CUwfStaticConfiguration@@QEAAJPEBG@Z` | `0x7E20` | 364 | UnwindData |  |
| 72 | `?FixupUpdatedSettings@CUwfConfiguration@@QEAAJXZ` | `0x7FA0` | 314 | UnwindData |  |
| 76 | `?GetOverlayFileName@CUwfStaticConfiguration@@QEAAJPEAPEAG@Z` | `0x80E0` | 944 | UnwindData |  |
| 88 | `?HaveUwfFactorySettings@CUwfConfiguration@@QEAAJPEA_N@Z` | `0x8820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `?Initialize@CUwfConfiguration@@QEAAJPEAX@Z` | `0x8830` | 396 | UnwindData |  |
| 96 | `?Initialize@CUwfStaticVolumeConfiguration@@QEAAJPEAUHKEY__@@K_NPEAVCUwfConfiguration@@PEAVCUwfStaticConfiguration@@@Z` | `0x89D0` | 282 | UnwindData |  |
| 100 | `?IsFileExcluded@CUwfStaticVolumeConfiguration@@QEAAJPEBGPEA_N@Z` | `0x8AF0` | 276 | UnwindData |  |
| 101 | `?IsHORMEnabled@CUwfConfiguration@@QEAA_NXZ` | `0x8C10` | 122 | UnwindData |  |
| 102 | `?IsOverlayFileExist@CUwfStaticConfiguration@@QEAAJPEA_N@Z` | `0x8C90` | 198 | UnwindData |  |
| 110 | `?Open@CUwfStaticConfiguration@@QEAAJ_NK0PEAVCUwfConfiguration@@@Z` | `0x8E40` | 463 | UnwindData |  |
| 111 | `?OpenKey@CUwfConfiguration@@QEAAJPEAUHKEY__@@PEBGKAEAVCUwfRegKey@@@Z` | `0x9020` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `?ReOpen@CUwfStaticConfiguration@@QEAAJK@Z` | `0x9350` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `?ReOpen@CUwfStaticVolumeConfiguration@@QEAAJPEAUHKEY__@@@Z` | `0x9380` | 172 | UnwindData |  |
| 125 | `?ReleaseStaticVolumeConfiguration@CUwfStaticConfiguration@@QEAAXXZ` | `0x9440` | 46 | UnwindData |  |
| 126 | `?RemoveAllFileExclusions@CUwfStaticVolumeConfiguration@@QEAAJXZ` | `0x9480` | 97 | UnwindData |  |
| 127 | `?RemoveFileExclusion@CUwfStaticVolumeConfiguration@@QEAAJPEBG@Z` | `0x94F0` | 477 | UnwindData |  |
| 128 | `?RemoveRegKeyExclusion@CUwfStaticConfiguration@@QEAAJPEBG@Z` | `0x96E0` | 452 | UnwindData |  |
| 129 | `?ResetBindingConfiguration@CUwfStaticVolumeConfiguration@@QEAAJXZ` | `0x98B0` | 98 | UnwindData |  |
| 130 | `?ResetFileExclusions@CUwfStaticVolumeConfiguration@@QEAAJXZ` | `0x9920` | 151 | UnwindData |  |
| 131 | `?ResetUwfSettings@CUwfConfiguration@@QEAAJXZ` | `0x99C0` | 167 | UnwindData |  |
| 138 | `?SetOverlayFileSize@CUwfStaticConfiguration@@QEAAJK@Z` | `0xA0D0` | 371 | UnwindData |  |
| 144 | `?UpdateDWORDValue@CUwfConfiguration@@QEAAJAEAVCUwfRegKey@@PEBGK_N@Z` | `0xA980` | 241 | UnwindData |  |
| 145 | `?UpdateMultiSzValue@CUwfConfiguration@@QEAAJAEAVCUwfRegKey@@PEBGQEAU_MULTISZ@@_N@Z` | `0xAA80` | 411 | UnwindData |  |
| 146 | `?UpdateQWORDValue@CUwfConfiguration@@QEAAJAEAVCUwfRegKey@@PEBG_K_N@Z` | `0xAEA0` | 242 | UnwindData |  |
| 147 | `?UpdateSzValue@CUwfConfiguration@@QEAAJAEAVCUwfRegKey@@PEBG1_N@Z` | `0xAFA0` | 348 | UnwindData |  |
| 206 | `?get_BindingType@CUwfStaticVolumeConfiguration@@QEAAJPEAK@Z` | `0xB3B0` | 45 | UnwindData |  |
| 207 | `?get_DiskNumber@CUwfStaticVolumeConfiguration@@QEAAJPEAK@Z` | `0xB3F0` | 45 | UnwindData |  |
| 208 | `?get_DiskSignature@CUwfStaticVolumeConfiguration@@QEAAJPEAK@Z` | `0xB430` | 45 | UnwindData |  |
| 209 | `?get_DriveLetter@CUwfStaticVolumeConfiguration@@QEAAJPEAPEAG@Z` | `0xB470` | 45 | UnwindData |  |
| 210 | `?get_FileExclusions@CUwfStaticVolumeConfiguration@@QEAAJPEAPEAU_MULTISZ@@@Z` | `0xB4B0` | 45 | UnwindData |  |
| 211 | `?get_HORMEnabled@CUwfConfiguration@@QEAAJPEA_N@Z` | `0xB4F0` | 170 | UnwindData |  |
| 213 | `?get_IsNoFileExclusion@CUwfStaticConfiguration@@QEAAJPEA_N@Z` | `0xB5A0` | 393 | UnwindData |  |
| 214 | `?get_IsNoRegExclusion@CUwfStaticConfiguration@@QEAAJPEA_N@Z` | `0xB730` | 86 | UnwindData |  |
| 215 | `?get_NumVolumes@CUwfStaticConfiguration@@QEAAJPEAK@Z` | `0xB790` | 45 | UnwindData |  |
| 216 | `?get_OverlayCriticalThreshold@CUwfConfiguration@@QEAAJPEAK@Z` | `0xB7D0` | 45 | UnwindData |  |
| 219 | `?get_OverlayFlags@CUwfStaticConfiguration@@QEAAJPEAK@Z` | `0xB810` | 166 | UnwindData |  |
| 222 | `?get_OverlayMaximumSize@CUwfStaticConfiguration@@QEAAJPEAK@Z` | `0xB8C0` | 45 | UnwindData |  |
| 224 | `?get_OverlayType@CUwfStaticConfiguration@@QEAAJPEAW4_UWF_CONFIG_OVERLAY_TYPE@@@Z` | `0xB900` | 189 | UnwindData |  |
| 225 | `?get_OverlayWarningThreshold@CUwfConfiguration@@QEAAJPEAK@Z` | `0xB9D0` | 45 | UnwindData |  |
| 227 | `?get_PartitionGUID@CUwfStaticVolumeConfiguration@@QEAAJPEAPEAG@Z` | `0xBA10` | 45 | UnwindData |  |
| 228 | `?get_PartitionNumber@CUwfStaticVolumeConfiguration@@QEAAJPEAK@Z` | `0xBA50` | 45 | UnwindData |  |
| 229 | `?get_PartitionOffset@CUwfStaticVolumeConfiguration@@QEAAJPEA_K@Z` | `0xBA90` | 45 | UnwindData |  |
| 230 | `?get_PartitionStyle@CUwfStaticVolumeConfiguration@@QEAAJPEAW4_PARTITION_STYLE@@@Z` | `0xBAD0` | 166 | UnwindData |  |
| 231 | `?get_PersistDomainSecretKey@CUwfStaticConfiguration@@QEAAJPEA_N@Z` | `0xBB80` | 170 | UnwindData |  |
| 232 | `?get_PersistTSCAL@CUwfStaticConfiguration@@QEAAJPEA_N@Z` | `0xBC30` | 170 | UnwindData |  |
| 233 | `?get_Protected@CUwfStaticVolumeConfiguration@@QEAAJPEA_N@Z` | `0xBCE0` | 170 | UnwindData |  |
| 234 | `?get_RegKeyExclusions@CUwfStaticConfiguration@@QEAAJPEAPEAU_MULTISZ@@@Z` | `0xBD90` | 45 | UnwindData |  |
| 235 | `?get_RegKeyExclusionsUWFSpecific@CUwfStaticConfiguration@@QEAAJPEAPEAU_MULTISZ@@@Z` | `0xBDD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `?get_ResetPersistentStateSavedMode@CUwfStaticConfiguration@@QEAAJPEAK@Z` | `0xBDF0` | 166 | UnwindData |  |
| 241 | `?get_ServicingModeEnabled@CUwfStaticConfiguration@@QEAAJPEA_N@Z` | `0xBEA0` | 158 | UnwindData |  |
| 242 | `?get_StaticConfiguration@CUwfConfiguration@@QEAAJ_NPEAPEAVCUwfStaticConfiguration@@@Z` | `0xBF50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `?get_StaticVolumeConfiguration@CUwfStaticConfiguration@@QEAAJKPEAPEAVCUwfStaticVolumeConfiguration@@@Z` | `0xBF80` | 216 | UnwindData |  |
| 244 | `?get_StaticVolumeConfiguration@CUwfStaticConfiguration@@QEAAJPEBG0PEAPEAVCUwfStaticVolumeConfiguration@@@Z` | `0xC060` | 672 | UnwindData |  |
| 245 | `?get_StaticVolumeConfiguration@CUwfStaticConfiguration@@QEAAJPEBGPEAPEAVCUwfStaticVolumeConfiguration@@@Z` | `0xC310` | 517 | UnwindData |  |
| 246 | `?get_SwapfileSize@CUwfStaticVolumeConfiguration@@QEAAJPEAK@Z` | `0xC520` | 62 | UnwindData |  |
| 248 | `?get_UwfEnabled@CUwfStaticConfiguration@@QEAAJPEA_N@Z` | `0xC570` | 170 | UnwindData |  |
| 249 | `?get_UwfEnabledBeforeServicing@CUwfConfiguration@@QEAAJPEAK@Z` | `0xC620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `?get_VolumeGuid@CUwfStaticVolumeConfiguration@@QEAAJPEAPEAG@Z` | `0xC640` | 45 | UnwindData |  |
| 251 | `?set_BindingType@CUwfStaticVolumeConfiguration@@QEAAJK@Z` | `0xC680` | 356 | UnwindData |  |
| 252 | `?set_DiskNumber@CUwfStaticVolumeConfiguration@@QEAAJK@Z` | `0xC920` | 74 | UnwindData |  |
| 253 | `?set_DiskSignature@CUwfStaticVolumeConfiguration@@QEAAJK@Z` | `0xC970` | 74 | UnwindData |  |
| 254 | `?set_DriveLetter@CUwfStaticVolumeConfiguration@@QEAAJPEBG@Z` | `0xC9C0` | 124 | UnwindData |  |
| 255 | `?set_HORMEnabled@CUwfConfiguration@@QEAAJ_N0@Z` | `0xCA50` | 203 | UnwindData |  |
| 258 | `?set_NumVolumes@CUwfStaticConfiguration@@QEAAJK@Z` | `0xCB30` | 74 | UnwindData |  |
| 259 | `?set_OverlayCriticalThreshold@CUwfConfiguration@@QEAAJK@Z` | `0xCB80` | 74 | UnwindData |  |
| 263 | `?set_OverlayFlags@CUwfStaticConfiguration@@QEAAJK@Z` | `0xCBD0` | 105 | UnwindData |  |
| 265 | `?set_OverlayMaximumSize@CUwfStaticConfiguration@@QEAAJK@Z` | `0xCC40` | 264 | UnwindData |  |
| 267 | `?set_OverlayType@CUwfStaticConfiguration@@QEAAJW4_UWF_CONFIG_OVERLAY_TYPE@@@Z` | `0xCD50` | 483 | UnwindData |  |
| 268 | `?set_OverlayWarningThreshold@CUwfConfiguration@@QEAAJK@Z` | `0xCF40` | 74 | UnwindData |  |
| 271 | `?set_PartitionGUID@CUwfStaticVolumeConfiguration@@QEAAJPEBG@Z` | `0xCF90` | 74 | UnwindData |  |
| 272 | `?set_PartitionNumber@CUwfStaticVolumeConfiguration@@QEAAJK@Z` | `0xCFE0` | 74 | UnwindData |  |
| 273 | `?set_PartitionOffset@CUwfStaticVolumeConfiguration@@QEAAJ_K@Z` | `0xD030` | 74 | UnwindData |  |
| 274 | `?set_PartitionStyle@CUwfStaticVolumeConfiguration@@QEAAJW4_PARTITION_STYLE@@@Z` | `0xD080` | 74 | UnwindData |  |
| 275 | `?set_PersistDomainSecretKey@CUwfStaticConfiguration@@QEAAJ_N@Z` | `0xD0D0` | 750 | UnwindData |  |
| 276 | `?set_PersistTSCAL@CUwfStaticConfiguration@@QEAAJ_N@Z` | `0xD3D0` | 750 | UnwindData |  |
| 277 | `?set_Protected@CUwfStaticVolumeConfiguration@@QEAAJ_N@Z` | `0xD6D0` | 236 | UnwindData |  |
| 278 | `?set_RegKeyExclusionsUWFSpecific@CUwfStaticConfiguration@@QEAAJPEAU_MULTISZ@@@Z` | `0xD7D0` | 48 | UnwindData |  |
| 281 | `?set_ResetPersistentStateSavedMode@CUwfStaticConfiguration@@QEAAJK@Z` | `0xD810` | 102 | UnwindData |  |
| 285 | `?set_ServicingModeEnabled@CUwfStaticConfiguration@@QEAAJ_N@Z` | `0xD880` | 275 | UnwindData |  |
| 286 | `?set_SwapfileSize@CUwfStaticVolumeConfiguration@@QEAAJK@Z` | `0xD9A0` | 74 | UnwindData |  |
| 287 | `?set_UwfBootPersistenceEnabled@CUwfConfiguration@@QEAAJ_N@Z` | `0xD9F0` | 296 | UnwindData |  |
| 288 | `?set_UwfEnabled@CUwfStaticConfiguration@@QEAAJ_N@Z` | `0xDB20` | 156 | UnwindData |  |
| 289 | `?set_UwfEnabledBeforeServicing@CUwfConfiguration@@QEAAJK@Z` | `0xDBD0` | 74 | UnwindData |  |
| 290 | `?set_VolumeGuid@CUwfStaticVolumeConfiguration@@QEAAJPEBG@Z` | `0xDC20` | 86 | UnwindData |  |
| 6 | `??0CUwfRegKey@@QEAA@XZ` | `0xDE70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??1CUwfRegKey@@QEAA@XZ` | `0xDE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `?AddDWORDValue@CUwfRegKey@@QEAAJPEBGK@Z` | `0xDE90` | 187 | UnwindData |  |
| 20 | `?AddMultiSzValue@CUwfRegKey@@QEAAJPEBG0@Z` | `0xDF60` | 412 | UnwindData |  |
| 22 | `?Attach@CUwfRegKey@@QEAAJPEAUHKEY__@@@Z` | `0xE110` | 62 | UnwindData |  |
| 31 | `?Close@CUwfRegKey@@QEAAJXZ` | `0xE160` | 42 | UnwindData |  |
| 45 | `?CopyTree@CUwfRegKey@@QEAAJAEAV1@PEBG_N@Z` | `0xE190` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `?CopyTree@CUwfRegKey@@QEAAJPEAUHKEY__@@PEBG_N@Z` | `0xE1A0` | 119 | UnwindData |  |
| 47 | `?CopyTreeTransacted@CUwfRegKey@@QEAAJPEBGPEAUHKEY__@@PEAX_N@Z` | `0xE220` | 470 | UnwindData |  |
| 48 | `?Create@CUwfRegKey@@QEAAJPEAUHKEY__@@PEBGPEAGKKPEAU_SECURITY_ATTRIBUTES@@PEAK@Z` | `0xE590` | 175 | UnwindData |  |
| 51 | `?CreateSubKey@CUwfRegKey@@QEAAJPEBGKKPEAKPEAV1@@Z` | `0xE650` | 228 | UnwindData |  |
| 52 | `?CreateTransacted@CUwfRegKey@@QEAAJPEAUHKEY__@@PEBGPEAGKKPEAU_SECURITY_ATTRIBUTES@@PEAKPEAX@Z` | `0xE740` | 193 | UnwindData |  |
| 58 | `?DeleteTree@CUwfRegKey@@QEAAJPEBG@Z` | `0xE810` | 63 | UnwindData |  |
| 60 | `?DeleteTreeTransacted@CUwfRegKey@@QEAAJPEBGPEAX@Z` | `0xE860` | 305 | UnwindData |  |
| 61 | `?DeleteValue@CUwfRegKey@@QEAAJPEBG@Z` | `0xE9A0` | 51 | UnwindData |  |
| 63 | `?Detach@CUwfRegKey@@QEAAPEAUHKEY__@@XZ` | `0xE9E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `?GetSubKeyAt@CUwfRegKey@@QEAAJKPEAGK@Z` | `0xE9F0` | 77 | UnwindData |  |
| 109 | `?Open@CUwfRegKey@@QEAAJPEAUHKEY__@@PEBGK@Z` | `0xEA50` | 127 | UnwindData |  |
| 112 | `?OpenSubKey@CUwfRegKey@@QEAAJPEBGKAEAV1@@Z` | `0xEAE0` | 82 | UnwindData |  |
| 113 | `?OpenSubKeyAt@CUwfRegKey@@QEAAJKKAEAV1@@Z` | `0xEB40` | 105 | UnwindData |  |
| 114 | `?OpenTransacted@CUwfRegKey@@QEAAJPEAUHKEY__@@PEBGKPEAX@Z` | `0xEBB0` | 142 | UnwindData |  |
| 117 | `?QueryBinaryValue@CUwfRegKey@@QEAAJPEBGPEAPEAEPEAK@Z` | `0xEC50` | 286 | UnwindData |  |
| 118 | `?QueryDWORDValue@CUwfRegKey@@QEAAJPEBGPEAK@Z` | `0xED80` | 118 | UnwindData |  |
| 119 | `?QueryMultiSzValue@CUwfRegKey@@QEAAJPEBGPEAPEAU_MULTISZ@@@Z` | `0xEE00` | 325 | UnwindData |  |
| 120 | `?QueryQWORDValue@CUwfRegKey@@QEAAJPEBGPEA_K@Z` | `0xEF50` | 118 | UnwindData |  |
| 121 | `?QuerySzValue@CUwfRegKey@@QEAAJPEBGPEAPEAG@Z` | `0xEFD0` | 273 | UnwindData |  |
| 134 | `?SetBinaryValue@CUwfRegKey@@QEAAJPEBGPEAEK@Z` | `0xF0F0` | 68 | UnwindData |  |
| 136 | `?SetDWORDValue@CUwfRegKey@@QEAAJPEBGK@Z` | `0xF140` | 76 | UnwindData |  |
| 137 | `?SetMultiSzValue@CUwfRegKey@@QEAAJPEBGQEAU_MULTISZ@@@Z` | `0xF1A0` | 93 | UnwindData |  |
| 139 | `?SetQWORDValue@CUwfRegKey@@QEAAJPEBG_K@Z` | `0xF210` | 80 | UnwindData |  |
| 141 | `?SetSzValue@CUwfRegKey@@QEAAJPEBG0@Z` | `0xF270` | 102 | UnwindData |  |
| 26 | `?CanVolumeBeProtected@@YAJPEBG_NPEA_N@Z` | `0xF310` | 231 | UnwindData |  |
| 27 | `?CaptureUwfSettings@@YAJW4E_UNATTEND_REASON@@@Z` | `0xF400` | 246 | UnwindData |  |
| 64 | `?DisableAutoDefragService@@YAJH@Z` | `0xFC30` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `?DisableService@@YAJPEBG_N@Z` | `0xFD60` | 314 | UnwindData |  |
| 71 | `?FixupLowerFiltersSetting@@YAJXZ` | `0x10370` | 795 | UnwindData |  |
| 78 | `?GetServiceStartType@@YAJPEBGPEAK@Z` | `0x108C0` | 360 | UnwindData |  |
| 83 | `?GetUwfProtectableVolumeList@@YAJ_NPEAKPEAUUWF_PROTECTABLEVOLUME_INFO@@@Z` | `0x10BA0` | 709 | UnwindData |  |
| 86 | `?GetWinResumeObjectId@@YAJPEAPEAG@Z` | `0x10E70` | 101 | UnwindData |  |
| 87 | `?HaveCapturedUwfSettings@@YAJPEA_N@Z` | `0x10EE0` | 199 | UnwindData |  |
| 103 | `?IsUserAdmin@@YAJPEA_N@Z` | `0x114D0` | 34 | UnwindData |  |
| 124 | `?RegReadValue@@YAJPEAUHKEY__@@PEBGKPEAPEAEPEAK@Z` | `0x11F30` | 250 | UnwindData |  |
| 135 | `?SetBootStatusPolicy@@YAJPEBG@Z` | `0x12030` | 122 | UnwindData |  |
| 140 | `?SetServiceStartType@@YAJPEBGK@Z` | `0x120B0` | 304 | UnwindData |  |
| 204 | `?VolumeGetConfig@@YAJPEAVCUwfStaticConfiguration@@PEBG1PEAPEAVCUwfStaticVolumeConfiguration@@@Z` | `0x121F0` | 873 | UnwindData |  |
| 205 | `?VolumeGetVolumeGuid@@YAJPEBGPEAGK@Z` | `0x12970` | 150 | UnwindData |  |
| 291 | `MultiSzAdd` | `0x12AD0` | 112 | UnwindData |  |
| 292 | `MultiSzAlloc` | `0x12B50` | 265 | UnwindData |  |
| 293 | `MultiSzCompare` | `0x12C60` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `MultiSzFind` | `0x12CD0` | 180 | UnwindData |  |
| 295 | `MultiSzFree` | `0x12D90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `MultiSzReAlloc` | `0x12DB0` | 254 | UnwindData |  |
| 297 | `MultiSzRemove` | `0x12EC0` | 253 | UnwindData |  |
| 25 | `?CanFileBeCommitted@@YA_NPEBG0@Z` | `0x12FD0` | 236 | UnwindData |  |
| 66 | `?ExecuteBackgroundProcess@@YAJPEBG0_NPEAK@Z` | `0x130D0` | 428 | UnwindData |  |
| 74 | `?GetDriveLetterFromVolumeName@@YAJPEBGPEAG@Z` | `0x13360` | 444 | UnwindData |  |
| 81 | `?GetSystemDriveLetter@@YAJPEAPEAG@Z` | `0x13530` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `?GetVolumeGuidFromDriveName@@YAJPEBGPEAGK@Z` | `0x13550` | 310 | UnwindData |  |
| 89 | `?HiberFileExists@@YA_NXZ` | `0x13690` | 168 | UnwindData |  |
| 104 | `?IsValidDriveLetter@@YA_NPEBG@Z` | `0x13920` | 91 | UnwindData |  |
| 105 | `?IsValidOverlayConfig@@YA_NW4_UWF_CONFIG_OVERLAY_TYPE@@K@Z` | `0x13990` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `?IsValidVolumeName@@YA_NPEBG@Z` | `0x139D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `?ParsePathSpec@@YAJPEBGPEAGK1K1K@Z` | `0x139E0` | 607 | UnwindData |  |
| 116 | `?ParseVolumeGUID@@YAJPEBGPEAGK@Z` | `0x13D10` | 298 | UnwindData |  |
| 202 | `?ValidateFileNameToBeCommitted@@YA?AW4FILE_COMMIT_VALIDATE_RESULT@@_NPEBG11@Z` | `0x13E40` | 348 | UnwindData |  |
| 203 | `?ValidateRegistryKeyValueToBeCommitted@@YA?AW4REG_COMMIT_VALIDATE_RESULT@@_N0PEBG1KPEAPEAG@Z` | `0x13FB0` | 448 | UnwindData |  |
| 1 | `??0CDevice@@QEAA@XZ` | `0x14290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0CUwfVolumeDevice@@QEAA@XZ` | `0x14290` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0CUwfRegDevice@@QEAA@XZ` | `0x142B0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??1CDevice@@UEAA@XZ` | `0x142E0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??1CUwfRegDevice@@UEAA@XZ` | `0x142E0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??1CUwfVolumeDevice@@UEAA@XZ` | `0x142E0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `?Close@CDevice@@QEAAXXZ` | `0x14630` | 43 | UnwindData |  |
| 38 | `?CommitRegistryKey@CUwfRegDevice@@QEAAJPEBG@Z` | `0x14670` | 216 | UnwindData |  |
| 39 | `?CommitRegistryKeyDeletion@CUwfRegDevice@@QEAAJPEBG@Z` | `0x14750` | 216 | UnwindData |  |
| 40 | `?CommitRegistryValue@CUwfRegDevice@@QEAAJPEBG0@Z` | `0x14830` | 330 | UnwindData |  |
| 41 | `?CommitRegistryValueDeletion@CUwfRegDevice@@QEAAJPEBG0@Z` | `0x14980` | 330 | UnwindData |  |
| 77 | `?GetOverlayFiles@CUwfOverlayDevice@@QEAAJAEA_KAEAV?$CRBMap@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@_KV?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@V?$CElementTraits@_K@2@@ATL@@@Z` | `0x14C80` | 576 | UnwindData |  |
| 90 | `?Initialize@CDevice@@QEAAJPEBG@Z` | `0x14F90` | 166 | UnwindData |  |
| 94 | `?Initialize@CUwfOverlayDevice@@QEAAJPEBG@Z` | `0x15040` | 279 | UnwindData |  |
| 95 | `?Initialize@CUwfRegDevice@@QEAAJXZ` | `0x15160` | 31 | UnwindData |  |
| 97 | `?Initialize@CUwfVolumeDevice@@QEAAJXZ` | `0x15190` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `?InitializeWithNoPermissions@CDevice@@QEAAJPEBG@Z` | `0x151B0` | 163 | UnwindData |  |
| 133 | `?SendIOCTL@CDevice@@QEAAJKPEAXK0KPEAK@Z` | `0x15C60` | 129 | UnwindData |  |
| 240 | `?get_RomModeDisposition@CUwfVolumeDevice@@QEAAJPEAW4_UWFVOL_ROM_MODE_DISPOSITION@@@Z` | `0x15EF0` | 69 | UnwindData |  |
| 257 | `?set_HORMEnabled@CUwfVolumeDevice@@QEAAJ_N@Z` | `0x15F40` | 52 | UnwindData |  |
| 261 | `?set_OverlayCriticalThreshold@CUwfVolumeDevice@@QEAAJK@Z` | `0x15F80` | 49 | UnwindData |  |
| 270 | `?set_OverlayWarningThreshold@CUwfVolumeDevice@@QEAAJK@Z` | `0x15FC0` | 49 | UnwindData |  |
| 283 | `?set_RomModeDisposition@CUwfVolumeDevice@@QEAAJW4_UWFVOL_ROM_MODE_DISPOSITION@@@Z` | `0x16000` | 49 | UnwindData |  |
| 3 | `??0CUwfManagement@@QEAA@XZ` | `0x16040` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??1CUwfManagement@@UEAA@XZ` | `0x16120` | 78 | UnwindData |  |
| 30 | `?Close@CUwfManagement@@QEAAXXZ` | `0x16340` | 67 | UnwindData |  |
| 34 | `?CommitFile@CUwfManagement@@QEAAJPEBG0@Z` | `0x16390` | 1,142 | UnwindData |  |
| 35 | `?CommitFileDeletion@CUwfManagement@@QEAAJPEBG00@Z` | `0x16810` | 1,093 | UnwindData |  |
| 36 | `?CommitRegistry@CUwfManagement@@QEAAJ_NPEBG1@Z` | `0x16C60` | 681 | UnwindData |  |
| 37 | `?CommitRegistryDeletion@CUwfManagement@@QEAAJ_NPEBG1@Z` | `0x16F10` | 677 | UnwindData |  |
| 67 | `?Finalize@CUwfManagement@@QEAAJXZ` | `0x171C0` | 202 | UnwindData |  |
| 82 | `?GetSystemShutdownState@CUwfManagement@@QEAAJPEA_N@Z` | `0x17A00` | 174 | UnwindData |  |
| 92 | `?Initialize@CUwfManagement@@QEAAJXZ` | `0x17AC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `?Initialize@CUwfManagement@@QEAAJ_N@Z` | `0x17AD0` | 176 | UnwindData |  |
| 108 | `?LookupShutdownPrivilegeInCurThreadToken@CUwfManagement@@QEAAJAEA_N@Z` | `0x17C30` | 416 | UnwindData |  |
| 132 | `?ResetUwfSettings@CUwfManagement@@QEAAJXZ` | `0x17E40` | 77 | UnwindData |  |
| 142 | `?ShutdownSystem@CUwfManagement@@QEAAJ_N@Z` | `0x17FE0` | 388 | UnwindData |  |
| 212 | `?get_HORMEnabled@CUwfManagement@@QEAAJPEA_N@Z` | `0x18440` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `?get_OverlayCriticalThreshold@CUwfManagement@@QEAAJPEAK@Z` | `0x187C0` | 35 | UnwindData |  |
| 218 | `?get_OverlayFlags@CUwfManagement@@QEAAJ_NPEAK@Z` | `0x187F0` | 55 | UnwindData |  |
| 220 | `?get_OverlayInformation@CUwfManagement@@QEAAJPEBGPEAU_UWFVOL_OVERLAY_DATA_OUTPUT@@PEAK2@Z` | `0x18830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `?get_OverlayMaximumSize@CUwfManagement@@QEAAJ_NPEAK@Z` | `0x18840` | 55 | UnwindData |  |
| 223 | `?get_OverlayType@CUwfManagement@@QEAAJ_NPEAW4_UWF_CONFIG_OVERLAY_TYPE@@@Z` | `0x18880` | 55 | UnwindData |  |
| 226 | `?get_OverlayWarningThreshold@CUwfManagement@@QEAAJPEAK@Z` | `0x188C0` | 35 | UnwindData |  |
| 236 | `?get_ResetPersistentOverlay@CUwfManagement@@QEAAJPEAK@Z` | `0x188F0` | 170 | UnwindData |  |
| 237 | `?get_ResetPersistentStateSavedMode@CUwfManagement@@QEAAJ_NPEAK@Z` | `0x189A0` | 55 | UnwindData |  |
| 239 | `?get_RomModeDisposition@CUwfManagement@@QEAAJPEAW4_UWFVOL_ROM_MODE_DISPOSITION@@@Z` | `0x189E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `?get_UwfConfiguration@CUwfManagement@@QEAAJPEAPEAVCUwfConfiguration@@@Z` | `0x189F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `?set_HORMEnabled@CUwfManagement@@QEAAJ_N@Z` | `0x18A10` | 742 | UnwindData |  |
| 260 | `?set_OverlayCriticalThreshold@CUwfManagement@@QEAAJK@Z` | `0x18D00` | 64 | UnwindData |  |
| 262 | `?set_OverlayFlags@CUwfManagement@@QEAAJK@Z` | `0x18D50` | 183 | UnwindData |  |
| 264 | `?set_OverlayMaximumSize@CUwfManagement@@QEAAJK@Z` | `0x18E10` | 236 | UnwindData |  |
| 266 | `?set_OverlayType@CUwfManagement@@QEAAJW4_UWF_CONFIG_OVERLAY_TYPE@@@Z` | `0x18F10` | 340 | UnwindData |  |
| 269 | `?set_OverlayWarningThreshold@CUwfManagement@@QEAAJK@Z` | `0x19070` | 64 | UnwindData |  |
| 279 | `?set_ResetPersistentOverlay@CUwfManagement@@QEAAJK@Z` | `0x190C0` | 325 | UnwindData |  |
| 280 | `?set_ResetPersistentStateSavedMode@CUwfManagement@@QEAAJK@Z` | `0x19210` | 183 | UnwindData |  |
| 282 | `?set_RomModeDisposition@CUwfManagement@@QEAAJW4_UWFVOL_ROM_MODE_DISPOSITION@@@Z` | `0x192D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `?set_ServicingModeEnabled@CUwfManagement@@QEAAJ_N0@Z` | `0x192E0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `?Begin@CUwfProvider@@QEAAJXZ` | `0x193B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `?Begin@CUwfProvider@@QEAAJ_N@Z` | `0x193C0` | 61 | UnwindData |  |
| 68 | `?Finalize@CUwfProvider@@QEAAJXZ` | `0x19410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `?GetConfiguration@CUwfProvider@@QEAAPEAVCUwfConfiguration@@XZ` | `0x19430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `?GetManagement@CUwfProvider@@QEAAPEAVCUwfManagement@@XZ` | `0x19440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `?GetStaticConfiguration@CUwfProvider@@QEAAJ_NPEAPEAVCUwfStaticConfiguration@@@Z` | `0x19450` | 119 | UnwindData |  |
| 84 | `?GetUwfProvider@CUwfProvider@@SAPEAV1@XZ` | `0x194D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `?LOCK@CUwfProvider@@QEAAXXZ` | `0x194E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `?UNLOCK@CUwfProvider@@QEAAXXZ` | `0x19500` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `UwfCfgAddFileExclusion` | `0x195D0` | 145 | UnwindData |  |
| 149 | `UwfCfgAddRegExclusion` | `0x19670` | 137 | UnwindData |  |
| 150 | `UwfCfgAddVolume` | `0x19700` | 278 | UnwindData |  |
| 151 | `UwfCfgCommitFile` | `0x19820` | 217 | UnwindData |  |
| 152 | `UwfCfgCommitFileDeletion` | `0x19900` | 288 | UnwindData |  |
| 153 | `UwfCfgCommitRegistry` | `0x19A30` | 186 | UnwindData |  |
| 154 | `UwfCfgCommitRegistryDeletion` | `0x19AF0` | 186 | UnwindData |  |
| 155 | `UwfCfgDoesFileExclusionExist` | `0x19BB0` | 159 | UnwindData |  |
| 156 | `UwfCfgDoesRegExclusionExist` | `0x19C60` | 141 | UnwindData |  |
| 157 | `UwfCfgDoesVolumeExist` | `0x19D00` | 123 | UnwindData |  |
| 158 | `UwfCfgGetCriticalThreshold` | `0x19D90` | 148 | UnwindData |  |
| 159 | `UwfCfgGetDriveLetter` | `0x19E30` | 159 | UnwindData |  |
| 160 | `UwfCfgGetFileExclusions` | `0x19EE0` | 296 | UnwindData |  |
| 161 | `UwfCfgGetFilterEnabled` | `0x1A010` | 118 | UnwindData |  |
| 162 | `UwfCfgGetHormEnabled` | `0x1A090` | 124 | UnwindData |  |
| 163 | `UwfCfgGetOverlayCommitState` | `0x1A120` | 149 | UnwindData |  |
| 164 | `UwfCfgGetOverlayFlags` | `0x1A1C0` | 146 | UnwindData |  |
| 165 | `UwfCfgGetOverlayInformation` | `0x1A260` | 660 | UnwindData |  |
| 166 | `UwfCfgGetOverlayMaximumSize` | `0x1A500` | 146 | UnwindData |  |
| 167 | `UwfCfgGetOverlayType` | `0x1A5A0` | 146 | UnwindData |  |
| 168 | `UwfCfgGetPersistDomainSecretKey` | `0x1A640` | 141 | UnwindData |  |
| 169 | `UwfCfgGetPersistTSCAL` | `0x1A6E0` | 160 | UnwindData |  |
| 170 | `UwfCfgGetRegExclusions` | `0x1A790` | 276 | UnwindData |  |
| 171 | `UwfCfgGetResetPersistentOverlay` | `0x1A8B0` | 148 | UnwindData |  |
| 172 | `UwfCfgGetResetPersistentOverlaySavedMode` | `0x1A950` | 164 | UnwindData |  |
| 173 | `UwfCfgGetServicingModeEnabled` | `0x1AA00` | 141 | UnwindData |  |
| 174 | `UwfCfgGetShutdownPending` | `0x1AAA0` | 148 | UnwindData |  |
| 175 | `UwfCfgGetVolumeBindByDriveLetter` | `0x1AB40` | 171 | UnwindData |  |
| 176 | `UwfCfgGetVolumeProtected` | `0x1AC00` | 154 | UnwindData |  |
| 177 | `UwfCfgGetVolumeSwapfileSize` | `0x1ACA0` | 154 | UnwindData |  |
| 178 | `UwfCfgGetVolumes` | `0x1AD40` | 593 | UnwindData |  |
| 179 | `UwfCfgGetWarningThreshold` | `0x1AFA0` | 148 | UnwindData |  |
| 180 | `UwfCfgRemoveFileExclusion` | `0x1B040` | 145 | UnwindData |  |
| 181 | `UwfCfgRemoveRegExclusion` | `0x1B0E0` | 137 | UnwindData |  |
| 182 | `UwfCfgRemoveVolume` | `0x1B170` | 263 | UnwindData |  |
| 183 | `UwfCfgResetSettings` | `0x1B280` | 109 | UnwindData |  |
| 184 | `UwfCfgRestartSystem` | `0x1B300` | 111 | UnwindData |  |
| 185 | `UwfCfgSetCriticalThreshold` | `0x1B380` | 122 | UnwindData |  |
| 186 | `UwfCfgSetFilterEnabled` | `0x1B400` | 904 | UnwindData |  |
| 187 | `UwfCfgSetHormEnabled` | `0x1B790` | 124 | UnwindData |  |
| 188 | `UwfCfgSetOverlayCommitState` | `0x1B820` | 130 | UnwindData |  |
| 189 | `UwfCfgSetOverlayFlags` | `0x1B8B0` | 285 | UnwindData |  |
| 190 | `UwfCfgSetOverlayMaximumSize` | `0x1B9E0` | 105 | UnwindData |  |
| 191 | `UwfCfgSetOverlayType` | `0x1BA50` | 105 | UnwindData |  |
| 192 | `UwfCfgSetPersistDomainSecretKey` | `0x1BAC0` | 116 | UnwindData |  |
| 193 | `UwfCfgSetPersistTSCAL` | `0x1BB40` | 116 | UnwindData |  |
| 194 | `UwfCfgSetResetPersistentOverlay` | `0x1BBC0` | 161 | UnwindData |  |
| 195 | `UwfCfgSetResetPersistentOverlaySavedMode` | `0x1BC70` | 149 | UnwindData |  |
| 196 | `UwfCfgSetServicingModeEnabled` | `0x1BD10` | 518 | UnwindData |  |
| 197 | `UwfCfgSetVolumeBindByDriveLetter` | `0x1BF20` | 142 | UnwindData |  |
| 198 | `UwfCfgSetVolumeProtected` | `0x1BFC0` | 140 | UnwindData |  |
| 199 | `UwfCfgSetVolumeSwapfileSize` | `0x1C060` | 757 | UnwindData |  |
| 200 | `UwfCfgSetWarningThreshold` | `0x1C360` | 122 | UnwindData |  |
| 201 | `UwfCfgShutdownSystem` | `0x1C3E0` | 111 | UnwindData |  |

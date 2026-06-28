# Binary Specification: uwfcfgmgmt.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\uwfcfgmgmt.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `63f23d7fd2ab74022b696187eb4a7528b036e4d0608f22853df392cd2c85b9f7`
* **Total Exported Functions:** 297

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `??0CUwfOverlayDevice@@QEAA@XZ` | `0x34E0` | 74 | UnwindData |  |
| 99 | `?IsCurrentSession@CUwfStaticConfiguration@@QEAA_NXZ` | `0x47B0` | 5,536 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0CUwfConfiguration@@QEAA@XZ` | `0x5D50` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0CUwfStaticConfiguration@@QEAA@XZ` | `0x5DC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0CUwfStaticVolumeConfiguration@@QEAA@XZ` | `0x5DF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??1CUwfConfiguration@@UEAA@XZ` | `0x5E20` | 65 | UnwindData |  |
| 15 | `??1CUwfStaticConfiguration@@UEAA@XZ` | `0x5E70` | 55 | UnwindData |  |
| 16 | `??1CUwfStaticVolumeConfiguration@@UEAA@XZ` | `0x5EB0` | 41 | UnwindData |  |
| 19 | `?AddFileExclusion@CUwfStaticVolumeConfiguration@@QEAAJPEBG@Z` | `0x60E0` | 657 | UnwindData |  |
| 21 | `?AddRegKeyExclusion@CUwfStaticConfiguration@@QEAAJPEBG@Z` | `0x6380` | 596 | UnwindData |  |
| 29 | `?Close@CUwfConfiguration@@QEAAXXZ` | `0x6690` | 50 | UnwindData |  |
| 32 | `?Close@CUwfStaticConfiguration@@QEAAXXZ` | `0x66D0` | 52 | UnwindData |  |
| 33 | `?Close@CUwfStaticVolumeConfiguration@@QEAAXXZ` | `0x6710` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `?Compare@CUwfStaticVolumeConfiguration@@QEAAJAEAV1@PEA_N@Z` | `0x6720` | 102 | UnwindData |  |
| 43 | `?CopyTo@CUwfStaticConfiguration@@QEAAJPEAUHKEY__@@PEBG_N@Z` | `0x6F50` | 142 | UnwindData |  |
| 44 | `?CopyTree@CUwfConfiguration@@QEAAJAEAVCUwfRegKey@@PEBGPEAUHKEY__@@_N@Z` | `0x6FF0` | 50 | UnwindData |  |
| 49 | `?CreateKey@CUwfConfiguration@@QEAAJPEAUHKEY__@@PEBGKKPEAKAEAVCUwfRegKey@@@Z` | `0x7030` | 120 | UnwindData |  |
| 50 | `?CreateOverlayFile@CUwfStaticConfiguration@@QEAAJK@Z` | `0x70B0` | 200 | UnwindData |  |
| 53 | `?CreateVolume@CUwfStaticConfiguration@@QEAAJPEBG0PEAPEAVCUwfStaticVolumeConfiguration@@@Z` | `0x7180` | 1,217 | UnwindData |  |
| 54 | `?DeleteBindingConfiguration@CUwfStaticVolumeConfiguration@@QEAAJXZ` | `0x7650` | 81 | UnwindData |  |
| 55 | `?DeleteFileW@CUwfConfiguration@@QEAAJPEBG@Z` | `0x76B0` | 92 | UnwindData |  |
| 56 | `?DeleteOverlayFile@CUwfStaticConfiguration@@QEAAJXZ` | `0x7790` | 93 | UnwindData |  |
| 57 | `?DeleteTree@CUwfConfiguration@@QEAAJAEAVCUwfRegKey@@PEBG@Z` | `0x78C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `?DeleteTreeFromRoot@CUwfConfiguration@@QEAAJAEAVCUwfRegKey@@PEBG@Z` | `0x78F0` | 165 | UnwindData |  |
| 62 | `?DeleteVolume@CUwfStaticConfiguration@@QEAAJK@Z` | `0x79A0` | 455 | UnwindData |  |
| 69 | `?FindFileExclusion@CUwfStaticVolumeConfiguration@@QEAAJPEBG@Z` | `0x7CB0` | 364 | UnwindData |  |
| 70 | `?FindRegKeyExclusion@CUwfStaticConfiguration@@QEAAJPEBG@Z` | `0x7E30` | 364 | UnwindData |  |
| 72 | `?FixupUpdatedSettings@CUwfConfiguration@@QEAAJXZ` | `0x7FB0` | 314 | UnwindData |  |
| 76 | `?GetOverlayFileName@CUwfStaticConfiguration@@QEAAJPEAPEAG@Z` | `0x80F0` | 944 | UnwindData |  |
| 88 | `?HaveUwfFactorySettings@CUwfConfiguration@@QEAAJPEA_N@Z` | `0x8830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | `?Initialize@CUwfConfiguration@@QEAAJPEAX@Z` | `0x8840` | 396 | UnwindData |  |
| 96 | `?Initialize@CUwfStaticVolumeConfiguration@@QEAAJPEAUHKEY__@@K_NPEAVCUwfConfiguration@@PEAVCUwfStaticConfiguration@@@Z` | `0x89E0` | 282 | UnwindData |  |
| 100 | `?IsFileExcluded@CUwfStaticVolumeConfiguration@@QEAAJPEBGPEA_N@Z` | `0x8B00` | 276 | UnwindData |  |
| 101 | `?IsHORMEnabled@CUwfConfiguration@@QEAA_NXZ` | `0x8C20` | 122 | UnwindData |  |
| 102 | `?IsOverlayFileExist@CUwfStaticConfiguration@@QEAAJPEA_N@Z` | `0x8CA0` | 198 | UnwindData |  |
| 110 | `?Open@CUwfStaticConfiguration@@QEAAJ_NK0PEAVCUwfConfiguration@@@Z` | `0x8E50` | 463 | UnwindData |  |
| 111 | `?OpenKey@CUwfConfiguration@@QEAAJPEAUHKEY__@@PEBGKAEAVCUwfRegKey@@@Z` | `0x9030` | 816 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `?ReOpen@CUwfStaticConfiguration@@QEAAJK@Z` | `0x9360` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `?ReOpen@CUwfStaticVolumeConfiguration@@QEAAJPEAUHKEY__@@@Z` | `0x9390` | 172 | UnwindData |  |
| 125 | `?ReleaseStaticVolumeConfiguration@CUwfStaticConfiguration@@QEAAXXZ` | `0x9450` | 46 | UnwindData |  |
| 126 | `?RemoveAllFileExclusions@CUwfStaticVolumeConfiguration@@QEAAJXZ` | `0x9490` | 97 | UnwindData |  |
| 127 | `?RemoveFileExclusion@CUwfStaticVolumeConfiguration@@QEAAJPEBG@Z` | `0x9500` | 477 | UnwindData |  |
| 128 | `?RemoveRegKeyExclusion@CUwfStaticConfiguration@@QEAAJPEBG@Z` | `0x96F0` | 452 | UnwindData |  |
| 129 | `?ResetBindingConfiguration@CUwfStaticVolumeConfiguration@@QEAAJXZ` | `0x98C0` | 98 | UnwindData |  |
| 130 | `?ResetFileExclusions@CUwfStaticVolumeConfiguration@@QEAAJXZ` | `0x9930` | 151 | UnwindData |  |
| 131 | `?ResetUwfSettings@CUwfConfiguration@@QEAAJXZ` | `0x99D0` | 167 | UnwindData |  |
| 138 | `?SetOverlayFileSize@CUwfStaticConfiguration@@QEAAJK@Z` | `0xA0E0` | 371 | UnwindData |  |
| 144 | `?UpdateDWORDValue@CUwfConfiguration@@QEAAJAEAVCUwfRegKey@@PEBGK_N@Z` | `0xA990` | 241 | UnwindData |  |
| 145 | `?UpdateMultiSzValue@CUwfConfiguration@@QEAAJAEAVCUwfRegKey@@PEBGQEAU_MULTISZ@@_N@Z` | `0xAA90` | 411 | UnwindData |  |
| 146 | `?UpdateQWORDValue@CUwfConfiguration@@QEAAJAEAVCUwfRegKey@@PEBG_K_N@Z` | `0xAEB0` | 242 | UnwindData |  |
| 147 | `?UpdateSzValue@CUwfConfiguration@@QEAAJAEAVCUwfRegKey@@PEBG1_N@Z` | `0xAFB0` | 348 | UnwindData |  |
| 206 | `?get_BindingType@CUwfStaticVolumeConfiguration@@QEAAJPEAK@Z` | `0xB3C0` | 45 | UnwindData |  |
| 207 | `?get_DiskNumber@CUwfStaticVolumeConfiguration@@QEAAJPEAK@Z` | `0xB400` | 45 | UnwindData |  |
| 208 | `?get_DiskSignature@CUwfStaticVolumeConfiguration@@QEAAJPEAK@Z` | `0xB440` | 45 | UnwindData |  |
| 209 | `?get_DriveLetter@CUwfStaticVolumeConfiguration@@QEAAJPEAPEAG@Z` | `0xB480` | 45 | UnwindData |  |
| 210 | `?get_FileExclusions@CUwfStaticVolumeConfiguration@@QEAAJPEAPEAU_MULTISZ@@@Z` | `0xB4C0` | 45 | UnwindData |  |
| 211 | `?get_HORMEnabled@CUwfConfiguration@@QEAAJPEA_N@Z` | `0xB500` | 170 | UnwindData |  |
| 213 | `?get_IsNoFileExclusion@CUwfStaticConfiguration@@QEAAJPEA_N@Z` | `0xB5B0` | 393 | UnwindData |  |
| 214 | `?get_IsNoRegExclusion@CUwfStaticConfiguration@@QEAAJPEA_N@Z` | `0xB740` | 86 | UnwindData |  |
| 215 | `?get_NumVolumes@CUwfStaticConfiguration@@QEAAJPEAK@Z` | `0xB7A0` | 45 | UnwindData |  |
| 216 | `?get_OverlayCriticalThreshold@CUwfConfiguration@@QEAAJPEAK@Z` | `0xB7E0` | 45 | UnwindData |  |
| 219 | `?get_OverlayFlags@CUwfStaticConfiguration@@QEAAJPEAK@Z` | `0xB820` | 166 | UnwindData |  |
| 222 | `?get_OverlayMaximumSize@CUwfStaticConfiguration@@QEAAJPEAK@Z` | `0xB8D0` | 45 | UnwindData |  |
| 224 | `?get_OverlayType@CUwfStaticConfiguration@@QEAAJPEAW4_UWF_CONFIG_OVERLAY_TYPE@@@Z` | `0xB910` | 189 | UnwindData |  |
| 225 | `?get_OverlayWarningThreshold@CUwfConfiguration@@QEAAJPEAK@Z` | `0xB9E0` | 45 | UnwindData |  |
| 227 | `?get_PartitionGUID@CUwfStaticVolumeConfiguration@@QEAAJPEAPEAG@Z` | `0xBA20` | 45 | UnwindData |  |
| 228 | `?get_PartitionNumber@CUwfStaticVolumeConfiguration@@QEAAJPEAK@Z` | `0xBA60` | 45 | UnwindData |  |
| 229 | `?get_PartitionOffset@CUwfStaticVolumeConfiguration@@QEAAJPEA_K@Z` | `0xBAA0` | 45 | UnwindData |  |
| 230 | `?get_PartitionStyle@CUwfStaticVolumeConfiguration@@QEAAJPEAW4_PARTITION_STYLE@@@Z` | `0xBAE0` | 166 | UnwindData |  |
| 231 | `?get_PersistDomainSecretKey@CUwfStaticConfiguration@@QEAAJPEA_N@Z` | `0xBB90` | 170 | UnwindData |  |
| 232 | `?get_PersistTSCAL@CUwfStaticConfiguration@@QEAAJPEA_N@Z` | `0xBC40` | 170 | UnwindData |  |
| 233 | `?get_Protected@CUwfStaticVolumeConfiguration@@QEAAJPEA_N@Z` | `0xBCF0` | 170 | UnwindData |  |
| 234 | `?get_RegKeyExclusions@CUwfStaticConfiguration@@QEAAJPEAPEAU_MULTISZ@@@Z` | `0xBDA0` | 45 | UnwindData |  |
| 235 | `?get_RegKeyExclusionsUWFSpecific@CUwfStaticConfiguration@@QEAAJPEAPEAU_MULTISZ@@@Z` | `0xBDE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 238 | `?get_ResetPersistentStateSavedMode@CUwfStaticConfiguration@@QEAAJPEAK@Z` | `0xBE00` | 166 | UnwindData |  |
| 241 | `?get_ServicingModeEnabled@CUwfStaticConfiguration@@QEAAJPEA_N@Z` | `0xBEB0` | 158 | UnwindData |  |
| 242 | `?get_StaticConfiguration@CUwfConfiguration@@QEAAJ_NPEAPEAVCUwfStaticConfiguration@@@Z` | `0xBF60` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 243 | `?get_StaticVolumeConfiguration@CUwfStaticConfiguration@@QEAAJKPEAPEAVCUwfStaticVolumeConfiguration@@@Z` | `0xBF90` | 216 | UnwindData |  |
| 244 | `?get_StaticVolumeConfiguration@CUwfStaticConfiguration@@QEAAJPEBG0PEAPEAVCUwfStaticVolumeConfiguration@@@Z` | `0xC070` | 672 | UnwindData |  |
| 245 | `?get_StaticVolumeConfiguration@CUwfStaticConfiguration@@QEAAJPEBGPEAPEAVCUwfStaticVolumeConfiguration@@@Z` | `0xC320` | 517 | UnwindData |  |
| 246 | `?get_SwapfileSize@CUwfStaticVolumeConfiguration@@QEAAJPEAK@Z` | `0xC530` | 62 | UnwindData |  |
| 248 | `?get_UwfEnabled@CUwfStaticConfiguration@@QEAAJPEA_N@Z` | `0xC580` | 170 | UnwindData |  |
| 249 | `?get_UwfEnabledBeforeServicing@CUwfConfiguration@@QEAAJPEAK@Z` | `0xC630` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 250 | `?get_VolumeGuid@CUwfStaticVolumeConfiguration@@QEAAJPEAPEAG@Z` | `0xC650` | 45 | UnwindData |  |
| 251 | `?set_BindingType@CUwfStaticVolumeConfiguration@@QEAAJK@Z` | `0xC690` | 356 | UnwindData |  |
| 252 | `?set_DiskNumber@CUwfStaticVolumeConfiguration@@QEAAJK@Z` | `0xC930` | 74 | UnwindData |  |
| 253 | `?set_DiskSignature@CUwfStaticVolumeConfiguration@@QEAAJK@Z` | `0xC980` | 74 | UnwindData |  |
| 254 | `?set_DriveLetter@CUwfStaticVolumeConfiguration@@QEAAJPEBG@Z` | `0xC9D0` | 124 | UnwindData |  |
| 255 | `?set_HORMEnabled@CUwfConfiguration@@QEAAJ_N0@Z` | `0xCA60` | 203 | UnwindData |  |
| 258 | `?set_NumVolumes@CUwfStaticConfiguration@@QEAAJK@Z` | `0xCB40` | 74 | UnwindData |  |
| 259 | `?set_OverlayCriticalThreshold@CUwfConfiguration@@QEAAJK@Z` | `0xCB90` | 74 | UnwindData |  |
| 263 | `?set_OverlayFlags@CUwfStaticConfiguration@@QEAAJK@Z` | `0xCBE0` | 105 | UnwindData |  |
| 265 | `?set_OverlayMaximumSize@CUwfStaticConfiguration@@QEAAJK@Z` | `0xCC50` | 264 | UnwindData |  |
| 267 | `?set_OverlayType@CUwfStaticConfiguration@@QEAAJW4_UWF_CONFIG_OVERLAY_TYPE@@@Z` | `0xCD60` | 483 | UnwindData |  |
| 268 | `?set_OverlayWarningThreshold@CUwfConfiguration@@QEAAJK@Z` | `0xCF50` | 74 | UnwindData |  |
| 271 | `?set_PartitionGUID@CUwfStaticVolumeConfiguration@@QEAAJPEBG@Z` | `0xCFA0` | 74 | UnwindData |  |
| 272 | `?set_PartitionNumber@CUwfStaticVolumeConfiguration@@QEAAJK@Z` | `0xCFF0` | 74 | UnwindData |  |
| 273 | `?set_PartitionOffset@CUwfStaticVolumeConfiguration@@QEAAJ_K@Z` | `0xD040` | 74 | UnwindData |  |
| 274 | `?set_PartitionStyle@CUwfStaticVolumeConfiguration@@QEAAJW4_PARTITION_STYLE@@@Z` | `0xD090` | 74 | UnwindData |  |
| 275 | `?set_PersistDomainSecretKey@CUwfStaticConfiguration@@QEAAJ_N@Z` | `0xD0E0` | 750 | UnwindData |  |
| 276 | `?set_PersistTSCAL@CUwfStaticConfiguration@@QEAAJ_N@Z` | `0xD3E0` | 750 | UnwindData |  |
| 277 | `?set_Protected@CUwfStaticVolumeConfiguration@@QEAAJ_N@Z` | `0xD6E0` | 236 | UnwindData |  |
| 278 | `?set_RegKeyExclusionsUWFSpecific@CUwfStaticConfiguration@@QEAAJPEAU_MULTISZ@@@Z` | `0xD7E0` | 48 | UnwindData |  |
| 281 | `?set_ResetPersistentStateSavedMode@CUwfStaticConfiguration@@QEAAJK@Z` | `0xD820` | 102 | UnwindData |  |
| 285 | `?set_ServicingModeEnabled@CUwfStaticConfiguration@@QEAAJ_N@Z` | `0xD890` | 275 | UnwindData |  |
| 286 | `?set_SwapfileSize@CUwfStaticVolumeConfiguration@@QEAAJK@Z` | `0xD9B0` | 74 | UnwindData |  |
| 287 | `?set_UwfBootPersistenceEnabled@CUwfConfiguration@@QEAAJ_N@Z` | `0xDA00` | 296 | UnwindData |  |
| 288 | `?set_UwfEnabled@CUwfStaticConfiguration@@QEAAJ_N@Z` | `0xDB30` | 156 | UnwindData |  |
| 289 | `?set_UwfEnabledBeforeServicing@CUwfConfiguration@@QEAAJK@Z` | `0xDBE0` | 74 | UnwindData |  |
| 290 | `?set_VolumeGuid@CUwfStaticVolumeConfiguration@@QEAAJPEBG@Z` | `0xDC30` | 86 | UnwindData |  |
| 6 | `??0CUwfRegKey@@QEAA@XZ` | `0xDE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `??1CUwfRegKey@@QEAA@XZ` | `0xDE90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `?AddDWORDValue@CUwfRegKey@@QEAAJPEBGK@Z` | `0xDEA0` | 187 | UnwindData |  |
| 20 | `?AddMultiSzValue@CUwfRegKey@@QEAAJPEBG0@Z` | `0xDF70` | 412 | UnwindData |  |
| 22 | `?Attach@CUwfRegKey@@QEAAJPEAUHKEY__@@@Z` | `0xE120` | 62 | UnwindData |  |
| 31 | `?Close@CUwfRegKey@@QEAAJXZ` | `0xE170` | 42 | UnwindData |  |
| 45 | `?CopyTree@CUwfRegKey@@QEAAJAEAV1@PEBG_N@Z` | `0xE1A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 46 | `?CopyTree@CUwfRegKey@@QEAAJPEAUHKEY__@@PEBG_N@Z` | `0xE1B0` | 119 | UnwindData |  |
| 47 | `?CopyTreeTransacted@CUwfRegKey@@QEAAJPEBGPEAUHKEY__@@PEAX_N@Z` | `0xE230` | 470 | UnwindData |  |
| 48 | `?Create@CUwfRegKey@@QEAAJPEAUHKEY__@@PEBGPEAGKKPEAU_SECURITY_ATTRIBUTES@@PEAK@Z` | `0xE5A0` | 175 | UnwindData |  |
| 51 | `?CreateSubKey@CUwfRegKey@@QEAAJPEBGKKPEAKPEAV1@@Z` | `0xE660` | 228 | UnwindData |  |
| 52 | `?CreateTransacted@CUwfRegKey@@QEAAJPEAUHKEY__@@PEBGPEAGKKPEAU_SECURITY_ATTRIBUTES@@PEAKPEAX@Z` | `0xE750` | 193 | UnwindData |  |
| 58 | `?DeleteTree@CUwfRegKey@@QEAAJPEBG@Z` | `0xE820` | 63 | UnwindData |  |
| 60 | `?DeleteTreeTransacted@CUwfRegKey@@QEAAJPEBGPEAX@Z` | `0xE870` | 305 | UnwindData |  |
| 61 | `?DeleteValue@CUwfRegKey@@QEAAJPEBG@Z` | `0xE9B0` | 51 | UnwindData |  |
| 63 | `?Detach@CUwfRegKey@@QEAAPEAUHKEY__@@XZ` | `0xE9F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `?GetSubKeyAt@CUwfRegKey@@QEAAJKPEAGK@Z` | `0xEA00` | 77 | UnwindData |  |
| 109 | `?Open@CUwfRegKey@@QEAAJPEAUHKEY__@@PEBGK@Z` | `0xEA60` | 127 | UnwindData |  |
| 112 | `?OpenSubKey@CUwfRegKey@@QEAAJPEBGKAEAV1@@Z` | `0xEAF0` | 82 | UnwindData |  |
| 113 | `?OpenSubKeyAt@CUwfRegKey@@QEAAJKKAEAV1@@Z` | `0xEB50` | 105 | UnwindData |  |
| 114 | `?OpenTransacted@CUwfRegKey@@QEAAJPEAUHKEY__@@PEBGKPEAX@Z` | `0xEBC0` | 142 | UnwindData |  |
| 117 | `?QueryBinaryValue@CUwfRegKey@@QEAAJPEBGPEAPEAEPEAK@Z` | `0xEC60` | 286 | UnwindData |  |
| 118 | `?QueryDWORDValue@CUwfRegKey@@QEAAJPEBGPEAK@Z` | `0xED90` | 118 | UnwindData |  |
| 119 | `?QueryMultiSzValue@CUwfRegKey@@QEAAJPEBGPEAPEAU_MULTISZ@@@Z` | `0xEE10` | 325 | UnwindData |  |
| 120 | `?QueryQWORDValue@CUwfRegKey@@QEAAJPEBGPEA_K@Z` | `0xEF60` | 118 | UnwindData |  |
| 121 | `?QuerySzValue@CUwfRegKey@@QEAAJPEBGPEAPEAG@Z` | `0xEFE0` | 273 | UnwindData |  |
| 134 | `?SetBinaryValue@CUwfRegKey@@QEAAJPEBGPEAEK@Z` | `0xF100` | 68 | UnwindData |  |
| 136 | `?SetDWORDValue@CUwfRegKey@@QEAAJPEBGK@Z` | `0xF150` | 76 | UnwindData |  |
| 137 | `?SetMultiSzValue@CUwfRegKey@@QEAAJPEBGQEAU_MULTISZ@@@Z` | `0xF1B0` | 93 | UnwindData |  |
| 139 | `?SetQWORDValue@CUwfRegKey@@QEAAJPEBG_K@Z` | `0xF220` | 80 | UnwindData |  |
| 141 | `?SetSzValue@CUwfRegKey@@QEAAJPEBG0@Z` | `0xF280` | 102 | UnwindData |  |
| 26 | `?CanVolumeBeProtected@@YAJPEBG_NPEA_N@Z` | `0xF320` | 231 | UnwindData |  |
| 27 | `?CaptureUwfSettings@@YAJW4E_UNATTEND_REASON@@@Z` | `0xF410` | 246 | UnwindData |  |
| 64 | `?DisableAutoDefragService@@YAJH@Z` | `0xFC40` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `?DisableService@@YAJPEBG_N@Z` | `0xFD70` | 314 | UnwindData |  |
| 71 | `?FixupLowerFiltersSetting@@YAJXZ` | `0x10380` | 795 | UnwindData |  |
| 78 | `?GetServiceStartType@@YAJPEBGPEAK@Z` | `0x108D0` | 360 | UnwindData |  |
| 83 | `?GetUwfProtectableVolumeList@@YAJ_NPEAKPEAUUWF_PROTECTABLEVOLUME_INFO@@@Z` | `0x10BB0` | 709 | UnwindData |  |
| 86 | `?GetWinResumeObjectId@@YAJPEAPEAG@Z` | `0x10E80` | 101 | UnwindData |  |
| 87 | `?HaveCapturedUwfSettings@@YAJPEA_N@Z` | `0x10EF0` | 199 | UnwindData |  |
| 103 | `?IsUserAdmin@@YAJPEA_N@Z` | `0x114E0` | 34 | UnwindData |  |
| 124 | `?RegReadValue@@YAJPEAUHKEY__@@PEBGKPEAPEAEPEAK@Z` | `0x11F40` | 250 | UnwindData |  |
| 135 | `?SetBootStatusPolicy@@YAJPEBG@Z` | `0x12040` | 122 | UnwindData |  |
| 140 | `?SetServiceStartType@@YAJPEBGK@Z` | `0x120C0` | 304 | UnwindData |  |
| 204 | `?VolumeGetConfig@@YAJPEAVCUwfStaticConfiguration@@PEBG1PEAPEAVCUwfStaticVolumeConfiguration@@@Z` | `0x12200` | 873 | UnwindData |  |
| 205 | `?VolumeGetVolumeGuid@@YAJPEBGPEAGK@Z` | `0x12980` | 150 | UnwindData |  |
| 291 | `MultiSzAdd` | `0x12AE0` | 112 | UnwindData |  |
| 292 | `MultiSzAlloc` | `0x12B60` | 265 | UnwindData |  |
| 293 | `MultiSzCompare` | `0x12C70` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 294 | `MultiSzFind` | `0x12CE0` | 180 | UnwindData |  |
| 295 | `MultiSzFree` | `0x12DA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 296 | `MultiSzReAlloc` | `0x12DC0` | 254 | UnwindData |  |
| 297 | `MultiSzRemove` | `0x12ED0` | 253 | UnwindData |  |
| 25 | `?CanFileBeCommitted@@YA_NPEBG0@Z` | `0x12FE0` | 236 | UnwindData |  |
| 66 | `?ExecuteBackgroundProcess@@YAJPEBG0_NPEAK@Z` | `0x130E0` | 428 | UnwindData |  |
| 74 | `?GetDriveLetterFromVolumeName@@YAJPEBGPEAG@Z` | `0x13370` | 444 | UnwindData |  |
| 81 | `?GetSystemDriveLetter@@YAJPEAPEAG@Z` | `0x13540` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `?GetVolumeGuidFromDriveName@@YAJPEBGPEAGK@Z` | `0x13560` | 310 | UnwindData |  |
| 89 | `?HiberFileExists@@YA_NXZ` | `0x136A0` | 168 | UnwindData |  |
| 104 | `?IsValidDriveLetter@@YA_NPEBG@Z` | `0x13930` | 91 | UnwindData |  |
| 105 | `?IsValidOverlayConfig@@YA_NW4_UWF_CONFIG_OVERLAY_TYPE@@K@Z` | `0x139A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `?IsValidVolumeName@@YA_NPEBG@Z` | `0x139E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `?ParsePathSpec@@YAJPEBGPEAGK1K1K@Z` | `0x139F0` | 607 | UnwindData |  |
| 116 | `?ParseVolumeGUID@@YAJPEBGPEAGK@Z` | `0x13D20` | 298 | UnwindData |  |
| 202 | `?ValidateFileNameToBeCommitted@@YA?AW4FILE_COMMIT_VALIDATE_RESULT@@_NPEBG11@Z` | `0x13E50` | 348 | UnwindData |  |
| 203 | `?ValidateRegistryKeyValueToBeCommitted@@YA?AW4REG_COMMIT_VALIDATE_RESULT@@_N0PEBG1KPEAPEAG@Z` | `0x13FC0` | 448 | UnwindData |  |
| 1 | `??0CDevice@@QEAA@XZ` | `0x142A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `??0CUwfVolumeDevice@@QEAA@XZ` | `0x142A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0CUwfRegDevice@@QEAA@XZ` | `0x142C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??1CDevice@@UEAA@XZ` | `0x142F0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 13 | `??1CUwfRegDevice@@UEAA@XZ` | `0x142F0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `??1CUwfVolumeDevice@@UEAA@XZ` | `0x142F0` | 848 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `?Close@CDevice@@QEAAXXZ` | `0x14640` | 43 | UnwindData |  |
| 38 | `?CommitRegistryKey@CUwfRegDevice@@QEAAJPEBG@Z` | `0x14680` | 216 | UnwindData |  |
| 39 | `?CommitRegistryKeyDeletion@CUwfRegDevice@@QEAAJPEBG@Z` | `0x14760` | 216 | UnwindData |  |
| 40 | `?CommitRegistryValue@CUwfRegDevice@@QEAAJPEBG0@Z` | `0x14840` | 330 | UnwindData |  |
| 41 | `?CommitRegistryValueDeletion@CUwfRegDevice@@QEAAJPEBG0@Z` | `0x14990` | 330 | UnwindData |  |
| 77 | `?GetOverlayFiles@CUwfOverlayDevice@@QEAAJAEA_KAEAV?$CRBMap@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@_KV?$CElementTraits@V?$CStringT@GV?$StrTraitATL@GV?$ChTraitsCRT@G@ATL@@@ATL@@@ATL@@@2@V?$CElementTraits@_K@2@@ATL@@@Z` | `0x14C90` | 576 | UnwindData |  |
| 90 | `?Initialize@CDevice@@QEAAJPEBG@Z` | `0x14FA0` | 166 | UnwindData |  |
| 94 | `?Initialize@CUwfOverlayDevice@@QEAAJPEBG@Z` | `0x15050` | 279 | UnwindData |  |
| 95 | `?Initialize@CUwfRegDevice@@QEAAJXZ` | `0x15170` | 31 | UnwindData |  |
| 97 | `?Initialize@CUwfVolumeDevice@@QEAAJXZ` | `0x151A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `?InitializeWithNoPermissions@CDevice@@QEAAJPEBG@Z` | `0x151C0` | 163 | UnwindData |  |
| 133 | `?SendIOCTL@CDevice@@QEAAJKPEAXK0KPEAK@Z` | `0x15C70` | 129 | UnwindData |  |
| 240 | `?get_RomModeDisposition@CUwfVolumeDevice@@QEAAJPEAW4_UWFVOL_ROM_MODE_DISPOSITION@@@Z` | `0x15F00` | 69 | UnwindData |  |
| 257 | `?set_HORMEnabled@CUwfVolumeDevice@@QEAAJ_N@Z` | `0x15F50` | 52 | UnwindData |  |
| 261 | `?set_OverlayCriticalThreshold@CUwfVolumeDevice@@QEAAJK@Z` | `0x15F90` | 49 | UnwindData |  |
| 270 | `?set_OverlayWarningThreshold@CUwfVolumeDevice@@QEAAJK@Z` | `0x15FD0` | 49 | UnwindData |  |
| 283 | `?set_RomModeDisposition@CUwfVolumeDevice@@QEAAJW4_UWFVOL_ROM_MODE_DISPOSITION@@@Z` | `0x16010` | 49 | UnwindData |  |
| 3 | `??0CUwfManagement@@QEAA@XZ` | `0x16050` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `??1CUwfManagement@@UEAA@XZ` | `0x16130` | 78 | UnwindData |  |
| 30 | `?Close@CUwfManagement@@QEAAXXZ` | `0x16350` | 67 | UnwindData |  |
| 34 | `?CommitFile@CUwfManagement@@QEAAJPEBG0@Z` | `0x163A0` | 1,142 | UnwindData |  |
| 35 | `?CommitFileDeletion@CUwfManagement@@QEAAJPEBG00@Z` | `0x16820` | 1,093 | UnwindData |  |
| 36 | `?CommitRegistry@CUwfManagement@@QEAAJ_NPEBG1@Z` | `0x16C70` | 681 | UnwindData |  |
| 37 | `?CommitRegistryDeletion@CUwfManagement@@QEAAJ_NPEBG1@Z` | `0x16F20` | 677 | UnwindData |  |
| 67 | `?Finalize@CUwfManagement@@QEAAJXZ` | `0x171D0` | 202 | UnwindData |  |
| 82 | `?GetSystemShutdownState@CUwfManagement@@QEAAJPEA_N@Z` | `0x17A10` | 174 | UnwindData |  |
| 92 | `?Initialize@CUwfManagement@@QEAAJXZ` | `0x17AD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `?Initialize@CUwfManagement@@QEAAJ_N@Z` | `0x17AE0` | 176 | UnwindData |  |
| 108 | `?LookupShutdownPrivilegeInCurThreadToken@CUwfManagement@@QEAAJAEA_N@Z` | `0x17C40` | 416 | UnwindData |  |
| 132 | `?ResetUwfSettings@CUwfManagement@@QEAAJXZ` | `0x17E50` | 77 | UnwindData |  |
| 142 | `?ShutdownSystem@CUwfManagement@@QEAAJ_N@Z` | `0x17FF0` | 388 | UnwindData |  |
| 212 | `?get_HORMEnabled@CUwfManagement@@QEAAJPEA_N@Z` | `0x18450` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | `?get_OverlayCriticalThreshold@CUwfManagement@@QEAAJPEAK@Z` | `0x187D0` | 35 | UnwindData |  |
| 218 | `?get_OverlayFlags@CUwfManagement@@QEAAJ_NPEAK@Z` | `0x18800` | 55 | UnwindData |  |
| 220 | `?get_OverlayInformation@CUwfManagement@@QEAAJPEBGPEAU_UWFVOL_OVERLAY_DATA_OUTPUT@@PEAK2@Z` | `0x18840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 221 | `?get_OverlayMaximumSize@CUwfManagement@@QEAAJ_NPEAK@Z` | `0x18850` | 55 | UnwindData |  |
| 223 | `?get_OverlayType@CUwfManagement@@QEAAJ_NPEAW4_UWF_CONFIG_OVERLAY_TYPE@@@Z` | `0x18890` | 55 | UnwindData |  |
| 226 | `?get_OverlayWarningThreshold@CUwfManagement@@QEAAJPEAK@Z` | `0x188D0` | 35 | UnwindData |  |
| 236 | `?get_ResetPersistentOverlay@CUwfManagement@@QEAAJPEAK@Z` | `0x18900` | 170 | UnwindData |  |
| 237 | `?get_ResetPersistentStateSavedMode@CUwfManagement@@QEAAJ_NPEAK@Z` | `0x189B0` | 55 | UnwindData |  |
| 239 | `?get_RomModeDisposition@CUwfManagement@@QEAAJPEAW4_UWFVOL_ROM_MODE_DISPOSITION@@@Z` | `0x189F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 247 | `?get_UwfConfiguration@CUwfManagement@@QEAAJPEAPEAVCUwfConfiguration@@@Z` | `0x18A00` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 256 | `?set_HORMEnabled@CUwfManagement@@QEAAJ_N@Z` | `0x18A20` | 742 | UnwindData |  |
| 260 | `?set_OverlayCriticalThreshold@CUwfManagement@@QEAAJK@Z` | `0x18D10` | 64 | UnwindData |  |
| 262 | `?set_OverlayFlags@CUwfManagement@@QEAAJK@Z` | `0x18D60` | 183 | UnwindData |  |
| 264 | `?set_OverlayMaximumSize@CUwfManagement@@QEAAJK@Z` | `0x18E20` | 236 | UnwindData |  |
| 266 | `?set_OverlayType@CUwfManagement@@QEAAJW4_UWF_CONFIG_OVERLAY_TYPE@@@Z` | `0x18F20` | 340 | UnwindData |  |
| 269 | `?set_OverlayWarningThreshold@CUwfManagement@@QEAAJK@Z` | `0x19080` | 64 | UnwindData |  |
| 279 | `?set_ResetPersistentOverlay@CUwfManagement@@QEAAJK@Z` | `0x190D0` | 325 | UnwindData |  |
| 280 | `?set_ResetPersistentStateSavedMode@CUwfManagement@@QEAAJK@Z` | `0x19220` | 183 | UnwindData |  |
| 282 | `?set_RomModeDisposition@CUwfManagement@@QEAAJW4_UWFVOL_ROM_MODE_DISPOSITION@@@Z` | `0x192E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 284 | `?set_ServicingModeEnabled@CUwfManagement@@QEAAJ_N0@Z` | `0x192F0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `?Begin@CUwfProvider@@QEAAJXZ` | `0x193C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `?Begin@CUwfProvider@@QEAAJ_N@Z` | `0x193D0` | 61 | UnwindData |  |
| 68 | `?Finalize@CUwfProvider@@QEAAJXZ` | `0x19420` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `?GetConfiguration@CUwfProvider@@QEAAPEAVCUwfConfiguration@@XZ` | `0x19440` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `?GetManagement@CUwfProvider@@QEAAPEAVCUwfManagement@@XZ` | `0x19450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `?GetStaticConfiguration@CUwfProvider@@QEAAJ_NPEAPEAVCUwfStaticConfiguration@@@Z` | `0x19460` | 119 | UnwindData |  |
| 84 | `?GetUwfProvider@CUwfProvider@@SAPEAV1@XZ` | `0x194E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `?LOCK@CUwfProvider@@QEAAXXZ` | `0x194F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `?UNLOCK@CUwfProvider@@QEAAXXZ` | `0x19510` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 148 | `UwfCfgAddFileExclusion` | `0x195E0` | 145 | UnwindData |  |
| 149 | `UwfCfgAddRegExclusion` | `0x19680` | 137 | UnwindData |  |
| 150 | `UwfCfgAddVolume` | `0x19710` | 278 | UnwindData |  |
| 151 | `UwfCfgCommitFile` | `0x19830` | 217 | UnwindData |  |
| 152 | `UwfCfgCommitFileDeletion` | `0x19910` | 288 | UnwindData |  |
| 153 | `UwfCfgCommitRegistry` | `0x19A40` | 186 | UnwindData |  |
| 154 | `UwfCfgCommitRegistryDeletion` | `0x19B00` | 186 | UnwindData |  |
| 155 | `UwfCfgDoesFileExclusionExist` | `0x19BC0` | 159 | UnwindData |  |
| 156 | `UwfCfgDoesRegExclusionExist` | `0x19C70` | 141 | UnwindData |  |
| 157 | `UwfCfgDoesVolumeExist` | `0x19D10` | 123 | UnwindData |  |
| 158 | `UwfCfgGetCriticalThreshold` | `0x19DA0` | 148 | UnwindData |  |
| 159 | `UwfCfgGetDriveLetter` | `0x19E40` | 159 | UnwindData |  |
| 160 | `UwfCfgGetFileExclusions` | `0x19EF0` | 296 | UnwindData |  |
| 161 | `UwfCfgGetFilterEnabled` | `0x1A020` | 118 | UnwindData |  |
| 162 | `UwfCfgGetHormEnabled` | `0x1A0A0` | 124 | UnwindData |  |
| 163 | `UwfCfgGetOverlayCommitState` | `0x1A130` | 149 | UnwindData |  |
| 164 | `UwfCfgGetOverlayFlags` | `0x1A1D0` | 146 | UnwindData |  |
| 165 | `UwfCfgGetOverlayInformation` | `0x1A270` | 660 | UnwindData |  |
| 166 | `UwfCfgGetOverlayMaximumSize` | `0x1A510` | 146 | UnwindData |  |
| 167 | `UwfCfgGetOverlayType` | `0x1A5B0` | 146 | UnwindData |  |
| 168 | `UwfCfgGetPersistDomainSecretKey` | `0x1A650` | 141 | UnwindData |  |
| 169 | `UwfCfgGetPersistTSCAL` | `0x1A6F0` | 160 | UnwindData |  |
| 170 | `UwfCfgGetRegExclusions` | `0x1A7A0` | 276 | UnwindData |  |
| 171 | `UwfCfgGetResetPersistentOverlay` | `0x1A8C0` | 148 | UnwindData |  |
| 172 | `UwfCfgGetResetPersistentOverlaySavedMode` | `0x1A960` | 164 | UnwindData |  |
| 173 | `UwfCfgGetServicingModeEnabled` | `0x1AA10` | 141 | UnwindData |  |
| 174 | `UwfCfgGetShutdownPending` | `0x1AAB0` | 148 | UnwindData |  |
| 175 | `UwfCfgGetVolumeBindByDriveLetter` | `0x1AB50` | 171 | UnwindData |  |
| 176 | `UwfCfgGetVolumeProtected` | `0x1AC10` | 154 | UnwindData |  |
| 177 | `UwfCfgGetVolumeSwapfileSize` | `0x1ACB0` | 154 | UnwindData |  |
| 178 | `UwfCfgGetVolumes` | `0x1AD50` | 593 | UnwindData |  |
| 179 | `UwfCfgGetWarningThreshold` | `0x1AFB0` | 148 | UnwindData |  |
| 180 | `UwfCfgRemoveFileExclusion` | `0x1B050` | 145 | UnwindData |  |
| 181 | `UwfCfgRemoveRegExclusion` | `0x1B0F0` | 137 | UnwindData |  |
| 182 | `UwfCfgRemoveVolume` | `0x1B180` | 263 | UnwindData |  |
| 183 | `UwfCfgResetSettings` | `0x1B290` | 109 | UnwindData |  |
| 184 | `UwfCfgRestartSystem` | `0x1B310` | 111 | UnwindData |  |
| 185 | `UwfCfgSetCriticalThreshold` | `0x1B390` | 122 | UnwindData |  |
| 186 | `UwfCfgSetFilterEnabled` | `0x1B410` | 904 | UnwindData |  |
| 187 | `UwfCfgSetHormEnabled` | `0x1B7A0` | 124 | UnwindData |  |
| 188 | `UwfCfgSetOverlayCommitState` | `0x1B830` | 130 | UnwindData |  |
| 189 | `UwfCfgSetOverlayFlags` | `0x1B8C0` | 285 | UnwindData |  |
| 190 | `UwfCfgSetOverlayMaximumSize` | `0x1B9F0` | 105 | UnwindData |  |
| 191 | `UwfCfgSetOverlayType` | `0x1BA60` | 105 | UnwindData |  |
| 192 | `UwfCfgSetPersistDomainSecretKey` | `0x1BAD0` | 116 | UnwindData |  |
| 193 | `UwfCfgSetPersistTSCAL` | `0x1BB50` | 116 | UnwindData |  |
| 194 | `UwfCfgSetResetPersistentOverlay` | `0x1BBD0` | 161 | UnwindData |  |
| 195 | `UwfCfgSetResetPersistentOverlaySavedMode` | `0x1BC80` | 149 | UnwindData |  |
| 196 | `UwfCfgSetServicingModeEnabled` | `0x1BD20` | 518 | UnwindData |  |
| 197 | `UwfCfgSetVolumeBindByDriveLetter` | `0x1BF30` | 142 | UnwindData |  |
| 198 | `UwfCfgSetVolumeProtected` | `0x1BFD0` | 140 | UnwindData |  |
| 199 | `UwfCfgSetVolumeSwapfileSize` | `0x1C070` | 757 | UnwindData |  |
| 200 | `UwfCfgSetWarningThreshold` | `0x1C370` | 122 | UnwindData |  |
| 201 | `UwfCfgShutdownSystem` | `0x1C3F0` | 111 | UnwindData |  |

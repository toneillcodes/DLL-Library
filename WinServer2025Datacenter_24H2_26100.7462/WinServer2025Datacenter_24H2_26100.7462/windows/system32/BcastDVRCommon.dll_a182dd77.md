# Binary Specification: BcastDVRCommon.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\BcastDVRCommon.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a182dd772a99cc9b78702476e8608486c3ed6f8a246c2a1bcedb1a4e9355313f`
* **Total Exported Functions:** 88

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 85 | `GetBroadcastSharedMemoryReader` | `0x9670` | 252 | UnwindData |  |
| 86 | `GetBroadcastSharedMemoryWriter` | `0x9780` | 252 | UnwindData |  |
| 87 | `GetPreviewSharedMemoryReader` | `0x9890` | 252 | UnwindData |  |
| 88 | `GetPreviewSharedMemoryWriter` | `0x99A0` | 252 | UnwindData |  |
| 11 | `CreateCallerManagerInstance` | `0xB380` | 194 | UnwindData |  |
| 12 | `CreateCallerManagerInstanceForAppId` | `0xB450` | 195 | UnwindData |  |
| 16 | `FireCallerManagerEvent` | `0xB520` | 146 | UnwindData |  |
| 17 | `FireCallerManagerEventForAppId` | `0xB5C0` | 147 | UnwindData |  |
| 4 | `ActiveMetadataManagerInstances` | `0xE420` | 64 | UnwindData |  |
| 13 | `CreateMetadataManagerInstance` | `0xFA20` | 131 | UnwindData |  |
| 14 | `CreateMetadataManagerInstanceForAppId` | `0xFAB0` | 152 | UnwindData |  |
| 15 | `CreateMetadataManagerInstanceFromJson` | `0xFB50` | 126 | UnwindData |  |
| 8 | `?CleanupObsoletePlugIns@PlugInUtility@Internal@Capture@Media@Windows@@YAJPEAUHKEY__@@@Z` | `0x177E0` | 737 | UnwindData |  |
| 18 | `?FreeBroadcastSebEventIds@PlugInUtility@Internal@Capture@Media@Windows@@YAXPEAPEAU_GUID@@@Z` | `0x17AD0` | 74 | UnwindData |  |
| 21 | `?GetBroadcastSebEventIds@PlugInUtility@Internal@Capture@Media@Windows@@YAJPEAKPEAPEAU_GUID@@@Z` | `0x17B20` | 291 | UnwindData |  |
| 22 | `?GetCallersPlugInInfo@PlugInUtility@Internal@Capture@Media@Windows@@YAJPEAUHKEY__@@AEBU_GUID@@PEAVString@25@2@Z` | `0x17C50` | 230 | UnwindData |  |
| 23 | `?GetCallersSebEventId@PlugInUtility@Internal@Capture@Media@Windows@@YAJPEAU_GUID@@@Z` | `0x17D40` | 739 | UnwindData |  |
| 24 | `?GetDefaultPlugIn@PlugInUtility@Internal@Capture@Media@Windows@@YAJPEAUHKEY__@@PEAU_GUID@@@Z` | `0x18030` | 334 | UnwindData |  |
| 41 | `?GetPlugInInfo@PlugInUtility@Internal@Capture@Media@Windows@@YAJPEAUHKEY__@@AEBU_GUID@@PEAVString@25@22@Z` | `0x18270` | 925 | UnwindData |  |
| 42 | `?GetPlugInPackageFullName@PlugInUtility@Internal@Capture@Media@Windows@@YAJAEBU_GUID@@PEAVString@25@@Z` | `0x18620` | 264 | UnwindData |  |
| 82 | `?RegisterCallingPlugIn@PlugInUtility@Internal@Capture@Media@Windows@@YAJPEAUHKEY__@@PEAUHSTRING__@@1AEBU_GUID@@@Z` | `0x187E0` | 1,384 | UnwindData |  |
| 83 | `?SetDefaultPlugIn@PlugInUtility@Internal@Capture@Media@Windows@@YAJPEAUHKEY__@@AEBU_GUID@@@Z` | `0x19920` | 286 | UnwindData |  |
| 1 | `??0BcastDVR_OutputDebug@@QEAA@PEBD@Z` | `0x1E180` | 282 | UnwindData |  |
| 25 | `?GetErrorHistoryCount@BcastDVRLogProviderBase@@SAKXZ` | `0x1F030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `?GetFormattedErrorHistory@BcastDVRLogProviderBase@@SAKPEAVString@Internal@Windows@@@Z` | `0x1F040` | 632 | UnwindData |  |
| 46 | `?Initialize@BcastDVR_OutputDebug@@SAXPEBGW4BcastDVR_OutputDebug_TraceToFileType@@0@Z` | `0x1F2C0` | 704 | UnwindData |  |
| 56 | `?LogError@BcastDVRLogProviderBase@@SAXJPEBD0H_N@Z` | `0x1F770` | 433 | UnwindData |  |
| 57 | `?LogErrorEx@BcastDVRLogProviderBase@@SAXJPEBD0H00_N@Z` | `0x1F930` | 591 | UnwindData |  |
| 59 | `?MostRecentErrorInHistory@BcastDVRLogProviderBase@@SAJXZ` | `0x1FC20` | 98 | UnwindData |  |
| 60 | `?OutputString@BcastDVR_OutputDebug@@QEAAXXZ` | `0x1FC90` | 356 | UnwindData |  |
| 62 | `?PrintHRESULT@BcastDVR_OutputDebug@@QEAAXJ@Z` | `0x1FE00` | 64 | UnwindData |  |
| 63 | `?PrintType@BcastDVR_OutputDebug@@QEAAXPEBD0@Z` | `0x1FE50` | 69 | UnwindData |  |
| 64 | `?PrintType@BcastDVR_OutputDebug@@QEAAXPEBDE@Z` | `0x1FEA0` | 79 | UnwindData |  |
| 65 | `?PrintType@BcastDVR_OutputDebug@@QEAAXPEBDH@Z` | `0x1FF00` | 69 | UnwindData |  |
| 66 | `?PrintType@BcastDVR_OutputDebug@@QEAAXPEBDI@Z` | `0x1FF50` | 69 | UnwindData |  |
| 67 | `?PrintType@BcastDVR_OutputDebug@@QEAAXPEBDK@Z` | `0x1FF50` | 69 | UnwindData |  |
| 68 | `?PrintType@BcastDVR_OutputDebug@@QEAAXPEBDN@Z` | `0x1FFA0` | 71 | UnwindData |  |
| 69 | `?PrintType@BcastDVR_OutputDebug@@QEAAXPEBDPEAX@Z` | `0x1FFF0` | 69 | UnwindData |  |
| 70 | `?PrintType@BcastDVR_OutputDebug@@QEAAXPEBDPEBG@Z` | `0x20040` | 69 | UnwindData |  |
| 71 | `?PrintType@BcastDVR_OutputDebug@@QEAAXPEBD_K@Z` | `0x20090` | 69 | UnwindData |  |
| 72 | `?Printf@BcastDVRLogProviderBase@@SAX_N0PEBD1HPEBGZZ` | `0x200E0` | 778 | UnwindData |  |
| 84 | `?Uninitialize@BcastDVR_OutputDebug@@SAXXZ` | `0x20720` | 138 | UnwindData |  |
| 2 | `??0ImpersonateHelper@Internal@Capture@Media@Windows@@QEAA@XZ` | `0x211F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??1ImpersonateHelper@Internal@Capture@Media@Windows@@QEAA@XZ` | `0x21200` | 27 | UnwindData |  |
| 44 | `?ImpersonateDefaultUser@ImpersonateHelper@Internal@Capture@Media@Windows@@QEAAJXZ` | `0x21230` | 226 | UnwindData |  |
| 45 | `?ImpersonateUser@ImpersonateHelper@Internal@Capture@Media@Windows@@QEAAJPEAUIUser@System@5@@Z` | `0x21320` | 586 | UnwindData |  |
| 5 | `?AppendPath@EnvironmentManager@Internal@Capture@Media@Windows@@YAJAEBVString@25@0PEAV625@@Z` | `0x21570` | 467 | UnwindData |  |
| 19 | `?GetBroadcastPlugInRegistryPathFromSebEventId@EnvironmentManager@Internal@Capture@Media@Windows@@YAJAEBU_GUID@@PEAVString@25@@Z` | `0x21750` | 347 | UnwindData |  |
| 20 | `?GetBroadcastPlugInRegistryPathFromSebEventIdString@EnvironmentManager@Internal@Capture@Media@Windows@@YAJPEBGPEAVString@25@@Z` | `0x218C0` | 248 | UnwindData |  |
| 39 | `?GetKnownFolderSubFolder@EnvironmentManager@Internal@Capture@Media@Windows@@YAJAEBU_GUID@@PEBGPEAVString@25@@Z` | `0x219C0` | 347 | UnwindData |  |
| 43 | `?GetUserGameDVRConfigFolderPath@EnvironmentManager@Internal@Capture@Media@Windows@@YAJPEAVString@25@PEBG@Z` | `0x21B30` | 548 | UnwindData |  |
| 6 | `?CalcPreviewVideoBufferDataSize@GameDVRUtility@Internal@Capture@Media@Windows@@YAJKKPEAK@Z` | `0x225F0` | 120 | UnwindData |  |
| 7 | `?CalcPreviewVideoFrameDataSize@GameDVRUtility@Internal@Capture@Media@Windows@@YAJKKPEAK@Z` | `0x22670` | 101 | UnwindData |  |
| 9 | `?CloseDuplicatedHandle@GameDVRUtility@Internal@Capture@Media@Windows@@YAJKPEAX@Z` | `0x226E0` | 270 | UnwindData |  |
| 10 | `?CloseDuplicatedHandles@GameDVRUtility@Internal@Capture@Media@Windows@@YAJKKQEAPEAX@Z` | `0x22890` | 330 | UnwindData |  |
| 27 | `?GetGuidFromGuidString@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEBGPEAU_GUID@@@Z` | `0x22BB0` | 65 | UnwindData |  |
| 28 | `?GetGuidStringFromGuid@GameDVRUtility@Internal@Capture@Media@Windows@@YAJAEBU_GUID@@_NPEAVString@25@@Z` | `0x22C00` | 362 | UnwindData |  |
| 29 | `?GetHKeyCurrentUserForDefaultUser@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAPEAUHKEY__@@@Z` | `0x22D70` | 261 | UnwindData |  |
| 30 | `?GetHKeyCurrentUserForIUser@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAUIUser@System@5@PEAPEAUHKEY__@@@Z` | `0x22E80` | 287 | UnwindData |  |
| 31 | `?GetIUserSID@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAUIUser@System@5@PEAVString@25@@Z` | `0x23330` | 169 | UnwindData |  |
| 32 | `?GetJsonArray@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAU?$IMap@PEAUHSTRING__@@PEAUIJsonValue@Json@Data@Windows@@@Collections@Foundation@5@PEAUHSTRING__@@PEAEPEAPEAU?$IVector@PEAUIJsonValue@Json@Data@Windows@@@785@@Z` | `0x233E0` | 956 | UnwindData |  |
| 33 | `?GetJsonBoolean@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAU?$IMap@PEAUHSTRING__@@PEAUIJsonValue@Json@Data@Windows@@@Collections@Foundation@5@PEAUHSTRING__@@PEAE2@Z` | `0x237B0` | 630 | UnwindData |  |
| 34 | `?GetJsonDateTime@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAU?$IMap@PEAUHSTRING__@@PEAUIJsonValue@Json@Data@Windows@@@Collections@Foundation@5@PEAUHSTRING__@@PEAEPEAUDateTime@85@@Z` | `0x23A30` | 1,025 | UnwindData |  |
| 35 | `?GetJsonDouble@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAU?$IMap@PEAUHSTRING__@@PEAUIJsonValue@Json@Data@Windows@@@Collections@Foundation@5@PEAUHSTRING__@@PEAEPEAN@Z` | `0x23E40` | 630 | UnwindData |  |
| 36 | `?GetJsonGuid@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAU?$IMap@PEAUHSTRING__@@PEAUIJsonValue@Json@Data@Windows@@@Collections@Foundation@5@PEAUHSTRING__@@PEAEPEAU_GUID@@@Z` | `0x240C0` | 948 | UnwindData |  |
| 37 | `?GetJsonNumber@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAU?$IMap@PEAUHSTRING__@@PEAUIJsonValue@Json@Data@Windows@@@Collections@Foundation@5@PEAUHSTRING__@@PEAEPEA_J@Z` | `0x24480` | 651 | UnwindData |  |
| 38 | `?GetJsonString@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAU?$IMap@PEAUHSTRING__@@PEAUIJsonValue@Json@Data@Windows@@@Collections@Foundation@5@PEAUHSTRING__@@PEAEPEAVString@25@@Z` | `0x24720` | 692 | UnwindData |  |
| 40 | `?GetOSVersionString@GameDVRUtility@Internal@Capture@Media@Windows@@YAXPEAVString@25@@Z` | `0x249E0` | 386 | UnwindData |  |
| 47 | `?InsertJsonArray@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAU?$IMap@PEAUHSTRING__@@PEAUIJsonValue@Json@Data@Windows@@@Collections@Foundation@5@PEAUHSTRING__@@PEAPEAU?$IVector@PEAUIJsonValue@Json@Data@Windows@@@785@@Z` | `0x24B70` | 652 | UnwindData |  |
| 48 | `?InsertJsonBoolean@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAUIJsonValueStatics@Json@Data@5@PEAU?$IMap@PEAUHSTRING__@@PEAUIJsonValue@Json@Data@Windows@@@Collections@Foundation@5@PEAUHSTRING__@@E@Z` | `0x24E10` | 268 | UnwindData |  |
| 49 | `?InsertJsonDateTime@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAUIJsonValueStatics@Json@Data@5@PEAU?$IMap@PEAUHSTRING__@@PEAUIJsonValue@Json@Data@Windows@@@Collections@Foundation@5@PEAUHSTRING__@@UDateTime@Foundation@5@@Z` | `0x24F30` | 396 | UnwindData |  |
| 50 | `?InsertJsonDouble@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAUIJsonValueStatics@Json@Data@5@PEAU?$IMap@PEAUHSTRING__@@PEAUIJsonValue@Json@Data@Windows@@@Collections@Foundation@5@PEAUHSTRING__@@N@Z` | `0x250D0` | 268 | UnwindData |  |
| 51 | `?InsertJsonGuid@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAUIJsonValueStatics@Json@Data@5@PEAU?$IMap@PEAUHSTRING__@@PEAUIJsonValue@Json@Data@Windows@@@Collections@Foundation@5@PEAUHSTRING__@@U_GUID@@@Z` | `0x251F0` | 300 | UnwindData |  |
| 52 | `?InsertJsonNumber@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAUIJsonValueStatics@Json@Data@5@PEAU?$IMap@PEAUHSTRING__@@PEAUIJsonValue@Json@Data@Windows@@@Collections@Foundation@5@PEAUHSTRING__@@_J@Z` | `0x25330` | 273 | UnwindData |  |
| 53 | `?InsertJsonObject@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAU?$IMap@PEAUHSTRING__@@PEAUIJsonValue@Json@Data@Windows@@@Collections@Foundation@5@PEAUHSTRING__@@PEAPEAUIJsonObject@Json@Data@5@@Z` | `0x25450` | 411 | UnwindData |  |
| 54 | `?InsertJsonString@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAUIJsonValueStatics@Json@Data@5@PEAU?$IMap@PEAUHSTRING__@@PEAUIJsonValue@Json@Data@Windows@@@Collections@Foundation@5@PEAUHSTRING__@@2@Z` | `0x25600` | 268 | UnwindData |  |
| 55 | `?InsertNamedJsonEnumBitfields@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAUIJsonValueStatics@Json@Data@5@PEAU?$IMap@PEAUHSTRING__@@PEAUIJsonValue@Json@Data@Windows@@@Collections@Foundation@5@PEAUHSTRING__@@_KPEBQEBGH@Z` | `0x25720` | 450 | UnwindData |  |
| 58 | `?MapConstantToString@GameDVRUtility@Internal@Capture@Media@Windows@@YAPEBGQEAPEBGKKKK@Z` | `0x25920` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?PrintGuid@GameDVRUtility@Internal@Capture@Media@Windows@@YAJU_GUID@@PEAVString@25@@Z` | `0x25A50` | 340 | UnwindData |  |
| 73 | `?RecreateStorageFile@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAUIStorageFile@Storage@5@PEAPEAU675@@Z` | `0x25F30` | 738 | UnwindData |  |
| 74 | `?RegGetDwordValue@GameDVRUtility@Internal@Capture@Media@Windows@@YAXPEAUHKEY__@@PEBG1KPEAK@Z` | `0x26220` | 87 | UnwindData |  |
| 75 | `?RegGetQwordValue@GameDVRUtility@Internal@Capture@Media@Windows@@YAXPEAUHKEY__@@PEBG1_KPEA_K@Z` | `0x26280` | 89 | UnwindData |  |
| 76 | `?RegGetStringValue@GameDVRUtility@Internal@Capture@Media@Windows@@YAXPEAUHKEY__@@PEBG1PEAVString@25@@Z` | `0x262E0` | 129 | UnwindData |  |
| 77 | `?RegSetBinaryValue@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAUHKEY__@@PEBG1PEBEK@Z` | `0x26370` | 269 | UnwindData |  |
| 78 | `?RegSetDwordValue@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAUHKEY__@@PEBG1K@Z` | `0x26490` | 263 | UnwindData |  |
| 79 | `?RegSetQwordValue@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAUHKEY__@@PEBG1_K@Z` | `0x265A0` | 266 | UnwindData |  |
| 80 | `?RegSetStringValue@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAUHKEY__@@PEBG1PEAVString@25@@Z` | `0x266B0` | 308 | UnwindData |  |
| 81 | `?RegSetStringValue@GameDVRUtility@Internal@Capture@Media@Windows@@YAJPEAUHKEY__@@PEBGPEBD2@Z` | `0x267F0` | 402 | UnwindData |  |

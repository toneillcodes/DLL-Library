# Binary Specification: UserDataPlatformHelperUtil.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\UserDataPlatformHelperUtil.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `71a241fed229fb2010f0e3462c49eb8900577f6dc576b2f45d6d5e9fd27688b1`
* **Total Exported Functions:** 68

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 6 | `??1Deserializer@Comms@@QEAA@XZ` | `0x27A0` | 82 | UnwindData |  |
| 17 | `?DeserializeObject@Comms@@YA_NAEAVDeserializer@1@AEAV?$basic_string@GU?$char_traits@G@utl@@V?$allocator@G@2@@utl@@@Z` | `0x2800` | 178 | UnwindData |  |
| 18 | `?DeserializeObject@Comms@@YA_NAEAVDeserializer@1@AEAV?$vector@EV?$allocator@E@utl@@@utl@@@Z` | `0x28C0` | 171 | UnwindData |  |
| 21 | `?GetBuffer@Deserializer@Comms@@QEAAPEAX_K@Z` | `0x2980` | 153 | UnwindData |  |
| 22 | `?GetBuffer@SerializeBuffer@Comms@@QEAAXAEAV?$vector@EV?$allocator@E@utl@@@utl@@@Z` | `0x2A20` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `?GetBuffer@SerializeBuffer@Comms@@QEBAPEBV?$vector@EV?$allocator@E@utl@@@utl@@XZ` | `0x2A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `?GetTotal@CalculateSize@Comms@@QEBA_KXZ` | `0x2A80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `?ReleaseBuffer@Deserializer@Comms@@QEAAXPEBX@Z` | `0x2A90` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `?SerializeObject@Comms@@YAXAEAVSerializeBase@1@AEBV?$basic_string@GU?$char_traits@G@utl@@V?$allocator@G@2@@utl@@@Z` | `0x2AC0` | 111 | UnwindData |  |
| 37 | `?SerializeObject@Comms@@YAXAEAVSerializeBase@1@AEBV?$vector@EV?$allocator@E@utl@@@utl@@@Z` | `0x2B40` | 102 | UnwindData |  |
| 2 | `??0Deserializer@Comms@@QEAA@PEBE0_N1@Z` | `0x2F40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `?CopyBytesOut@Deserializer@Comms@@QEAA_NPEAX_KAEBVtype_info@@@Z` | `0x2F70` | 236 | UnwindData |  |
| 13 | `?DeserializeObject@Comms@@YA_NAEAVDeserializer@1@AEAPEAD@Z` | `0x3070` | 168 | UnwindData |  |
| 14 | `?DeserializeObject@Comms@@YA_NAEAVDeserializer@1@AEAPEAG@Z` | `0x3120` | 178 | UnwindData |  |
| 15 | `?DeserializeObject@Comms@@YA_NAEAVDeserializer@1@AEAPEBD@Z` | `0x31E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `?DeserializeObject@Comms@@YA_NAEAVDeserializer@1@AEAPEBG@Z` | `0x31F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `?DeserializeObject@Comms@@YA_NAEAVDeserializer@1@AEAVNullType@detail@1@@Z` | `0x3200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `?DeserializeObject@Comms@@YA_NAEAVDeserializer@1@AEBVNullType@detail@1@@Z` | `0x3200` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0RpcClient@Comms@@QEAA@XZ` | `0x3210` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0SecureRpcClient@Comms@@QEAA@XZ` | `0x3230` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??1RpcClient@Comms@@QEAA@XZ` | `0x3300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??1SecureRpcClient@Comms@@UEAA@XZ` | `0x3310` | 51 | UnwindData |  |
| 30 | `?InitializeBinding@RpcClient@Comms@@QEAAJPEBGAEAPEAX@Z` | `0x33F0` | 188 | UnwindData |  |
| 31 | `IsActiveDebugger` | `0x34C0` | 48 | UnwindData |  |
| 43 | `?_InitializeSecureRpcBinding@SecureRpcClient@Comms@@IEAAJPEBG0@Z` | `0x3500` | 613 | UnwindData |  |
| 1 | `??0CalculateSize@Comms@@QEAA@_N0@Z` | `0x3970` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `??0SerializeBuffer@Comms@@QEAA@AEBVCalculateSize@1@_N1@Z` | `0x39A0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `?CopyBytesIn@CalculateSize@Comms@@UEAAXPEBX_KAEBVtype_info@@@Z` | `0x3A70` | 57 | UnwindData |  |
| 10 | `?CopyBytesIn@SerializeBuffer@Comms@@UEAAXPEBX_KAEBVtype_info@@@Z` | `0x3AB0` | 342 | UnwindData |  |
| 29 | `?Initialize@SerializeBuffer@Comms@@QEAA_NXZ` | `0x3C10` | 56 | UnwindData |  |
| 38 | `?SerializeObject@Comms@@YAXAEAVSerializeBase@1@AEBVNullType@detail@1@@Z` | `0x3C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `?SerializeObject@Comms@@YAXAEAVSerializeBase@1@PEBD@Z` | `0x3C60` | 109 | UnwindData |  |
| 40 | `?SerializeObject@Comms@@YAXAEAVSerializeBase@1@PEBG@Z` | `0x3CE0` | 113 | UnwindData |  |
| 47 | `DllCanUnloadNow` | `0x4AB0` | 42 | UnwindData |  |
| 48 | `DllGetClassObject` | `0x4AE0` | 302 | UnwindData |  |
| 12 | `CreateKnownFolderPath` | `0x4DF0` | 368 | UnwindData |  |
| 26 | `GetTempFileNameWithExt` | `0x4F70` | 989 | UnwindData |  |
| 24 | `GetRpcClientThreadToken` | `0x5490` | 185 | UnwindData |  |
| 50 | `GenerateUserModeServiceName` | `0x5890` | 247 | UnwindData |  |
| 52 | `GetCombinedTransientObjectSecurityDescriptor` | `0x5990` | 630 | UnwindData |  |
| 56 | `GetQueryProcessHandle` | `0x5C10` | 122 | UnwindData |  |
| 57 | `GetUserContextFromHandle` | `0x5C90` | 65 | UnwindData |  |
| 58 | `GetUserTokenFromContext` | `0x5CE0` | 70 | UnwindData |  |
| 59 | `IsCommsSystemService` | `0x5D30` | 157 | UnwindData |  |
| 62 | `RunServicesInProc` | `0x5DE0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `StartAndWaitForService` | `0x5E00` | 46 | UnwindData |  |
| 65 | `StartAndWaitForServiceForUser` | `0x5E40` | 652 | UnwindData |  |
| 66 | `StopAndWaitForFullyNamedService` | `0x60E0` | 535 | UnwindData |  |
| 67 | `StopAndWaitForService` | `0x6300` | 111 | UnwindData |  |
| 25 | `GetSupportedImageFileExtensions` | `0x6790` | 1,504 | UnwindData |  |
| 32 | `IsImageExtension` | `0x6D80` | 404 | UnwindData |  |
| 34 | `ResizeImageBySizeInMemory` | `0x7390` | 1,123 | UnwindData |  |
| 35 | `ResizeImageBySizeToStream` | `0x7800` | 388 | UnwindData |  |
| 27 | `GetThreadIOPriority` | `0x7B10` | 112 | UnwindData |  |
| 41 | `SetPoolThreadBasePriority` | `0x7B90` | 139 | UnwindData |  |
| 42 | `SetThreadIOPriority` | `0x7C30` | 114 | UnwindData |  |
| 44 | `ConvertHtmlStringToPlainTextStringOneCore` | `0x7FD0` | 298 | UnwindData |  |
| 45 | `ConvertPlainTextStringToHtmlStringOneCore` | `0x8100` | 24 | UnwindData |  |
| 61 | `PrependHtmlOneCore` | `0x8120` | 83 | UnwindData |  |
| 68 | `UT_UninitializeTrident` | `0x8180` | 132 | UnwindData |  |
| 51 | `GetCalendarColors` | `0x8210` | 91 | UnwindData |  |
| 55 | `GetNextNewCalendarColor` | `0x8280` | 411 | UnwindData |  |
| 53 | `GetContentTypeFromFilePath` | `0x8C30` | 39 | UnwindData |  |
| 54 | `GetFileExtensionFromContentType` | `0x8C60` | 39 | UnwindData |  |
| 46 | `DefaultMakeHresultFromJetError` | `0x9030` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `FreeEnumColumn` | `0x9060` | 247 | UnwindData |  |
| 60 | `JetReallocMethod` | `0x9160` | 126 | UnwindData |  |
| 63 | `SetCommsServiceJetGlobalSystemParameters` | `0x91F0` | 94 | UnwindData |  |

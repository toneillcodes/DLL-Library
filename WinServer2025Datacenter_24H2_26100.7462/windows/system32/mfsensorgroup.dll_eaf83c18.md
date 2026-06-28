# Binary Specification: mfsensorgroup.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\mfsensorgroup.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `eaf83c183c26331d5af603c84abcbbe06ad55b36c3c158f6c424cdaa12a5b7a5`
* **Total Exported Functions:** 52

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 35 | `MFGetSensorDeviceProperty` | `0x30E0` | 53 | UnwindData |  |
| 40 | `MFGetSensorOrientation` | `0x3240` | 464 | UnwindData |  |
| 32 | `MFGetDeviceFromFSUniqueId` | `0x4260` | 887 | UnwindData |  |
| 41 | `MFInitializeSensorGroupStore` | `0xAA30` | 517 | UnwindData |  |
| 17 | `MFCreateSensorGroupById` | `0x10ED0` | 249 | UnwindData |  |
| 23 | `MFCreateSensorProfileWithFlags` | `0x10FD0` | 251 | UnwindData |  |
| 21 | `MFCreateSensorProfile` | `0x110E0` | 267 | UnwindData |  |
| 9 | `MFCreateCameraOcclusionStateMonitor` | `0x114B0` | 251 | UnwindData |  |
| 20 | `MFCreateSensorGroupWithOptions` | `0x115C0` | 252 | UnwindData |  |
| 7 | `MFCloneSensorProfile` | `0x12220` | 262 | UnwindData |  |
| 19 | `MFCreateSensorGroupIdManager` | `0x12330` | 232 | UnwindData |  |
| 37 | `MFGetSensorGroupAttributesFromId` | `0x12420` | 262 | UnwindData |  |
| 22 | `MFCreateSensorProfileCollection` | `0x12530` | 232 | UnwindData |  |
| 16 | `MFCreateSensorGroup` | `0x12620` | 259 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1C540` | 48 | UnwindData |  |
| 12 | `MFCreatePassthroughTranslatedMediaType` | `0x1CDF0` | 375 | UnwindData |  |
| 36 | `MFGetSensorDeviceRegistryProperty` | `0x1DD90` | 405 | UnwindData |  |
| 26 | `MFCreateTranslatedMediaType2` | `0x20610` | 36 | UnwindData |  |
| 27 | `MFCreateTranslatedMediaType3` | `0x20640` | 420 | UnwindData |  |
| 11 | `MFCreatePackageFamilyNameTag` | `0x25470` | 369 | UnwindData |  |
| 44 | `MFIsStreamAvailableToAppPackage` | `0x259A0` | 409 | UnwindData |  |
| 52 | `MFWriteSensorGroupDataToRegistry` | `0x261F0` | 441 | UnwindData |  |
| 28 | `MFCreateVirtualCamera` | `0x28620` | 911 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x28AF0` | 88 | UnwindData |  |
| 34 | `MFGetSGCH` | `0x2C840` | 397 | UnwindData |  |
| 6 | `MFCleanupVirtualCameraEntries` | `0x34390` | 662 | UnwindData |  |
| 30 | `MFGenerateAndPublishCameraTelemetry` | `0x34630` | 3,704 | UnwindData |  |
| 42 | `MFIsCameraDShowBridged` | `0x354B0` | 3,292 | UnwindData |  |
| 33 | `MFGetDeviceFromSGHash` | `0x397C0` | 649 | UnwindData |  |
| 43 | `MFIsSensorGroupName` | `0x3A460` | 125 | UnwindData |  |
| 5 | `MFCheckProcessCapabilities` | `0x50B40` | 877 | UnwindData |  |
| 8 | `MFCreateCameraControlMonitor` | `0x50EC0` | 239 | UnwindData |  |
| 10 | `MFCreateConfigurationEntry` | `0x50FC0` | 260 | UnwindData |  |
| 13 | `MFCreateRelativePanelWatcher` | `0x510D0` | 237 | UnwindData |  |
| 14 | `MFCreateSensorActivityMonitor` | `0x511D0` | 222 | UnwindData |  |
| 15 | `MFCreateSensorDeviceBlobByObject` | `0x512C0` | 1,115 | UnwindData |  |
| 18 | `MFCreateSensorGroupCollection` | `0x51730` | 222 | UnwindData |  |
| 24 | `MFCreateSensorStream` | `0x51820` | 256 | UnwindData |  |
| 25 | `MFCreateTranslatedMediaType` | `0x51930` | 31 | UnwindData |  |
| 29 | `MFDeleteSensorGroupById` | `0x51960` | 731 | UnwindData |  |
| 31 | `MFGetCameraKLibInformation` | `0x51C50` | 573 | UnwindData |  |
| 38 | `MFGetSensorGroupIdFromDeviceName` | `0x51EA0` | 1,072 | UnwindData |  |
| 39 | `MFGetSensorGroupPropertyName` | `0x522E0` | 290 | UnwindData |  |
| 45 | `MFIsVirtualCameraTypeSupported` | `0x52410` | 86 | UnwindData |  |
| 46 | `MFIsWindowsStudioEffectAvailable` | `0x52470` | 372 | UnwindData |  |
| 47 | `MFLoadSensorGroupFromRegistry` | `0x525F0` | 225 | UnwindData |  |
| 48 | `MFLoadSensorProfiles` | `0x526E0` | 225 | UnwindData |  |
| 49 | `MFPublishSensorProfiles` | `0x527D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `MFSensorProfileParseFilterSetString` | `0x527F0` | 259 | UnwindData |  |
| 51 | `MFValidateSensorProfile` | `0x52900` | 741 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x656A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x656B0` | 82,129 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |

# Binary Specification: mfsensorgroup.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\mfsensorgroup.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b0452ea6cee66d041f2bb75dfc0a548ba339e4a61b21face4c1b1d53a042c7d3`
* **Total Exported Functions:** 52

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 35 | `MFGetSensorDeviceProperty` | `0x3190` | 53 | UnwindData |  |
| 40 | `MFGetSensorOrientation` | `0x32F0` | 464 | UnwindData |  |
| 32 | `MFGetDeviceFromFSUniqueId` | `0x4480` | 887 | UnwindData |  |
| 41 | `MFInitializeSensorGroupStore` | `0x9590` | 517 | UnwindData |  |
| 17 | `MFCreateSensorGroupById` | `0xF340` | 249 | UnwindData |  |
| 23 | `MFCreateSensorProfileWithFlags` | `0xF440` | 251 | UnwindData |  |
| 21 | `MFCreateSensorProfile` | `0xF550` | 267 | UnwindData |  |
| 9 | `MFCreateCameraOcclusionStateMonitor` | `0xF920` | 251 | UnwindData |  |
| 20 | `MFCreateSensorGroupWithOptions` | `0xFA30` | 252 | UnwindData |  |
| 7 | `MFCloneSensorProfile` | `0x10690` | 262 | UnwindData |  |
| 19 | `MFCreateSensorGroupIdManager` | `0x107A0` | 232 | UnwindData |  |
| 37 | `MFGetSensorGroupAttributesFromId` | `0x10890` | 262 | UnwindData |  |
| 22 | `MFCreateSensorProfileCollection` | `0x109A0` | 232 | UnwindData |  |
| 16 | `MFCreateSensorGroup` | `0x10A90` | 259 | UnwindData |  |
| 2 | `DllGetClassObject` | `0x1A970` | 48 | UnwindData |  |
| 12 | `MFCreatePassthroughTranslatedMediaType` | `0x1B400` | 375 | UnwindData |  |
| 36 | `MFGetSensorDeviceRegistryProperty` | `0x1BE10` | 405 | UnwindData |  |
| 26 | `MFCreateTranslatedMediaType2` | `0x1E690` | 36 | UnwindData |  |
| 27 | `MFCreateTranslatedMediaType3` | `0x1E6C0` | 420 | UnwindData |  |
| 11 | `MFCreatePackageFamilyNameTag` | `0x23690` | 369 | UnwindData |  |
| 44 | `MFIsStreamAvailableToAppPackage` | `0x23BC0` | 409 | UnwindData |  |
| 52 | `MFWriteSensorGroupDataToRegistry` | `0x24800` | 441 | UnwindData |  |
| 28 | `MFCreateVirtualCamera` | `0x26DC0` | 911 | UnwindData |  |
| 1 | `DllCanUnloadNow` | `0x27290` | 88 | UnwindData |  |
| 34 | `MFGetSGCH` | `0x2B080` | 397 | UnwindData |  |
| 6 | `MFCleanupVirtualCameraEntries` | `0x33A80` | 662 | UnwindData |  |
| 30 | `MFGenerateAndPublishCameraTelemetry` | `0x33D20` | 46 | UnwindData |  |
| 42 | `MFIsCameraDShowBridged` | `0x33D60` | 3,276 | UnwindData |  |
| 33 | `MFGetDeviceFromSGHash` | `0x38380` | 649 | UnwindData |  |
| 43 | `MFIsSensorGroupName` | `0x39020` | 125 | UnwindData |  |
| 5 | `MFCheckProcessCapabilities` | `0x51D40` | 877 | UnwindData |  |
| 8 | `MFCreateCameraControlMonitor` | `0x520C0` | 239 | UnwindData |  |
| 10 | `MFCreateConfigurationEntry` | `0x521C0` | 260 | UnwindData |  |
| 13 | `MFCreateRelativePanelWatcher` | `0x522D0` | 237 | UnwindData |  |
| 14 | `MFCreateSensorActivityMonitor` | `0x523D0` | 222 | UnwindData |  |
| 15 | `MFCreateSensorDeviceBlobByObject` | `0x524C0` | 1,115 | UnwindData |  |
| 18 | `MFCreateSensorGroupCollection` | `0x52930` | 222 | UnwindData |  |
| 24 | `MFCreateSensorStream` | `0x52A20` | 256 | UnwindData |  |
| 25 | `MFCreateTranslatedMediaType` | `0x52B30` | 31 | UnwindData |  |
| 29 | `MFDeleteSensorGroupById` | `0x52B60` | 731 | UnwindData |  |
| 31 | `MFGetCameraKLibInformation` | `0x52E50` | 573 | UnwindData |  |
| 38 | `MFGetSensorGroupIdFromDeviceName` | `0x530A0` | 1,072 | UnwindData |  |
| 39 | `MFGetSensorGroupPropertyName` | `0x534E0` | 290 | UnwindData |  |
| 45 | `MFIsVirtualCameraTypeSupported` | `0x53610` | 86 | UnwindData |  |
| 46 | `MFIsWindowsStudioEffectAvailable` | `0x53670` | 356 | UnwindData |  |
| 47 | `MFLoadSensorGroupFromRegistry` | `0x537E0` | 225 | UnwindData |  |
| 48 | `MFLoadSensorProfiles` | `0x538D0` | 225 | UnwindData |  |
| 49 | `MFPublishSensorProfiles` | `0x539C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `MFSensorProfileParseFilterSetString` | `0x539E0` | 259 | UnwindData |  |
| 51 | `MFValidateSensorProfile` | `0x53AF0` | 741 | UnwindData |  |
| 3 | `DllRegisterServer` | `0x669D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DllUnregisterServer` | `0x669E0` | 77,697 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |

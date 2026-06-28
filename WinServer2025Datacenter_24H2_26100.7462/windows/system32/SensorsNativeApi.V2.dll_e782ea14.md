# Binary Specification: SensorsNativeApi.V2.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SensorsNativeApi.V2.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `e782ea141e222dec496956842b313e44332a03a916ef0f7bd64d21c0a8d8644d`
* **Total Exported Functions:** 72

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 3 | `SensorCloseV2` | `0x12060` | 132 | UnwindData |  |
| 4 | `SensorDeviceIoControlV2` | `0x12370` | 70 | UnwindData |  |
| 5 | `SensorDisableIoPathForDataNotificationsV2` | `0x12830` | 36 | UnwindData |  |
| 7 | `SensorEnableIdleOperationV2` | `0x12860` | 164 | UnwindData |  |
| 14 | `SensorGetCapabilitiesV2` | `0x12910` | 521 | UnwindData |  |
| 21 | `SensorGetDataV2` | `0x12B20` | 730 | UnwindData |  |
| 23 | `SensorGetDeviceIdV2` | `0x12E00` | 295 | UnwindData |  |
| 31 | `SensorGetRangeResolutionV2` | `0x12F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `SensorNotificationConfigureV2` | `0x12F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `SensorNotificationStartV2` | `0x12F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `SensorNotificationStopV2` | `0x12F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `SensorSetRangeResolutionV2` | `0x12F30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `SensorOpenV2` | `0x12F40` | 345 | UnwindData |  |
| 39 | `SensorRegisterDeviceRemovalNotificationV2` | `0x130A0` | 482 | UnwindData |  |
| 56 | `SensorStartV2` | `0x13290` | 277 | UnwindData |  |
| 59 | `SensorStopV2` | `0x137D0` | 1,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `SensorUnregisterDeviceRemovalNotificationV2` | `0x13CA0` | 660 | UnwindData |  |
| 72 | `DllMain` | `0x142E0` | 252 | UnwindData |  |
| 1 | `SensorCancelHistoryRetrievalV2` | `0x19290` | 103 | UnwindData |  |
| 2 | `SensorClearHistoryV2` | `0x19300` | 200 | UnwindData |  |
| 6 | `SensorDisableWakeV2` | `0x193D0` | 200 | UnwindData |  |
| 8 | `SensorEnableWakeV2` | `0x194A0` | 200 | UnwindData |  |
| 9 | `SensorGetAccDataV2` | `0x19570` | 76 | UnwindData |  |
| 10 | `SensorGetAlsDataV2` | `0x195D0` | 55 | UnwindData |  |
| 11 | `SensorGetAlsDataWithColorV2` | `0x19610` | 86 | UnwindData |  |
| 12 | `SensorGetBarDataV2` | `0x19670` | 62 | UnwindData |  |
| 13 | `SensorGetCapabilitiesCollectionV2` | `0x196C0` | 498 | UnwindData |  |
| 15 | `SensorGetCurrentReadingV2` | `0x198C0` | 463 | UnwindData |  |
| 16 | `SensorGetDataCollectionV2` | `0x19AA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `SensorGetDataDeliveryModeV2` | `0x19AB0` | 499 | UnwindData |  |
| 18 | `SensorGetDataFieldPropertiesV2` | `0x19CB0` | 637 | UnwindData |  |
| 19 | `SensorGetDataIntervalV2` | `0x19F40` | 496 | UnwindData |  |
| 20 | `SensorGetDataThresholdsV2` | `0x1A140` | 677 | UnwindData |  |
| 22 | `SensorGetDefaultDataThresholdsV2` | `0x1A3F0` | 677 | UnwindData |  |
| 24 | `SensorGetFifoMaxSizeV2` | `0x1A6A0` | 340 | UnwindData |  |
| 25 | `SensorGetFusDataV2` | `0x1A800` | 112 | UnwindData |  |
| 26 | `SensorGetGyrDataV2` | `0x1A880` | 55 | UnwindData |  |
| 27 | `SensorGetHistoryV2` | `0x1A8C0` | 946 | UnwindData |  |
| 28 | `SensorGetMagDataV2` | `0x1AC80` | 71 | UnwindData |  |
| 29 | `SensorGetPropertiesV2` | `0x1ACD0` | 681 | UnwindData |  |
| 30 | `SensorGetPrxDataV2` | `0x1AF80` | 76 | UnwindData |  |
| 32 | `SensorGetSupportedDataFieldsV2` | `0x1AFE0` | 493 | UnwindData |  |
| 33 | `SensorIsWakeEnabledV2` | `0x1B240` | 217 | UnwindData |  |
| 37 | `SensorOpenByInterfaceV2` | `0x1B320` | 396 | UnwindData |  |
| 40 | `SensorSetAccThresholdsV2` | `0x1B4C0` | 388 | UnwindData |  |
| 41 | `SensorSetAlsThresholdsV2` | `0x1B650` | 27 | UnwindData |  |
| 42 | `SensorSetAlsWithColorThresholdsV2` | `0x1B680` | 563 | UnwindData |  |
| 43 | `SensorSetBarThresholdsV2` | `0x1B8C0` | 184 | UnwindData |  |
| 44 | `SensorSetDataDeliveryModeV2` | `0x1B980` | 474 | UnwindData |  |
| 45 | `SensorSetDataIntervalV2` | `0x1BB60` | 260 | UnwindData |  |
| 46 | `SensorSetDataThresholdsV2` | `0x1BC70` | 359 | UnwindData |  |
| 47 | `SensorSetFusThresholdsV2` | `0x1BDE0` | 474 | UnwindData |  |
| 48 | `SensorSetGyrThresholdsV2` | `0x1BFC0` | 388 | UnwindData |  |
| 49 | `SensorSetMagThresholdsV2` | `0x1C150` | 388 | UnwindData |  |
| 50 | `SensorSetOrientationSensorThresholdsV2` | `0x1C2E0` | 175 | UnwindData |  |
| 52 | `SensorSetReportLatencyV2` | `0x1C3A0` | 474 | UnwindData |  |
| 53 | `SensorStartCollectionV2` | `0x1C580` | 277 | UnwindData |  |
| 54 | `SensorStartHistoryV2` | `0x1C6A0` | 472 | UnwindData |  |
| 55 | `SensorStartStateChangeNotificationV2` | `0x1C880` | 465 | UnwindData |  |
| 57 | `SensorStopHistoryV2` | `0x1CA60` | 472 | UnwindData |  |
| 58 | `SensorStopStateChangeNotificationV2` | `0x1CC40` | 338 | UnwindData |  |
| 61 | `SimpleOrientationClose` | `0x1FF00` | 98 | UnwindData |  |
| 62 | `SimpleOrientationEnableInLowPowerMode` | `0x1FF70` | 102 | UnwindData |  |
| 63 | `SimpleOrientationGetCapabilitiesCollectionV2` | `0x1FFE0` | 106 | UnwindData |  |
| 64 | `SimpleOrientationGetCurrentOrientation` | `0x20050` | 107 | UnwindData |  |
| 65 | `SimpleOrientationGetDeviceId` | `0x200D0` | 112 | UnwindData |  |
| 66 | `SimpleOrientationGetProperties` | `0x20150` | 112 | UnwindData |  |
| 67 | `SimpleOrientationOpen` | `0x201D0` | 171 | UnwindData |  |
| 68 | `SimpleOrientationRegisterDeviceRemovalNotification` | `0x20290` | 112 | UnwindData |  |
| 69 | `SimpleOrientationStart` | `0x20310` | 112 | UnwindData |  |
| 70 | `SimpleOrientationStop` | `0x20390` | 98 | UnwindData |  |
| 71 | `SimpleOrientationUnregisterDeviceRemovalNotification` | `0x20400` | 98 | UnwindData |  |

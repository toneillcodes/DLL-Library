# Binary Specification: SensorsNativeApi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\SensorsNativeApi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `519389c22232af3acb6b930f5cd0000daef884f3acc2769698b726f592bb1718`
* **Total Exported Functions:** 68

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 44 | `SensorRegisterPowerNotifications` | `0x6990` | 137 | UnwindData |  |
| 68 | `SensorsUnregisterPowerNotifications` | `0x6A20` | 47 | UnwindData |  |
| 1 | `SensorGetDataFieldProperties` | `0x8D90` | 214 | UnwindData |  |
| 2 | `DllMain` | `0x8F80` | 327 | UnwindData |  |
| 3 | `SensorCancelHistoryRetrieval` | `0x93E0` | 165 | UnwindData |  |
| 4 | `SensorClearHistory` | `0x9490` | 165 | UnwindData |  |
| 5 | `SensorClose` | `0x9540` | 291 | UnwindData |  |
| 6 | `SensorDetermineStackByPropertyStore` | `0x9670` | 242 | UnwindData |  |
| 7 | `SensorDeviceIoControl` | `0x9770` | 297 | UnwindData |  |
| 8 | `SensorDisableIoPathForDataNotifications` | `0x98A0` | 165 | UnwindData |  |
| 9 | `SensorDisableWake` | `0x9950` | 165 | UnwindData |  |
| 10 | `SensorEnableIdleOperation` | `0x9A00` | 181 | UnwindData |  |
| 11 | `SensorEnableWake` | `0x9AC0` | 165 | UnwindData |  |
| 12 | `SensorGetAccData` | `0x9B70` | 286 | UnwindData |  |
| 13 | `SensorGetAlsData` | `0x9CA0` | 241 | UnwindData |  |
| 14 | `SensorGetAlsDataWithColor` | `0x9DA0` | 327 | UnwindData |  |
| 15 | `SensorGetBarData` | `0x9EF0` | 241 | UnwindData |  |
| 16 | `SensorGetCapabilities` | `0x9FF0` | 194 | UnwindData |  |
| 17 | `SensorGetCapabilitiesCollection` | `0xA0C0` | 257 | UnwindData |  |
| 18 | `SensorGetCurrentReading` | `0xA1D0` | 214 | UnwindData |  |
| 19 | `SensorGetData` | `0xA2B0` | 210 | UnwindData |  |
| 20 | `SensorGetDataCollection` | `0xA390` | 214 | UnwindData |  |
| 21 | `SensorGetDataDeliveryMode` | `0xA470` | 187 | UnwindData |  |
| 22 | `SensorGetDefaultThresholds` | `0xA540` | 202 | UnwindData |  |
| 23 | `SensorGetDeviceId` | `0xA610` | 197 | UnwindData |  |
| 24 | `SensorGetFifoMaxSize` | `0xA6E0` | 187 | UnwindData |  |
| 25 | `SensorGetFusData` | `0xA7B0` | 387 | UnwindData |  |
| 26 | `SensorGetGyrData` | `0xA940` | 246 | UnwindData |  |
| 27 | `SensorGetHistory` | `0xAA40` | 181 | UnwindData |  |
| 28 | `SensorGetMagData` | `0xAB00` | 276 | UnwindData |  |
| 29 | `SensorGetProperties` | `0xAC20` | 197 | UnwindData |  |
| 30 | `SensorGetPrxData` | `0xACF0` | 283 | UnwindData |  |
| 31 | `SensorGetRangeResolution` | `0xAE20` | 266 | UnwindData |  |
| 32 | `SensorGetSupportedDataFields` | `0xAF30` | 197 | UnwindData |  |
| 33 | `SensorGetThresholds` | `0xB000` | 197 | UnwindData |  |
| 34 | `SensorGetTypeFromInterfacePath` | `0xB0D0` | 297 | UnwindData |  |
| 35 | `SensorIsWakeEnabled` | `0xB200` | 181 | UnwindData |  |
| 36 | `SensorNotificationConfigure` | `0xB2C0` | 247 | UnwindData |  |
| 37 | `SensorNotificationStart` | `0xB3C0` | 165 | UnwindData |  |
| 38 | `SensorNotificationStop` | `0xB470` | 170 | UnwindData |  |
| 39 | `SensorOpen` | `0xB520` | 543 | UnwindData |  |
| 40 | `SensorOpenByInterface` | `0xB750` | 489 | UnwindData |  |
| 41 | `SensorOpenByType` | `0xB940` | 481 | UnwindData |  |
| 42 | `SensorRegisterDeviceRemovalNotification` | `0xBB30` | 187 | UnwindData |  |
| 43 | `SensorRegisterEvent` | `0xBC00` | 214 | UnwindData |  |
| 45 | `SensorSelectBestDevice` | `0xBCE0` | 1,717 | UnwindData |  |
| 46 | `SensorSetAccThresholds` | `0xC3A0` | 209 | UnwindData |  |
| 47 | `SensorSetAlsThresholds` | `0xC480` | 209 | UnwindData |  |
| 48 | `SensorSetAlsWithColorThresholds` | `0xC560` | 257 | UnwindData |  |
| 49 | `SensorSetBarThresholds` | `0xC670` | 209 | UnwindData |  |
| 50 | `SensorSetDataDeliveryMode` | `0xC750` | 179 | UnwindData |  |
| 51 | `SensorSetDataInterval` | `0xC810` | 179 | UnwindData |  |
| 52 | `SensorSetFusThresholds` | `0xC8D0` | 209 | UnwindData |  |
| 53 | `SensorSetGyrThresholds` | `0xC9B0` | 209 | UnwindData |  |
| 54 | `SensorSetMagThresholds` | `0xCA90` | 209 | UnwindData |  |
| 55 | `SensorSetOrientationSensorThresholds` | `0xCB70` | 173 | UnwindData |  |
| 56 | `SensorSetRangeResolution` | `0xCC30` | 179 | UnwindData |  |
| 57 | `SensorSetReportLatency` | `0xCCF0` | 179 | UnwindData |  |
| 58 | `SensorSetThresholds` | `0xCDB0` | 181 | UnwindData |  |
| 59 | `SensorStart` | `0xCE70` | 220 | UnwindData |  |
| 60 | `SensorStartCollection` | `0xCF60` | 224 | UnwindData |  |
| 61 | `SensorStartHistory` | `0xD050` | 165 | UnwindData |  |
| 62 | `SensorStartStateChangeNotification` | `0xD100` | 197 | UnwindData |  |
| 63 | `SensorStop` | `0xD1D0` | 183 | UnwindData |  |
| 64 | `SensorStopHistory` | `0xD290` | 165 | UnwindData |  |
| 65 | `SensorStopStateChangeNotification` | `0xD340` | 165 | UnwindData |  |
| 66 | `SensorUnregisterDeviceRemovalNotification` | `0xD3F0` | 160 | UnwindData |  |
| 67 | `SensorUnregisterEvent` | `0xD4A0` | 165 | UnwindData |  |

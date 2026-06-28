# Binary Specification: SensorsNativeApi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\SensorsNativeApi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `6377bc9377ac82e572ebe021600ae80bbc4e2ebbb7a0f55696b5debb076f3b99`
* **Total Exported Functions:** 68

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 44 | `SensorRegisterPowerNotifications` | `0x6B50` | 137 | UnwindData |  |
| 68 | `SensorsUnregisterPowerNotifications` | `0x6BE0` | 47 | UnwindData |  |
| 1 | `SensorGetDataFieldProperties` | `0xAB90` | 214 | UnwindData |  |
| 2 | `DllMain` | `0xB910` | 327 | UnwindData |  |
| 3 | `SensorCancelHistoryRetrieval` | `0xBD70` | 165 | UnwindData |  |
| 4 | `SensorClearHistory` | `0xBE20` | 165 | UnwindData |  |
| 5 | `SensorClose` | `0xBED0` | 291 | UnwindData |  |
| 6 | `SensorDetermineStackByPropertyStore` | `0xC000` | 242 | UnwindData |  |
| 7 | `SensorDeviceIoControl` | `0xC100` | 297 | UnwindData |  |
| 8 | `SensorDisableIoPathForDataNotifications` | `0xC230` | 165 | UnwindData |  |
| 9 | `SensorDisableWake` | `0xC2E0` | 165 | UnwindData |  |
| 10 | `SensorEnableIdleOperation` | `0xC390` | 181 | UnwindData |  |
| 11 | `SensorEnableWake` | `0xC450` | 165 | UnwindData |  |
| 12 | `SensorGetAccData` | `0xC500` | 286 | UnwindData |  |
| 13 | `SensorGetAlsData` | `0xC630` | 241 | UnwindData |  |
| 14 | `SensorGetAlsDataWithColor` | `0xC730` | 327 | UnwindData |  |
| 15 | `SensorGetBarData` | `0xC880` | 241 | UnwindData |  |
| 16 | `SensorGetCapabilities` | `0xC980` | 194 | UnwindData |  |
| 17 | `SensorGetCapabilitiesCollection` | `0xCA50` | 257 | UnwindData |  |
| 18 | `SensorGetCurrentReading` | `0xCB60` | 214 | UnwindData |  |
| 19 | `SensorGetData` | `0xCC40` | 210 | UnwindData |  |
| 20 | `SensorGetDataCollection` | `0xCD20` | 214 | UnwindData |  |
| 21 | `SensorGetDataDeliveryMode` | `0xCE00` | 187 | UnwindData |  |
| 22 | `SensorGetDefaultThresholds` | `0xCED0` | 202 | UnwindData |  |
| 23 | `SensorGetDeviceId` | `0xCFA0` | 197 | UnwindData |  |
| 24 | `SensorGetFifoMaxSize` | `0xD070` | 187 | UnwindData |  |
| 25 | `SensorGetFusData` | `0xD140` | 387 | UnwindData |  |
| 26 | `SensorGetGyrData` | `0xD2D0` | 246 | UnwindData |  |
| 27 | `SensorGetHistory` | `0xD3D0` | 181 | UnwindData |  |
| 28 | `SensorGetMagData` | `0xD490` | 276 | UnwindData |  |
| 29 | `SensorGetProperties` | `0xD5B0` | 197 | UnwindData |  |
| 30 | `SensorGetPrxData` | `0xD680` | 283 | UnwindData |  |
| 31 | `SensorGetRangeResolution` | `0xD7B0` | 266 | UnwindData |  |
| 32 | `SensorGetSupportedDataFields` | `0xD8C0` | 197 | UnwindData |  |
| 33 | `SensorGetThresholds` | `0xD990` | 197 | UnwindData |  |
| 34 | `SensorGetTypeFromInterfacePath` | `0xDA60` | 297 | UnwindData |  |
| 35 | `SensorIsWakeEnabled` | `0xDB90` | 181 | UnwindData |  |
| 36 | `SensorNotificationConfigure` | `0xDC50` | 247 | UnwindData |  |
| 37 | `SensorNotificationStart` | `0xDD50` | 165 | UnwindData |  |
| 38 | `SensorNotificationStop` | `0xDE00` | 170 | UnwindData |  |
| 39 | `SensorOpen` | `0xDEB0` | 543 | UnwindData |  |
| 40 | `SensorOpenByInterface` | `0xE0E0` | 489 | UnwindData |  |
| 41 | `SensorOpenByType` | `0xE2D0` | 481 | UnwindData |  |
| 42 | `SensorRegisterDeviceRemovalNotification` | `0xE4C0` | 187 | UnwindData |  |
| 43 | `SensorRegisterEvent` | `0xE590` | 214 | UnwindData |  |
| 45 | `SensorSelectBestDevice` | `0xE670` | 1,717 | UnwindData |  |
| 46 | `SensorSetAccThresholds` | `0xED30` | 209 | UnwindData |  |
| 47 | `SensorSetAlsThresholds` | `0xEE10` | 209 | UnwindData |  |
| 48 | `SensorSetAlsWithColorThresholds` | `0xEEF0` | 257 | UnwindData |  |
| 49 | `SensorSetBarThresholds` | `0xF000` | 209 | UnwindData |  |
| 50 | `SensorSetDataDeliveryMode` | `0xF0E0` | 179 | UnwindData |  |
| 51 | `SensorSetDataInterval` | `0xF1A0` | 179 | UnwindData |  |
| 52 | `SensorSetFusThresholds` | `0xF260` | 209 | UnwindData |  |
| 53 | `SensorSetGyrThresholds` | `0xF340` | 209 | UnwindData |  |
| 54 | `SensorSetMagThresholds` | `0xF420` | 209 | UnwindData |  |
| 55 | `SensorSetOrientationSensorThresholds` | `0xF500` | 173 | UnwindData |  |
| 56 | `SensorSetRangeResolution` | `0xF5C0` | 179 | UnwindData |  |
| 57 | `SensorSetReportLatency` | `0xF680` | 179 | UnwindData |  |
| 58 | `SensorSetThresholds` | `0xF740` | 181 | UnwindData |  |
| 59 | `SensorStart` | `0xF800` | 220 | UnwindData |  |
| 60 | `SensorStartCollection` | `0xF8F0` | 224 | UnwindData |  |
| 61 | `SensorStartHistory` | `0xF9E0` | 165 | UnwindData |  |
| 62 | `SensorStartStateChangeNotification` | `0xFA90` | 197 | UnwindData |  |
| 63 | `SensorStop` | `0xFB60` | 183 | UnwindData |  |
| 64 | `SensorStopHistory` | `0xFC20` | 165 | UnwindData |  |
| 65 | `SensorStopStateChangeNotification` | `0xFCD0` | 165 | UnwindData |  |
| 66 | `SensorUnregisterDeviceRemovalNotification` | `0xFD80` | 160 | UnwindData |  |
| 67 | `SensorUnregisterEvent` | `0xFE30` | 165 | UnwindData |  |

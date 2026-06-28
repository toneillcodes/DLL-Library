# Binary Specification: NvInstallerUtil.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\DriverStore\FileRepository\nvlt.inf_amd64_18cae871934f9f98\NvInstallerUtil.dll`
* **Architecture:** x86
* **SHA256 Fingerprint:** `d2ff450bc1ce6a71d0208d9b6e695ff21b176c1a0b65df4963bbbba2ce2333f3`
* **Total Exported Functions:** 29

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `NvPluginGetInfo` | `0x4DA10` | 32,224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `InitializeTelemetryStandalone` | `0x557F0` | 864 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `InitializeTelemetryStandaloneWithDeviceId` | `0x55B50` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 12 | `InitializeTelemetryStandalone_3` | `0x55F70` | 832 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `InitializeTelemetryStandalone_2` | `0x562B0` | 464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `UninitializeTelemetry` | `0x56480` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `SubscribeForTelemetryNotifications` | `0x56570` | 336 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `UnsubscribeFromTelemetryNotifications` | `0x566C0` | 304 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `NvTelemetrySetAbContext` | `0x567F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 16 | `NvTelemetrySendEvent` | `0x56800` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 17 | `NvTelemetrySendEvent_2` | `0x56820` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `NvTelemetrySendAnonymousEvent` | `0x56C40` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `NvTelemetrySendAnonymousEvent_2` | `0x56C70` | 1,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `NvTelemetrySendFeedback` | `0x57090` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 19 | `NvTelemetrySendFeedback_2` | `0x570C0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `NvTelemetrySendFeedback_3` | `0x570F0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 21 | `NvTelemetrySendFeedback_4` | `0x57120` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetUserTelemetryConsent` | `0x574C0` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `SetUserTelemetryConsent` | `0x57830` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `GetDeviceTelemetryConsent` | `0x57AF0` | 880 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `SetDeviceTelemetryConsent` | `0x57E60` | 704 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `GetActivityById` | `0x58120` | 1,024 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 23 | `ReleaseActivity` | `0x58520` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `AddActivity` | `0x58570` | 1,232 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `DeleteActivity` | `0x58A40` | 528 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DeviceId` | `0x58C50` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `DeviceIdFree` | `0x58E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `FreeTelemetryString` | `0x58E90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `SetLocalizedEndpoints` | `0x58EA0` | 3,095,075 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |

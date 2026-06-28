# Binary Specification: winbioext.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\winbioext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2ab67affc7120e09d5862e4f14fb572812fa42f23f966a20d074e7f4974a29a6`
* **Total Exported Functions:** 26

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `WinBioAcquireFocus` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioAcquireFocus` |
| 5 | `WinBioAsyncEnumDatabases` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioAsyncEnumDatabases` |
| 6 | `WinBioAsyncMonitorFrameworkChanges` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioAsyncMonitorFrameworkChanges` |
| 7 | `WinBioCaptureSample` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioCaptureSample` |
| 8 | `WinBioCaptureSampleWithCallback` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioCaptureSampleWithCallback` |
| 9 | `WinBioEnrollCaptureWithCallback` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioEnrollCaptureWithCallback` |
| 10 | `WinBioEnumDatabases` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioEnumDatabases` |
| 11 | `WinBioGetDomainLogonSetting` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioGetDomainLogonSetting` |
| 12 | `WinBioGetEnabledSetting` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioGetEnabledSetting` |
| 13 | `WinBioGetLogonSetting` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioGetLogonSetting` |
| 14 | `WinBioIdentifyWithCallback` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioIdentifyWithCallback` |
| 15 | `WinBioIsESSCapable` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioIsESSCapable` |
| 17 | `WinBioLocateSensor` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioLocateSensor` |
| 18 | `WinBioLocateSensorWithCallback` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioLocateSensorWithCallback` |
| 19 | `WinBioLogonIdentifiedUser` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioLogonIdentifiedUser` |
| 1 | `WinBioNotifyPasswordChange` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioNotifyPasswordChange` |
| 20 | `WinBioOpenSession` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioOpenSession` |
| 21 | `WinBioRegisterEventMonitor` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioRegisterEventMonitor` |
| 22 | `WinBioRegisterServiceMonitor` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioRegisterServiceMonitor` |
| 23 | `WinBioReleaseFocus` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioReleaseFocus` |
| 24 | `WinBioUnregisterEventMonitor` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioUnregisterEventMonitor` |
| 25 | `WinBioUnregisterServiceMonitor` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioUnregisterServiceMonitor` |
| 26 | `WinBioVerifyWithCallback` | `0x0` | - | Forwarded | Forwarded to: `winbio.WinBioVerifyWithCallback` |
| 2 | `DllCanUnloadNow` | `0x67A0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `DllGetClassObject` | `0x67D0` | 200 | UnwindData |  |
| 16 | `WinBioIsLegacy` | `0x68D0` | 54 | UnwindData |  |

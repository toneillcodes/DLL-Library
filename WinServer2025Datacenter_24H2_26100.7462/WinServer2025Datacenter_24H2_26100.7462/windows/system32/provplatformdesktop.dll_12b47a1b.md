# Binary Specification: provplatformdesktop.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\provplatformdesktop.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `12b47a1b4a3a5eac5ef49ee303702be7fc93386ce9b3d42a659caf99a70b7e08`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `DllCanUnloadNow` | `0x2ABA0` | 70 | UnwindData |  |
| 6 | `DllGetActivationFactory` | `0x2ABF0` | 466 | UnwindData |  |
| 7 | `DllGetClassObject` | `0x2ADD0` | 232 | UnwindData |  |
| 1 | `CreateAutomaticRedeploymentFailureNotificationTask` | `0x2BC10` | 125 | UnwindData |  |
| 2 | `CheckPackageManagerOutOfProc` | `0x30CE0` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CheckUserConsent` | `0x30D70` | 1,146 | UnwindData |  |
| 4 | `ConfigureAppLaunch` | `0x312B0` | 356 | UnwindData |  |
| 8 | `GetDeviceId` | `0x31420` | 423 | UnwindData |  |
| 19 | `SetDeviceName` | `0x315D0` | 348 | UnwindData |  |
| 9 | `GetPackagePassword` | `0x31740` | 1,118 | UnwindData |  |
| 10 | `GetProvisioningTargetUser` | `0x31BD0` | 1,793 | UnwindData |  |
| 11 | `InitiateMgmtRefresh` | `0x322E0` | 165 | UnwindData |  |
| 12 | `InitiateSystemReset` | `0x32390` | 148 | UnwindData |  |
| 13 | `MgmtRefreshPrecheck` | `0x32430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MgmtRefreshRebootSystem` | `0x32440` | 124 | UnwindData |  |
| 15 | `MgmtRefreshReleaseSession` | `0x324D0` | 64 | UnwindData |  |
| 16 | `MgmtRefreshStageSession` | `0x32520` | 57 | UnwindData |  |
| 17 | `MgmtRefreshUnstageSession` | `0x32560` | 57 | UnwindData |  |
| 18 | `ReportInstallationError` | `0x325A0` | 763 | UnwindData |  |

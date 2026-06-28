# Binary Specification: provplatformdesktop.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\provplatformdesktop.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d9da65eb4aafc22af497a16a5a0c226d312b4ae20d1434792f62e72dc45db33f`
* **Total Exported Functions:** 19

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 5 | `DllCanUnloadNow` | `0x2ABB0` | 70 | UnwindData |  |
| 6 | `DllGetActivationFactory` | `0x2AC00` | 466 | UnwindData |  |
| 7 | `DllGetClassObject` | `0x2ADE0` | 232 | UnwindData |  |
| 1 | `CreateAutomaticRedeploymentFailureNotificationTask` | `0x2BC20` | 125 | UnwindData |  |
| 2 | `CheckPackageManagerOutOfProc` | `0x30D00` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `CheckUserConsent` | `0x30D90` | 1,146 | UnwindData |  |
| 4 | `ConfigureAppLaunch` | `0x312D0` | 356 | UnwindData |  |
| 8 | `GetDeviceId` | `0x31440` | 423 | UnwindData |  |
| 19 | `SetDeviceName` | `0x315F0` | 348 | UnwindData |  |
| 9 | `GetPackagePassword` | `0x31760` | 1,118 | UnwindData |  |
| 10 | `GetProvisioningTargetUser` | `0x31BF0` | 1,793 | UnwindData |  |
| 11 | `InitiateMgmtRefresh` | `0x32300` | 165 | UnwindData |  |
| 12 | `InitiateSystemReset` | `0x323B0` | 148 | UnwindData |  |
| 13 | `MgmtRefreshPrecheck` | `0x32450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MgmtRefreshRebootSystem` | `0x32460` | 124 | UnwindData |  |
| 15 | `MgmtRefreshReleaseSession` | `0x324F0` | 64 | UnwindData |  |
| 16 | `MgmtRefreshStageSession` | `0x32540` | 57 | UnwindData |  |
| 17 | `MgmtRefreshUnstageSession` | `0x32580` | 57 | UnwindData |  |
| 18 | `ReportInstallationError` | `0x325C0` | 763 | UnwindData |  |

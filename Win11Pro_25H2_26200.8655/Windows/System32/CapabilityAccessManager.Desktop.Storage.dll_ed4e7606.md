# Binary Specification: CapabilityAccessManager.Desktop.Storage.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\CapabilityAccessManager.Desktop.Storage.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `ed4e7606e97c96ca580dc3e0d027aa2d4f7872c527432dfd8a038ecc8561a80c`
* **Total Exported Functions:** 24

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllCanUnloadNow` | `0xEC840` | 90 | UnwindData |  |
| 1 | `CAMStorageAccessCheck` | `0xEDD00` | 63 | UnwindData |  |
| 2 | `ClearCAMStorageDatabase` | `0xEDD50` | 87 | UnwindData |  |
| 3 | `DeleteCAMStorageDatabaseFiles` | `0xEDDB0` | 23 | UnwindData |  |
| 5 | `DoCAMStorageDatabaseMaintenance` | `0xEDDD0` | 278 | UnwindData |  |
| 6 | `EraseUInt64CAMSetting` | `0xEDEF0` | 34 | UnwindData |  |
| 7 | `EraseUInt64MCPSettingsForClient` | `0xEDF20` | 40 | UnwindData |  |
| 8 | `EraseUInt64MCPSettingsForServer` | `0xEDF50` | 40 | UnwindData |  |
| 9 | `EraseUInt64MCPSettingsForUser` | `0xEDF80` | 20 | UnwindData |  |
| 10 | `FreeCAMStorageAppConsentArray` | `0xEDFA0` | 170 | UnwindData |  |
| 11 | `FreeMCPStorageConsentArray` | `0xEE050` | 33 | UnwindData |  |
| 12 | `GetCAMAutoAcceptConsentPromptsValue` | `0xEE080` | 59 | UnwindData |  |
| 13 | `GetUInt64CAMSetting` | `0xEE0D0` | 106 | UnwindData |  |
| 14 | `GetUInt64MCPSetting` | `0xEE140` | 33 | UnwindData |  |
| 15 | `GetUInt64MCPSettingsForClient` | `0xEE170` | 33 | UnwindData |  |
| 16 | `GetUInt64MCPSettingsForServer` | `0xEE1A0` | 33 | UnwindData |  |
| 17 | `InitializeCAMStorage` | `0xEE1D0` | 198 | UnwindData |  |
| 18 | `MCPStorageAccessCheck` | `0xEE2A0` | 33 | UnwindData |  |
| 19 | `PrepareCAMStorageDatabase` | `0xEE3E0` | 26 | UnwindData |  |
| 20 | `PutUInt64CAMSetting` | `0xEE400` | 44 | UnwindData |  |
| 21 | `PutUInt64CAMSettings` | `0xEE440` | 24 | UnwindData |  |
| 22 | `PutUInt64MCPSetting` | `0xEE460` | 40 | UnwindData |  |
| 23 | `QueryCAMSettingAppList` | `0xEE490` | 202 | UnwindData |  |
| 24 | `Test_ResetCAMStorageInitializationState` | `0xEE560` | 40 | UnwindData |  |

# Binary Specification: CapabilityAccessManager.Desktop.Storage.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\CapabilityAccessManager.Desktop.Storage.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0fb5724cd8f0ec673f37f31c0728a7f6df9aabde36009bfacc2f968860f82d06`
* **Total Exported Functions:** 22

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 4 | `DllCanUnloadNow` | `0xEBCB0` | 70 | UnwindData |  |
| 1 | `CAMStorageAccessCheck` | `0xECAD0` | 63 | UnwindData |  |
| 2 | `ClearCAMStorageDatabase` | `0xECB20` | 87 | UnwindData |  |
| 3 | `DeleteCAMStorageDatabaseFiles` | `0xECB80` | 23 | UnwindData |  |
| 5 | `DoCAMStorageDatabaseMaintenance` | `0xECBA0` | 278 | UnwindData |  |
| 6 | `EraseUInt64CAMSetting` | `0xECCC0` | 34 | UnwindData |  |
| 7 | `EraseUInt64MCPSettingsForClient` | `0xECCF0` | 24 | UnwindData |  |
| 8 | `EraseUInt64MCPSettingsForServer` | `0xECD10` | 24 | UnwindData |  |
| 9 | `FreeCAMStorageAppConsentArray` | `0xECD30` | 170 | UnwindData |  |
| 10 | `FreeMCPStorageConsentArray` | `0xECDE0` | 206 | UnwindData |  |
| 11 | `GetUInt64CAMSetting` | `0xECEC0` | 106 | UnwindData |  |
| 12 | `GetUInt64MCPSetting` | `0xECF30` | 110 | UnwindData |  |
| 13 | `GetUInt64MCPSettingsForClient` | `0xECFB0` | 68 | UnwindData |  |
| 14 | `GetUInt64MCPSettingsForServer` | `0xED000` | 68 | UnwindData |  |
| 15 | `InitializeCAMStorage` | `0xED050` | 198 | UnwindData |  |
| 16 | `MCPStorageAccessCheck` | `0xED120` | 62 | UnwindData |  |
| 17 | `PrepareCAMStorageDatabase` | `0xED280` | 26 | UnwindData |  |
| 18 | `PutUInt64CAMSetting` | `0xED2A0` | 44 | UnwindData |  |
| 19 | `PutUInt64CAMSettings` | `0xED2E0` | 24 | UnwindData |  |
| 20 | `PutUInt64MCPSetting` | `0xED300` | 44 | UnwindData |  |
| 21 | `QueryCAMSettingAppList` | `0xED340` | 202 | UnwindData |  |
| 22 | `Test_ResetCAMStorageInitializationState` | `0xED410` | 125 | UnwindData |  |

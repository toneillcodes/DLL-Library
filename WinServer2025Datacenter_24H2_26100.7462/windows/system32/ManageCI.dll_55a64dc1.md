# Binary Specification: ManageCI.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\ManageCI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `55a64dc1c9a2dc13b2e20da665cff8163e9ee86593fda919cdc6ea8b6af179a5`
* **Total Exported Functions:** 52

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 23 | `ManageCI` | `0x8950` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `ManageCI_BeginRemoveCIPolicy` | `0x8960` | 23 | UnwindData |  |
| 25 | `ManageCI_BeginRemoveSBCPToken` | `0x8980` | 23 | UnwindData |  |
| 26 | `ManageCI_BeginSetSBCPToken` | `0x89A0` | 26 | UnwindData |  |
| 27 | `ManageCI_BeginTransaction` | `0x89C0` | 23 | UnwindData |  |
| 28 | `ManageCI_BeginUpsertCIPolicy` | `0x89E0` | 26 | UnwindData |  |
| 29 | `ManageCI_Commit` | `0x8A00` | 23 | UnwindData |  |
| 30 | `ManageCI_End` | `0x8A20` | 25 | UnwindData |  |
| 31 | `ManageCI_FreeSbcpHandle` | `0x8A40` | 30 | UnwindData |  |
| 32 | `ManageCI_GetAllCIPolicies` | `0x8A70` | 209 | UnwindData |  |
| 33 | `ManageCI_GetAllSBCPTokens` | `0x8B50` | 368 | UnwindData |  |
| 34 | `ManageCI_GetCIPolicyByID` | `0x8CD0` | 128 | UnwindData |  |
| 35 | `ManageCI_GetPoliciesAuthorizedBySBCPToken` | `0x8D60` | 212 | UnwindData |  |
| 36 | `ManageCI_GetPolicyInformation` | `0x8E40` | 193 | UnwindData |  |
| 37 | `ManageCI_GetSBCPTokenByID` | `0x8F10` | 128 | UnwindData |  |
| 38 | `ManageCI_GetSBCPTokensForPolicyID` | `0x8FA0` | 371 | UnwindData |  |
| 39 | `ManageCI_GetSModeUnlockID` | `0x9120` | 125 | UnwindData |  |
| 40 | `ManageCI_GetTenantID` | `0x91B0` | 83 | UnwindData |  |
| 41 | `ManageCI_GetTokenInformation` | `0x9210` | 50 | UnwindData |  |
| 18 | `IsInProgress` | `0x9250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `ManageCI_IsInProgress` | `0x9250` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `ManageCI_ParsePolicy` | `0x9260` | 100 | UnwindData |  |
| 44 | `ManageCI_ParseSbcpToken` | `0x92D0` | 136 | UnwindData |  |
| 45 | `ManageCI_QueryBinary` | `0x9360` | 136 | UnwindData |  |
| 46 | `ManageCI_QueryDword` | `0x93F0` | 30 | UnwindData |  |
| 47 | `ManageCI_QueryQword` | `0x9420` | 31 | UnwindData |  |
| 48 | `ManageCI_QueryString` | `0x9450` | 169 | UnwindData |  |
| 49 | `ManageCI_Rollback` | `0x9500` | 23 | UnwindData |  |
| 50 | `ManageCI_ShouldIgnoreRemoval` | `0x9520` | 72 | UnwindData |  |
| 51 | `ManageCI_Start` | `0x9570` | 23 | UnwindData |  |
| 52 | `ManageCI_ValidateState` | `0x9590` | 23 | UnwindData |  |
| 1 | `BeginRemoveCIPolicy` | `0xE300` | 239 | UnwindData |  |
| 2 | `BeginRemoveSBCPToken` | `0xE400` | 522 | UnwindData |  |
| 3 | `BeginSetSBCPToken` | `0xE610` | 477 | UnwindData |  |
| 4 | `BeginTransaction` | `0xE800` | 449 | UnwindData |  |
| 5 | `BeginUpsertCIPolicy` | `0xE9D0` | 328 | UnwindData |  |
| 6 | `Commit` | `0xEB80` | 510 | UnwindData |  |
| 7 | `End` | `0xEE30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `GetAllCIPolicies` | `0xEE40` | 129 | UnwindData |  |
| 9 | `GetAllSBCPTokens` | `0xEED0` | 168 | UnwindData |  |
| 10 | `GetCIPolicyByID` | `0xEF80` | 99 | UnwindData |  |
| 11 | `GetPoliciesAuthorizedBySBCPToken` | `0xEFF0` | 26 | UnwindData |  |
| 12 | `GetPolicyInformation` | `0xF010` | 110 | UnwindData |  |
| 13 | `GetSBCPTokenByID` | `0xF090` | 289 | UnwindData |  |
| 14 | `GetSBCPTokensForPolicyID` | `0xF1C0` | 26 | UnwindData |  |
| 15 | `GetSModeUnlockID` | `0xF1E0` | 24 | UnwindData |  |
| 16 | `GetTenantID` | `0xF200` | 1,915 | UnwindData |  |
| 17 | `GetTokenInformation` | `0xF990` | 402 | UnwindData |  |
| 19 | `ParsePolicy` | `0x10F70` | 181 | UnwindData |  |
| 20 | `Rollback` | `0x11060` | 346 | UnwindData |  |
| 21 | `Start` | `0x11230` | 129 | UnwindData |  |
| 22 | `ValidateState` | `0x11880` | 10 | UnwindData |  |

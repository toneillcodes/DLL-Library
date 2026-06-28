# Binary Specification: ManageCI.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\ManageCI.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `296817f66c5c4e42d99eea8d97489e500565c3e27ee94bcd2126b55b46768f41`
* **Total Exported Functions:** 54

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 24 | `ManageCI` | `0xD060` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `ManageCI_BeginRemoveCIPolicy` | `0xD070` | 23 | UnwindData |  |
| 26 | `ManageCI_BeginRemoveSBCPToken` | `0xD090` | 23 | UnwindData |  |
| 27 | `ManageCI_BeginSetSBCPToken` | `0xD0B0` | 26 | UnwindData |  |
| 28 | `ManageCI_BeginTransaction` | `0xD0D0` | 23 | UnwindData |  |
| 29 | `ManageCI_BeginUpsertCIPolicy` | `0xD0F0` | 26 | UnwindData |  |
| 30 | `ManageCI_BeginUpsertSystemCIPolicy` | `0xD110` | 23 | UnwindData |  |
| 31 | `ManageCI_Commit` | `0xD130` | 23 | UnwindData |  |
| 32 | `ManageCI_End` | `0xD150` | 25 | UnwindData |  |
| 33 | `ManageCI_FreeSbcpHandle` | `0xD170` | 30 | UnwindData |  |
| 34 | `ManageCI_GetAllCIPolicies` | `0xD1A0` | 209 | UnwindData |  |
| 35 | `ManageCI_GetAllSBCPTokens` | `0xD280` | 368 | UnwindData |  |
| 36 | `ManageCI_GetCIPolicyByID` | `0xD400` | 128 | UnwindData |  |
| 37 | `ManageCI_GetPoliciesAuthorizedBySBCPToken` | `0xD490` | 212 | UnwindData |  |
| 38 | `ManageCI_GetPolicyInformation` | `0xD570` | 355 | UnwindData |  |
| 39 | `ManageCI_GetSBCPTokenByID` | `0xD6E0` | 128 | UnwindData |  |
| 40 | `ManageCI_GetSBCPTokensForPolicyID` | `0xD770` | 371 | UnwindData |  |
| 41 | `ManageCI_GetSModeUnlockID` | `0xD8F0` | 125 | UnwindData |  |
| 42 | `ManageCI_GetTenantID` | `0xD980` | 83 | UnwindData |  |
| 43 | `ManageCI_GetTokenInformation` | `0xD9E0` | 50 | UnwindData |  |
| 19 | `IsInProgress` | `0xDA20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `ManageCI_IsInProgress` | `0xDA20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `ManageCI_ParsePolicy` | `0xDA30` | 100 | UnwindData |  |
| 46 | `ManageCI_ParseSbcpToken` | `0xDAA0` | 136 | UnwindData |  |
| 47 | `ManageCI_QueryBinary` | `0xDB30` | 136 | UnwindData |  |
| 48 | `ManageCI_QueryDword` | `0xDBC0` | 30 | UnwindData |  |
| 49 | `ManageCI_QueryQword` | `0xDBF0` | 31 | UnwindData |  |
| 50 | `ManageCI_QueryString` | `0xDC20` | 169 | UnwindData |  |
| 51 | `ManageCI_Rollback` | `0xDCD0` | 23 | UnwindData |  |
| 52 | `ManageCI_ShouldIgnoreRemoval` | `0xDCF0` | 72 | UnwindData |  |
| 53 | `ManageCI_Start` | `0xDD40` | 23 | UnwindData |  |
| 54 | `ManageCI_ValidateState` | `0xDD60` | 23 | UnwindData |  |
| 1 | `BeginRemoveCIPolicy` | `0x145C0` | 239 | UnwindData |  |
| 2 | `BeginRemoveSBCPToken` | `0x146C0` | 522 | UnwindData |  |
| 3 | `BeginSetSBCPToken` | `0x148D0` | 477 | UnwindData |  |
| 4 | `BeginTransaction` | `0x14AC0` | 449 | UnwindData |  |
| 5 | `BeginUpsertCIPolicy` | `0x14C90` | 328 | UnwindData |  |
| 6 | `BeginUpsertSystemCIPolicy` | `0x14DE0` | 1,244 | UnwindData |  |
| 7 | `Commit` | `0x15320` | 510 | UnwindData |  |
| 8 | `End` | `0x155D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 9 | `GetAllCIPolicies` | `0x155E0` | 129 | UnwindData |  |
| 10 | `GetAllSBCPTokens` | `0x15670` | 168 | UnwindData |  |
| 11 | `GetCIPolicyByID` | `0x15720` | 99 | UnwindData |  |
| 12 | `GetPoliciesAuthorizedBySBCPToken` | `0x15790` | 26 | UnwindData |  |
| 13 | `GetPolicyInformation` | `0x157B0` | 110 | UnwindData |  |
| 14 | `GetSBCPTokenByID` | `0x15830` | 289 | UnwindData |  |
| 15 | `GetSBCPTokensForPolicyID` | `0x15960` | 26 | UnwindData |  |
| 16 | `GetSModeUnlockID` | `0x15980` | 24 | UnwindData |  |
| 17 | `GetTenantID` | `0x159A0` | 1,915 | UnwindData |  |
| 18 | `GetTokenInformation` | `0x16130` | 402 | UnwindData |  |
| 20 | `ParsePolicy` | `0x17710` | 175 | UnwindData |  |
| 21 | `Rollback` | `0x17800` | 346 | UnwindData |  |
| 22 | `Start` | `0x179D0` | 129 | UnwindData |  |
| 23 | `ValidateState` | `0x18050` | 10 | UnwindData |  |

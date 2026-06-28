# Binary Specification: tbs.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\tbs.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `5e92eb8bda894fd050eec0cdd005ba35fccc783b2a4ae5b72db856c4b1ebcd00`
* **Total Exported Functions:** 23

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `Tbsi_Is_Tpm_Present` | `0x14B0` | 56 | UnwindData |  |
| 9 | `Tbsi_GetDeviceInfo` | `0x14F0` | 158 | UnwindData |  |
| 20 | `Tbsip_Submit_Command` | `0x16C0` | 54 | UnwindData |  |
| 19 | `Tbsip_Context_Close` | `0x1F10` | 23 | UnwindData |  |
| 4 | `GetDeviceIDString` | `0x2340` | 99 | UnwindData |  |
| 5 | `GetDeviceIDWithTimeout` | `0x2620` | 144 | UnwindData |  |
| 14 | `Tbsi_Physical_Presence_Command` | `0x3010` | 123 | UnwindData |  |
| 12 | `Tbsi_Get_TCG_Log_Ex` | `0x30A0` | 164 | UnwindData |  |
| 6 | `Tbsi_Context_Create` | `0x32D0` | 57 | UnwindData |  |
| 3 | `GetDeviceID` | `0x3790` | 23 | UnwindData |  |
| 2 | `Tbsi_Get_TCG_Logs` | `0x9E20` | 48 | UnwindData |  |
| 7 | `Tbsi_Create_Windows_Key` | `0xB140` | 163 | UnwindData |  |
| 10 | `Tbsi_Get_OwnerAuth` | `0xB1F0` | 2,018 | UnwindData |  |
| 11 | `Tbsi_Get_TCG_Log` | `0xB9E0` | 85 | UnwindData |  |
| 15 | `Tbsi_Revoke_Attestation` | `0xBA40` | 134 | UnwindData |  |
| 17 | `Tbsi_Tpm_Vendor_Maintenance_Mode` | `0xBAD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `Tbsip_Cancel_Commands` | `0xBAF0` | 61 | UnwindData |  |
| 21 | `Tbsip_Submit_Command_NonBlocking` | `0xBB40` | 54 | UnwindData |  |
| 22 | `Tbsip_TestInterruptInformation` | `0xBB80` | 181 | UnwindData |  |
| 23 | `Tbsip_TestMorBit` | `0xBC40` | 186 | UnwindData |  |
| 1 | `Tbsi_Create_Attestation_From_Log` | `0xD6A0` | 1,701 | UnwindData |  |
| 8 | `Tbsi_FilterLog` | `0xDFA0` | 740 | UnwindData |  |
| 16 | `Tbsi_ShaHash` | `0xE290` | 473 | UnwindData |  |

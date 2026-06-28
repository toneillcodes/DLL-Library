# Binary Specification: tbs.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\tbs.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `88dfdc70ffc05ca9b0d866203f2f4314d66e8c9ca41a3e8f65b5f87383c909be`
* **Total Exported Functions:** 23

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 13 | `Tbsi_Is_Tpm_Present` | `0x15D0` | 56 | UnwindData |  |
| 9 | `Tbsi_GetDeviceInfo` | `0x1610` | 11 | UnwindData |  |
| 20 | `Tbsip_Submit_Command` | `0x18E0` | 54 | UnwindData |  |
| 19 | `Tbsip_Context_Close` | `0x2040` | 23 | UnwindData |  |
| 4 | `GetDeviceIDString` | `0x20A0` | 99 | UnwindData |  |
| 5 | `GetDeviceIDWithTimeout` | `0x2380` | 144 | UnwindData |  |
| 14 | `Tbsi_Physical_Presence_Command` | `0x2D70` | 123 | UnwindData |  |
| 12 | `Tbsi_Get_TCG_Log_Ex` | `0x2E00` | 164 | UnwindData |  |
| 6 | `Tbsi_Context_Create` | `0x3030` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `GetDeviceID` | `0x3170` | 23 | UnwindData |  |
| 2 | `Tbsi_Get_TCG_Logs` | `0x93C0` | 48 | UnwindData |  |
| 7 | `Tbsi_Create_Windows_Key` | `0xA540` | 163 | UnwindData |  |
| 10 | `Tbsi_Get_OwnerAuth` | `0xA5F0` | 2,018 | UnwindData |  |
| 11 | `Tbsi_Get_TCG_Log` | `0xADE0` | 42 | UnwindData |  |
| 15 | `Tbsi_Revoke_Attestation` | `0xAE10` | 134 | UnwindData |  |
| 17 | `Tbsi_Tpm_Vendor_Maintenance_Mode` | `0xAEA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 18 | `Tbsip_Cancel_Commands` | `0xAEC0` | 61 | UnwindData |  |
| 21 | `Tbsip_Submit_Command_NonBlocking` | `0xAF10` | 54 | UnwindData |  |
| 22 | `Tbsip_TestInterruptInformation` | `0xAF50` | 181 | UnwindData |  |
| 23 | `Tbsip_TestMorBit` | `0xB010` | 186 | UnwindData |  |
| 1 | `Tbsi_Create_Attestation_From_Log` | `0xB870` | 1,701 | UnwindData |  |
| 8 | `Tbsi_FilterLog` | `0xC170` | 740 | UnwindData |  |
| 16 | `Tbsi_ShaHash` | `0xC460` | 473 | UnwindData |  |

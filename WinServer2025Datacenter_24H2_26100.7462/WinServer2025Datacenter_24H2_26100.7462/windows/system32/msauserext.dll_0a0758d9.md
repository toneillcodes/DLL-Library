# Binary Specification: msauserext.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\msauserext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `0a0758d99b199ced82a49a67ec05879a5a1b48363e886f1918c85850ea3a2d64`
* **Total Exported Functions:** 21

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `MsaUser_CallerIsLoggedOnUser` | `0x5D90` | 90 | UnwindData |  |
| 10 | `MsaUser_CanSetParentWindow` | `0x5DF0` | 82 | UnwindData |  |
| 11 | `MsaUser_CheckIfAppTrusted` | `0x5E50` | 90 | UnwindData |  |
| 12 | `MsaUser_FormatUserDisplayName` | `0x5EB0` | 111 | UnwindData |  |
| 13 | `MsaUser_GetDeviceTelemetryInformation` | `0x5F30` | 133 | UnwindData |  |
| 14 | `MsaUser_GetDeviceTypeParameterValue` | `0x5FC0` | 91 | UnwindData |  |
| 15 | `MsaUser_GetInlineUxParameterValue` | `0x6030` | 91 | UnwindData |  |
| 16 | `MsaUser_GetPlatformQualifier` | `0x60A0` | 91 | UnwindData |  |
| 17 | `MsaUser_GetUserRegistrySecurityDescriptor` | `0x6110` | 99 | UnwindData |  |
| 18 | `MsaUser_IsChildAccount` | `0x6180` | 90 | UnwindData |  |
| 19 | `MsaUser_LoadServiceConfiguration` | `0x61E0` | 75 | UnwindData |  |
| 20 | `MsaUser_OverrideTicketRequestForLegacyAdControl` | `0x6240` | 88 | UnwindData |  |
| 21 | `MsaUser_WinBioSetMSACredential` | `0x62A0` | 79 | UnwindData |  |
| 1 | `MsaUI_ClearThreadClientContext` | `0x6300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `MsaUI_CloseClientContext` | `0x6300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MsaUI_RunWizard` | `0x6300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MsaUI_SetThreadClientContext` | `0x6300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `MsaUI_CreateClientContext` | `0x6310` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MsaUI_CredUIPromptForWindowsCredentials` | `0x6330` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MsaUI_LaunchWebAuthFlow` | `0x6350` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MsaUi_CreateClientContextFromWab` | `0x6370` | 0 | Indeterminate |  |

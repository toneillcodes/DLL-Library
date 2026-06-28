# Binary Specification: msauserext.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\msauserext.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f69bb8a162e50a5f6aedf02043a9665b3960fa9549986ce375cf321f994a7e26`
* **Total Exported Functions:** 21

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 9 | `MsaUser_CallerIsLoggedOnUser` | `0x5DA0` | 90 | UnwindData |  |
| 10 | `MsaUser_CanSetParentWindow` | `0x5E00` | 82 | UnwindData |  |
| 11 | `MsaUser_CheckIfAppTrusted` | `0x5E60` | 90 | UnwindData |  |
| 12 | `MsaUser_FormatUserDisplayName` | `0x5EC0` | 111 | UnwindData |  |
| 13 | `MsaUser_GetDeviceTelemetryInformation` | `0x5F40` | 133 | UnwindData |  |
| 14 | `MsaUser_GetDeviceTypeParameterValue` | `0x5FD0` | 91 | UnwindData |  |
| 15 | `MsaUser_GetInlineUxParameterValue` | `0x6040` | 91 | UnwindData |  |
| 16 | `MsaUser_GetPlatformQualifier` | `0x60B0` | 91 | UnwindData |  |
| 17 | `MsaUser_GetUserRegistrySecurityDescriptor` | `0x6120` | 99 | UnwindData |  |
| 18 | `MsaUser_IsChildAccount` | `0x6190` | 90 | UnwindData |  |
| 19 | `MsaUser_LoadServiceConfiguration` | `0x61F0` | 75 | UnwindData |  |
| 20 | `MsaUser_OverrideTicketRequestForLegacyAdControl` | `0x6250` | 88 | UnwindData |  |
| 21 | `MsaUser_WinBioSetMSACredential` | `0x62B0` | 79 | UnwindData |  |
| 1 | `MsaUI_ClearThreadClientContext` | `0x6310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `MsaUI_CloseClientContext` | `0x6310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `MsaUI_RunWizard` | `0x6310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `MsaUI_SetThreadClientContext` | `0x6310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `MsaUI_CreateClientContext` | `0x6320` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `MsaUI_CredUIPromptForWindowsCredentials` | `0x6340` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 5 | `MsaUI_LaunchWebAuthFlow` | `0x6360` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `MsaUi_CreateClientContextFromWab` | `0x6380` | 0 | Indeterminate |  |

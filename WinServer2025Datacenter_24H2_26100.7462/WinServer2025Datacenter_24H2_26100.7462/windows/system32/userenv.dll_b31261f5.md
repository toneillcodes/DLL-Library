# Binary Specification: userenv.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\userenv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `b31261f53f426cd45ca03dfe0ce8d8caf9f6df728bc54fdd3d6182a0d3324bb6`
* **Total Exported Functions:** 79

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 144 | `GetProfileType` | `0x2330` | 43 | UnwindData |  |
| 153 | `LoadUserProfileW` | `0x4510` | 43 | UnwindData |  |
| 164 | `UnloadUserProfile` | `0x4B80` | 43 | UnwindData |  |
| 148 | `GetUserProfileDirectoryW` | `0x61B0` | 78 | UnwindData |  |
| 147 | `GetUserProfileDirectoryA` | `0x6B10` | 270 | UnwindData |  |
| 151 | `LoadProfileExtender` | `0x6C30` | 304 | UnwindData |  |
| 123 | `ExpandEnvironmentStringsForUserA` | `0x9ED0` | 228 | UnwindData |  |
| 152 | `LoadUserProfileA` | `0x9FC0` | 387 | UnwindData |  |
| 124 | `ExpandEnvironmentStringsForUserW` | `0xA220` | 50 | UnwindData |  |
| 131 | `GetAppContainerFolderPath` | `0xA500` | 62 | UnwindData |  |
| 109 | `CreateEnvironmentBlock` | `0xA670` | 50 | UnwindData |  |
| 116 | `DestroyEnvironmentBlock` | `0xA6E0` | 50 | UnwindData |  |
| 132 | `GetAppContainerRegistryLocation` | `0xA720` | 60 | UnwindData |  |
| 114 | `DeriveAppContainerSidFromAppContainerName` | `0xB040` | 62 | UnwindData |  |
| 211 | *Ordinal Only* | `0xB090` | 62 | UnwindData |  |
| 130 | `GetAllUsersProfileDirectoryW` | `0xB0E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `CreateAppContainerProfile` | `0xB100` | 38 | UnwindData |  |
| 212 | *Ordinal Only* | `0xB130` | 123 | UnwindData |  |
| 158 | `RegisterGPNotification` | `0xB1E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `UnregisterGPNotification` | `0xB200` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | *Ordinal Only* | `0xB340` | 123 | UnwindData |  |
| 218 | *Ordinal Only* | `0xB3D0` | 76 | UnwindData |  |
| 146 | `GetProfilesDirectoryW` | `0xB430` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `GetAppliedGPOListA` | `0xB450` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | *Ordinal Only* | `0xB6A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `ProcessGroupPolicyCompletedEx` | `0xB6B0` | 94 | UnwindData |  |
| 213 | *Ordinal Only* | `0xB720` | 60 | UnwindData |  |
| 121 | `EnterCriticalPolicySection` | `0xBED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `GetDefaultUserProfileDirectoryW` | `0xBEF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `DeleteAppContainerProfile` | `0xBF10` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `FreeGPOListA` | `0xBFA0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `LeaveCriticalPolicySection` | `0xC040` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `DeleteProfileW` | `0xC560` | 43 | UnwindData |  |
| 162 | `RsopSetPolicySettingStatus` | `0xC720` | 102 | UnwindData |  |
| 161 | `RsopResetPolicySettingStatus` | `0xC790` | 76 | UnwindData |  |
| 163 | `UnloadProfileExtender` | `0xCB90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `GetNextFgPolicyRefreshInfo` | `0xCBB0` | 10,736 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `RsopLoggingEnabled` | `0xF5A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `AreThereVisibleLogoffScripts` | `0xF5C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `AreThereVisibleShutdownScripts` | `0xF5E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `ForceSyncFgPolicy` | `0xF600` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `FreeGPOListW` | `0xF620` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `GenerateGPNotification` | `0xF640` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `GetAppliedGPOListW` | `0xF660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `GetGPOListA` | `0xF680` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `GetGPOListW` | `0xF6A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `GetPreviousFgPolicyRefreshInfo` | `0xF6C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `HasPolicyForegroundProcessingCompleted` | `0xF6E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `RefreshPolicy` | `0xF700` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `RefreshPolicyEx` | `0xF720` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `WaitForMachinePolicyForegroundProcessing` | `0xF740` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `WaitForUserPolicyForegroundProcessing` | `0xF760` | 3,984 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | *Ordinal Only* | `0x106F0` | 40 | UnwindData |  |
| 207 | *Ordinal Only* | `0x10720` | 50 | UnwindData |  |
| 137 | *Ordinal Only* | `0x10760` | 89 | UnwindData |  |
| 139 | *Ordinal Only* | `0x107C0` | 188 | UnwindData |  |
| 104 | *Ordinal Only* | `0x10890` | 57 | UnwindData |  |
| 122 | *Ordinal Only* | `0x108D0` | 89 | UnwindData |  |
| 115 | `DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName` | `0x10930` | 78 | UnwindData |  |
| 154 | `ProcessGroupPolicyCompleted` | `0x10990` | 78 | UnwindData |  |
| 159 | `RsopAccessCheckByType` | `0x109F0` | 184 | UnwindData |  |
| 160 | `RsopFileAccessCheck` | `0x10AB0` | 104 | UnwindData |  |
| 110 | `CreateProfile` | `0x13B90` | 375 | UnwindData |  |
| 208 | *Ordinal Only* | `0x13D50` | 357 | UnwindData |  |
| 112 | `DeleteProfileA` | `0x13EC0` | 247 | UnwindData |  |
| 129 | `GetAllUsersProfileDirectoryA` | `0x13FC0` | 268 | UnwindData |  |
| 136 | `GetDefaultUserProfileDirectoryA` | `0x140E0` | 268 | UnwindData |  |
| 145 | `GetProfilesDirectoryA` | `0x14200` | 268 | UnwindData |  |
| 203 | *Ordinal Only* | `0x145A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | *Ordinal Only* | `0x145B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | *Ordinal Only* | `0x145C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | *Ordinal Only* | `0x145D0` | 129 | UnwindData |  |
| 117 | `DllCanUnloadNow` | `0x14660` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `DllGetClassObject` | `0x14680` | 70 | UnwindData |  |
| 119 | `DllRegisterServer` | `0x146D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `DllUnregisterServer` | `0x14710` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | *Ordinal Only* | `0x14750` | 1,840 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | *Ordinal Only* | `0x14E80` | 428 | UnwindData |  |
| 135 | *Ordinal Only* | `0x15040` | 5,340 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |

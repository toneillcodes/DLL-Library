# Binary Specification: userenv.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\userenv.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `7323a7e1c78e20283e0f9b1bacb8f5b6d5edd3900b039a5a47f2682a5e6e2728`
* **Total Exported Functions:** 79

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 153 | `LoadUserProfileW` | `0x45E0` | 43 | UnwindData |  |
| 164 | `UnloadUserProfile` | `0x4C50` | 43 | UnwindData |  |
| 148 | `GetUserProfileDirectoryW` | `0x6290` | 78 | UnwindData |  |
| 147 | `GetUserProfileDirectoryA` | `0x6AF0` | 270 | UnwindData |  |
| 151 | `LoadProfileExtender` | `0x6C10` | 304 | UnwindData |  |
| 123 | `ExpandEnvironmentStringsForUserA` | `0x82F0` | 228 | UnwindData |  |
| 152 | `LoadUserProfileA` | `0x83E0` | 387 | UnwindData |  |
| 124 | `ExpandEnvironmentStringsForUserW` | `0x8640` | 50 | UnwindData |  |
| 131 | `GetAppContainerFolderPath` | `0x8870` | 62 | UnwindData |  |
| 109 | `CreateEnvironmentBlock` | `0x89E0` | 50 | UnwindData |  |
| 116 | `DestroyEnvironmentBlock` | `0x8A50` | 50 | UnwindData |  |
| 132 | `GetAppContainerRegistryLocation` | `0x8A90` | 60 | UnwindData |  |
| 114 | `DeriveAppContainerSidFromAppContainerName` | `0x8AE0` | 62 | UnwindData |  |
| 211 | *Ordinal Only* | `0x8B30` | 62 | UnwindData |  |
| 130 | `GetAllUsersProfileDirectoryW` | `0x8E60` | 240 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `CreateAppContainerProfile` | `0x8F50` | 38 | UnwindData |  |
| 212 | *Ordinal Only* | `0x8F80` | 123 | UnwindData |  |
| 158 | `RegisterGPNotification` | `0x9030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 165 | `UnregisterGPNotification` | `0x9050` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 210 | *Ordinal Only* | `0x9190` | 123 | UnwindData |  |
| 218 | *Ordinal Only* | `0x9220` | 76 | UnwindData |  |
| 146 | `GetProfilesDirectoryW` | `0x9280` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 133 | `GetAppliedGPOListA` | `0x9520` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 217 | *Ordinal Only* | `0x9770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 155 | `ProcessGroupPolicyCompletedEx` | `0x9780` | 94 | UnwindData |  |
| 213 | *Ordinal Only* | `0x97F0` | 60 | UnwindData |  |
| 121 | `EnterCriticalPolicySection` | `0xA000` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `GetDefaultUserProfileDirectoryW` | `0xA020` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `DeleteAppContainerProfile` | `0xA040` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `FreeGPOListA` | `0xA0D0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `LeaveCriticalPolicySection` | `0xA170` | 1,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `DeleteProfileW` | `0xA690` | 43 | UnwindData |  |
| 162 | `RsopSetPolicySettingStatus` | `0xA850` | 102 | UnwindData |  |
| 161 | `RsopResetPolicySettingStatus` | `0xA8C0` | 76 | UnwindData |  |
| 163 | `UnloadProfileExtender` | `0xACC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `GetNextFgPolicyRefreshInfo` | `0xACE0` | 608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `GetProfileType` | `0xAF40` | 81 | UnwindData |  |
| 105 | `RsopLoggingEnabled` | `0xFF30` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `AreThereVisibleLogoffScripts` | `0xFF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `AreThereVisibleShutdownScripts` | `0xFF70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `ForceSyncFgPolicy` | `0xFF90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 127 | `FreeGPOListW` | `0xFFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `GenerateGPNotification` | `0xFFD0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `GetAppliedGPOListW` | `0xFFF0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 140 | `GetGPOListA` | `0x10010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `GetGPOListW` | `0x10030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `GetPreviousFgPolicyRefreshInfo` | `0x10050` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 149 | `HasPolicyForegroundProcessingCompleted` | `0x10070` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `RefreshPolicy` | `0x10090` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 157 | `RefreshPolicyEx` | `0x100B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `WaitForMachinePolicyForegroundProcessing` | `0x100D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 167 | `WaitForUserPolicyForegroundProcessing` | `0x100F0` | 4,080 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | *Ordinal Only* | `0x110E0` | 40 | UnwindData |  |
| 207 | *Ordinal Only* | `0x11110` | 50 | UnwindData |  |
| 137 | *Ordinal Only* | `0x11150` | 89 | UnwindData |  |
| 139 | *Ordinal Only* | `0x111B0` | 188 | UnwindData |  |
| 104 | *Ordinal Only* | `0x11280` | 57 | UnwindData |  |
| 122 | *Ordinal Only* | `0x112C0` | 89 | UnwindData |  |
| 115 | `DeriveRestrictedAppContainerSidFromAppContainerSidAndRestrictedName` | `0x11320` | 78 | UnwindData |  |
| 154 | `ProcessGroupPolicyCompleted` | `0x11380` | 78 | UnwindData |  |
| 159 | `RsopAccessCheckByType` | `0x113E0` | 184 | UnwindData |  |
| 160 | `RsopFileAccessCheck` | `0x114A0` | 104 | UnwindData |  |
| 110 | `CreateProfile` | `0x14620` | 375 | UnwindData |  |
| 208 | *Ordinal Only* | `0x147E0` | 357 | UnwindData |  |
| 112 | `DeleteProfileA` | `0x14950` | 247 | UnwindData |  |
| 129 | `GetAllUsersProfileDirectoryA` | `0x14A50` | 268 | UnwindData |  |
| 136 | `GetDefaultUserProfileDirectoryA` | `0x14B70` | 268 | UnwindData |  |
| 145 | `GetProfilesDirectoryA` | `0x14C90` | 268 | UnwindData |  |
| 203 | *Ordinal Only* | `0x15020` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 209 | *Ordinal Only* | `0x15030` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 202 | *Ordinal Only* | `0x15040` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 219 | *Ordinal Only* | `0x15050` | 140 | UnwindData |  |
| 117 | `DllCanUnloadNow` | `0x150F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `DllGetClassObject` | `0x15110` | 70 | UnwindData |  |
| 119 | `DllRegisterServer` | `0x15160` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `DllUnregisterServer` | `0x151A0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 214 | *Ordinal Only* | `0x151E0` | 15,056 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 175 | *Ordinal Only* | `0x18CB0` | 529 | UnwindData |  |
| 135 | *Ordinal Only* | `0x18F90` | 9,557 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |

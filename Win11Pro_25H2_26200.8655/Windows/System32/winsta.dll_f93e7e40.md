# Binary Specification: winsta.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\winsta.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `f93e7e4076315c13ba83ef14311cbb0413c3c4f04168f450b510bd567f21fa51`
* **Total Exported Functions:** 181

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 38 | `WinStationDisconnect` | `0x1320` | 203 | UnwindData |  |
| 155 | `WinStationVirtualOpenEx` | `0x1560` | 117 | UnwindData |  |
| 75 | `WinStationGetProcessSid` | `0x1CC0` | 137 | UnwindData |  |
| 65 | `WinStationGetCurrentSessionConnectionProperty` | `0x1F00` | 391 | UnwindData |  |
| 50 | `WinStationFreeGAPMemory` | `0x2540` | 52 | UnwindData |  |
| 63 | `WinStationGetConnectionProperty` | `0x2690` | 246 | UnwindData |  |
| 58 | `WinStationGetAllProcesses` | `0x2CC0` | 609 | UnwindData |  |
| 91 | `WinStationNameFromLogonIdW` | `0x2F50` | 260 | UnwindData |  |
| 66 | `WinStationGetCurrentSessionTerminalName` | `0x3CE0` | 484 | UnwindData |  |
| 86 | `WinStationIsCurrentSessionRemoteable` | `0x44B0` | 608 | UnwindData |  |
| 101 | `WinStationQueryCurrentSessionInformation` | `0x4720` | 20 | UnwindData |  |
| 64 | `WinStationGetCurrentSessionCapabilities` | `0x4840` | 695 | UnwindData |  |
| 45 | `WinStationEnumerateW` | `0x5B90` | 139 | UnwindData |  |
| 89 | `WinStationIsSessionRemoteable` | `0x7DE0` | 520 | UnwindData |  |
| 59 | `WinStationGetAllSessionsEx` | `0xA0D0` | 1,484 | UnwindData |  |
| 150 | `WinStationUnRegisterNotificationEvent` | `0xA840` | 42 | UnwindData |  |
| 149 | `WinStationUnRegisterConsoleNotification` | `0xB920` | 54 | UnwindData |  |
| 151 | `WinStationUnRegisterSessionNotification` | `0xB920` | 54 | UnwindData |  |
| 23 | `WTSUnRegisterSessionNotificationEx` | `0xBD70` | 165 | UnwindData |  |
| 146 | `WinStationSystemShutdownWait` | `0xBE20` | 207 | UnwindData |  |
| 180 | `_WinStationWaitForConnect` | `0xCB40` | 336 | UnwindData |  |
| 88 | `WinStationIsSessionPermitted` | `0xCCA0` | 335 | UnwindData |  |
| 49 | `WinStationFreeEXECENVDATAEX` | `0xCF80` | 109 | UnwindData |  |
| 51 | `WinStationFreeMemory` | `0xD930` | 29 | UnwindData |  |
| 79 | `WinStationGetTermSrvCountersValue` | `0xDFD0` | 343 | UnwindData |  |
| 118 | `WinStationRegisterCurrentSessionNotificationEvent` | `0xF310` | 30 | UnwindData |  |
| 131 | `WinStationSendWindowMessage` | `0xF680` | 935 | UnwindData |  |
| 136 | `WinStationSetLastWinlogonNotification` | `0xFE60` | 450 | UnwindData |  |
| 94 | `WinStationOpenServerA` | `0x104C0` | 268 | UnwindData |  |
| 61 | `WinStationGetAllUserSessions` | `0x10670` | 900 | UnwindData |  |
| 99 | `WinStationPreCreateGlassReplacementSessionEx` | `0x10A00` | 1,008 | UnwindData |  |
| 115 | `WinStationRegisterConsoleNotification` | `0x110B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `WinStationRegisterSessionNotification` | `0x110B0` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `WinStationNegotiateSession` | `0x11120` | 574 | UnwindData |  |
| 22 | `WTSRegisterSessionNotificationEx` | `0x11430` | 154 | UnwindData |  |
| 116 | `WinStationRegisterConsoleNotificationEx` | `0x114D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `WinStationRegisterConsoleNotificationEx2` | `0x114D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `WinStationRegisterSessionNotificationEx` | `0x114D0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `WinStationCloseServer` | `0x11510` | 36 | UnwindData |  |
| 27 | `WinStationBroadcastSystemMessage` | `0x11620` | 758 | UnwindData |  |
| 42 | `WinStationEnumerateExW` | `0x11D40` | 713 | UnwindData |  |
| 52 | `WinStationFreePropertyValue` | `0x12470` | 113 | UnwindData |  |
| 72 | `WinStationGetLoggedOnCount` | `0x12AB0` | 353 | UnwindData |  |
| 97 | `WinStationOpenServerW` | `0x12C50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `WinStationWaitSystemEvent` | `0x12C60` | 1,037 | UnwindData |  |
| 102 | `WinStationQueryEnforcementCore` | `0x13080` | 486 | UnwindData |  |
| 125 | `WinStationReportLoggedOnCompleted` | `0x13270` | 378 | UnwindData |  |
| 96 | `WinStationOpenServerExW` | `0x13560` | 144 | UnwindData |  |
| 56 | `WinStationFreeUserSessionInfo` | `0x13600` | 53 | UnwindData |  |
| 145 | `WinStationSystemShutdownStarted` | `0x13AA0` | 360 | UnwindData |  |
| 55 | `WinStationFreeUserCredentials` | `0x141E0` | 84 | UnwindData |  |
| 98 | `WinStationPreCreateGlassReplacementSession` | `0x142F0` | 1,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `WinStationQueryInformationW` | `0x14970` | 502 | UnwindData |  |
| 95 | `WinStationOpenServerExA` | `0x22E20` | 268 | UnwindData |  |
| 25 | `WinStationActiveSessionExists` | `0x24AB0` | 269 | UnwindData |  |
| 32 | `WinStationConnectAndLockDesktop` | `0x24BD0` | 288 | UnwindData |  |
| 35 | `WinStationConnectW` | `0x24D00` | 381 | UnwindData |  |
| 39 | `WinStationEnableChildSessions` | `0x24E90` | 231 | UnwindData |  |
| 40 | `WinStationEnumerateA` | `0x24F80` | 259 | UnwindData |  |
| 41 | `WinStationEnumerateContainerSessions` | `0x25090` | 249 | UnwindData |  |
| 44 | `WinStationEnumerateProcesses` | `0x25190` | 165 | UnwindData |  |
| 54 | `WinStationFreeUserCertificates` | `0x25240` | 59 | UnwindData |  |
| 62 | `WinStationGetChildSessionId` | `0x25290` | 250 | UnwindData |  |
| 67 | `WinStationGetDeviceId` | `0x25390` | 266 | UnwindData |  |
| 68 | `WinStationGetInitialApplication` | `0x254A0` | 336 | UnwindData |  |
| 74 | `WinStationGetParentSessionId` | `0x25600` | 286 | UnwindData |  |
| 78 | `WinStationGetSessionIds` | `0x25730` | 378 | UnwindData |  |
| 80 | `WinStationGetUserCertificates` | `0x258B0` | 548 | UnwindData |  |
| 85 | `WinStationIsChildSessionsEnabled` | `0x25AE0` | 275 | UnwindData |  |
| 109 | `WinStationRcmShadow2` | `0x25C00` | 344 | UnwindData |  |
| 127 | `WinStationReset` | `0x25D60` | 203 | UnwindData |  |
| 128 | `WinStationRevertFromServicesSession` | `0x25E40` | 212 | UnwindData |  |
| 129 | `WinStationSendMessageA` | `0x25F20` | 334 | UnwindData |  |
| 130 | `WinStationSendMessageW` | `0x26080` | 819 | UnwindData |  |
| 135 | `WinStationSetInformationW` | `0x263C0` | 297 | UnwindData |  |
| 139 | `WinStationShadow` | `0x264F0` | 373 | UnwindData |  |
| 140 | `WinStationShadowAccessCheck` | `0x26670` | 289 | UnwindData |  |
| 141 | `WinStationShadowStop` | `0x267A0` | 323 | UnwindData |  |
| 142 | `WinStationShadowStop2` | `0x268F0` | 262 | UnwindData |  |
| 143 | `WinStationShutdownSystem` | `0x26A00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `WinStationSwitchToServicesSession` | `0x26A10` | 212 | UnwindData |  |
| 148 | `WinStationTerminateProcess` | `0x26AF0` | 401 | UnwindData |  |
| 153 | `WinStationVerify` | `0x26C90` | 324 | UnwindData |  |
| 154 | `WinStationVirtualOpen` | `0x26DE0` | 147 | UnwindData |  |
| 160 | `_WinStationBeepOpen` | `0x26E80` | 66 | UnwindData |  |
| 174 | `_WinStationShadowTarget` | `0x26ED0` | 105 | UnwindData |  |
| 175 | `_WinStationShadowTarget2` | `0x26F40` | 724 | UnwindData |  |
| 172 | `_WinStationReadRegistry` | `0x27220` | 3,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `_WinStationSessionInitialized` | `0x27220` | 3,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `_WinStationShadowTargetSetup` | `0x27220` | 3,312 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `WinStationFreeConsoleNotification` | `0x27F10` | 49 | UnwindData |  |
| 53 | `WinStationFreeSessionNotification` | `0x27F10` | 49 | UnwindData |  |
| 119 | `WinStationRegisterNotificationEvent` | `0x27F50` | 28 | UnwindData |  |
| 37 | `WinStationCreateChildSessionTransport` | `0x28500` | 206 | UnwindData |  |
| 133 | `WinStationSetAutologonPassword` | `0x285E0` | 236 | UnwindData |  |
| 36 | `WinStationConsumeCacheSession` | `0x28920` | 262 | UnwindData |  |
| 71 | `WinStationGetLastWinlogonNotification` | `0x28A30` | 359 | UnwindData |  |
| 76 | `WinStationGetRedirectAuthInfo` | `0x28BA0` | 294 | UnwindData |  |
| 77 | `WinStationGetRestrictedLogonInfo` | `0x28CD0` | 288 | UnwindData |  |
| 81 | `WinStationGetUserCredentials` | `0x28E00` | 803 | UnwindData |  |
| 82 | `WinStationGetUserProfile` | `0x29130` | 277 | UnwindData |  |
| 84 | `WinStationIsBoundToCacheTerminal` | `0x29250` | 270 | UnwindData |  |
| 87 | `WinStationIsHelpAssistantSession` | `0x29370` | 50 | UnwindData |  |
| 110 | `WinStationRedirectErrorMessage` | `0x293B0` | 215 | UnwindData |  |
| 111 | `WinStationRedirectLogonBeginPainting` | `0x29490` | 220 | UnwindData |  |
| 112 | `WinStationRedirectLogonError` | `0x29580` | 316 | UnwindData |  |
| 113 | `WinStationRedirectLogonMessage` | `0x296D0` | 291 | UnwindData |  |
| 114 | `WinStationRedirectLogonStatus` | `0x29800` | 255 | UnwindData |  |
| 126 | `WinStationReportUIResult` | `0x29910` | 212 | UnwindData |  |
| 147 | `WinStationTerminateGlassReplacementSession` | `0x299F0` | 339 | UnwindData |  |
| 152 | `WinStationUserLoginAccessCheck` | `0x29B50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `_WinStationWaitForConnectEx` | `0x29B70` | 255 | UnwindData |  |
| 2 | `LogonIdFromWinStationNameW` | `0x29C80` | 814 | UnwindData |  |
| 60 | `WinStationGetAllSessionsW` | `0x29FC0` | 471 | UnwindData |  |
| 5 | `ServerLicensingClose` | `0x2AA90` | 77 | UnwindData |  |
| 6 | `ServerLicensingDeactivateCurrentPolicy` | `0x2AAF0` | 164 | UnwindData |  |
| 7 | `ServerLicensingFreePolicyInformation` | `0x2ABA0` | 87 | UnwindData |  |
| 8 | `ServerLicensingGetAadInfo` | `0x2AC00` | 335 | UnwindData |  |
| 9 | `ServerLicensingGetAvailablePolicyIds` | `0x2AD60` | 239 | UnwindData |  |
| 10 | `ServerLicensingGetPolicy` | `0x2AE60` | 201 | UnwindData |  |
| 11 | `ServerLicensingGetPolicyInformationA` | `0x2AF30` | 99 | UnwindData |  |
| 12 | `ServerLicensingGetPolicyInformationW` | `0x2AFA0` | 345 | UnwindData |  |
| 13 | `ServerLicensingLoadPolicy` | `0x2B100` | 29 | UnwindData |  |
| 18 | `ServerLicensingUnloadPolicy` | `0x2B100` | 29 | UnwindData |  |
| 14 | `ServerLicensingOpenA` | `0x2B130` | 43 | UnwindData |  |
| 15 | `ServerLicensingOpenW` | `0x2B170` | 325 | UnwindData |  |
| 16 | `ServerLicensingSetAadInfo` | `0x2B2C0` | 300 | UnwindData |  |
| 17 | `ServerLicensingSetPolicy` | `0x2B400` | 191 | UnwindData |  |
| 132 | `WinStationServerPing` | `0x2B4D0` | 164 | UnwindData |  |
| 1 | `LogonIdFromWinStationNameA` | `0x2B580` | 46 | UnwindData |  |
| 3 | `RemoteAssistancePrepareSystemRestore` | `0x2B5C0` | 46 | UnwindData |  |
| 4 | `ServerGetInternetConnectorStatus` | `0x2B600` | 46 | UnwindData |  |
| 19 | `ServerQueryInetConnectorInformationA` | `0x2B640` | 46 | UnwindData |  |
| 20 | `ServerQueryInetConnectorInformationW` | `0x2B680` | 46 | UnwindData |  |
| 21 | `ServerSetInternetConnectorStatus` | `0x2B6C0` | 46 | UnwindData |  |
| 24 | `WinStationActivateLicense` | `0x2B700` | 46 | UnwindData |  |
| 26 | `WinStationAutoReconnect` | `0x2B740` | 46 | UnwindData |  |
| 28 | `WinStationCheckAccess` | `0x2B780` | 46 | UnwindData |  |
| 29 | `WinStationCheckLoopBack` | `0x2B7C0` | 46 | UnwindData |  |
| 31 | `WinStationConnectA` | `0x2B800` | 46 | UnwindData |  |
| 33 | `WinStationConnectCallback` | `0x2B840` | 46 | UnwindData |  |
| 34 | `WinStationConnectEx` | `0x2B880` | 49 | UnwindData |  |
| 43 | `WinStationEnumerateLicenses` | `0x2B8C0` | 46 | UnwindData |  |
| 46 | `WinStationEnumerate_IndexedA` | `0x2B900` | 46 | UnwindData |  |
| 47 | `WinStationEnumerate_IndexedW` | `0x2B940` | 46 | UnwindData |  |
| 57 | `WinStationGenerateLicense` | `0x2B980` | 46 | UnwindData |  |
| 69 | `WinStationGetLanAdapterNameA` | `0x2B9C0` | 46 | UnwindData |  |
| 70 | `WinStationGetLanAdapterNameW` | `0x2BA00` | 46 | UnwindData |  |
| 73 | `WinStationGetMachinePolicy` | `0x2BA40` | 46 | UnwindData |  |
| 83 | `WinStationInstallLicense` | `0x2BA80` | 46 | UnwindData |  |
| 90 | `WinStationNameFromLogonIdA` | `0x2BAC0` | 46 | UnwindData |  |
| 93 | `WinStationNtsdDebug` | `0x2BB00` | 46 | UnwindData |  |
| 100 | `WinStationQueryAllowConcurrentConnections` | `0x2BB40` | 46 | UnwindData |  |
| 103 | `WinStationQueryInformationA` | `0x2BB80` | 46 | UnwindData |  |
| 105 | `WinStationQueryLicense` | `0x2BBC0` | 46 | UnwindData |  |
| 106 | `WinStationQueryLogonCredentialsW` | `0x2BC00` | 46 | UnwindData |  |
| 108 | `WinStationQueryUpdateRequired` | `0x2BC40` | 46 | UnwindData |  |
| 122 | `WinStationRemoveLicense` | `0x2BC80` | 46 | UnwindData |  |
| 123 | `WinStationRenameA` | `0x2BCC0` | 46 | UnwindData |  |
| 124 | `WinStationRenameW` | `0x2BD00` | 46 | UnwindData |  |
| 134 | `WinStationSetInformationA` | `0x2BD40` | 46 | UnwindData |  |
| 137 | `WinStationSetPoolCount` | `0x2BD80` | 46 | UnwindData |  |
| 157 | `_NWLogonQueryAdmin` | `0x2BDC0` | 46 | UnwindData |  |
| 158 | `_NWLogonSetAdmin` | `0x2BE00` | 46 | UnwindData |  |
| 159 | `_WinStationAnnoyancePopup` | `0x2BE40` | 46 | UnwindData |  |
| 161 | `_WinStationBreakPoint` | `0x2BE80` | 46 | UnwindData |  |
| 162 | `_WinStationCallback` | `0x2BEC0` | 46 | UnwindData |  |
| 163 | `_WinStationCheckForApplicationName` | `0x2BF00` | 46 | UnwindData |  |
| 164 | `_WinStationFUSCanRemoteUserDisconnect` | `0x2BF40` | 46 | UnwindData |  |
| 165 | `_WinStationGetApplicationInfo` | `0x2BF80` | 46 | UnwindData |  |
| 166 | `_WinStationNotifyDisconnectPipe` | `0x2BFC0` | 46 | UnwindData |  |
| 167 | `_WinStationNotifyLogoff` | `0x2C000` | 46 | UnwindData |  |
| 168 | `_WinStationNotifyLogon` | `0x2C040` | 46 | UnwindData |  |
| 169 | `_WinStationNotifyNewSession` | `0x2C080` | 46 | UnwindData |  |
| 170 | `_WinStationOpenSessionDirectory` | `0x2C0C0` | 46 | UnwindData |  |
| 171 | `_WinStationReInitializeSecurity` | `0x2C100` | 46 | UnwindData |  |
| 177 | `_WinStationUpdateClientCachedCredentials` | `0x2C140` | 46 | UnwindData |  |
| 178 | `_WinStationUpdateSettings` | `0x2C180` | 46 | UnwindData |  |
| 179 | `_WinStationUpdateUserConfig` | `0x2C1C0` | 46 | UnwindData |  |
| 107 | `WinStationQuerySessionVirtualIP` | `0x2E2C0` | 396 | UnwindData |  |
| 138 | `WinStationSetRenderHint` | `0x2E460` | 157 | UnwindData |  |

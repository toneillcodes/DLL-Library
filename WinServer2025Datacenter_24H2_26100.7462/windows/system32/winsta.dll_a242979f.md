# Binary Specification: winsta.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\winsta.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `a242979f357b373ea2cda9b3438c865f5c5204808d98157a2f32ef4dc6f7e494`
* **Total Exported Functions:** 181

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 38 | `WinStationDisconnect` | `0x1310` | 203 | UnwindData |  |
| 155 | `WinStationVirtualOpenEx` | `0x1550` | 117 | UnwindData |  |
| 75 | `WinStationGetProcessSid` | `0x1CB0` | 137 | UnwindData |  |
| 65 | `WinStationGetCurrentSessionConnectionProperty` | `0x1EF0` | 391 | UnwindData |  |
| 50 | `WinStationFreeGAPMemory` | `0x2530` | 52 | UnwindData |  |
| 63 | `WinStationGetConnectionProperty` | `0x2680` | 246 | UnwindData |  |
| 58 | `WinStationGetAllProcesses` | `0x2CB0` | 609 | UnwindData |  |
| 91 | `WinStationNameFromLogonIdW` | `0x2F40` | 260 | UnwindData |  |
| 66 | `WinStationGetCurrentSessionTerminalName` | `0x3CD0` | 484 | UnwindData |  |
| 86 | `WinStationIsCurrentSessionRemoteable` | `0x44A0` | 608 | UnwindData |  |
| 101 | `WinStationQueryCurrentSessionInformation` | `0x4710` | 20 | UnwindData |  |
| 64 | `WinStationGetCurrentSessionCapabilities` | `0x4830` | 695 | UnwindData |  |
| 45 | `WinStationEnumerateW` | `0x5B80` | 139 | UnwindData |  |
| 89 | `WinStationIsSessionRemoteable` | `0x7DD0` | 520 | UnwindData |  |
| 118 | `WinStationRegisterCurrentSessionNotificationEvent` | `0x9FD0` | 30 | UnwindData |  |
| 59 | `WinStationGetAllSessionsEx` | `0xA650` | 1,484 | UnwindData |  |
| 150 | `WinStationUnRegisterNotificationEvent` | `0xAC70` | 42 | UnwindData |  |
| 149 | `WinStationUnRegisterConsoleNotification` | `0xBFD0` | 54 | UnwindData |  |
| 151 | `WinStationUnRegisterSessionNotification` | `0xBFD0` | 54 | UnwindData |  |
| 23 | `WTSUnRegisterSessionNotificationEx` | `0xC420` | 165 | UnwindData |  |
| 146 | `WinStationSystemShutdownWait` | `0xC4D0` | 207 | UnwindData |  |
| 180 | `_WinStationWaitForConnect` | `0xD1F0` | 336 | UnwindData |  |
| 88 | `WinStationIsSessionPermitted` | `0xD350` | 335 | UnwindData |  |
| 49 | `WinStationFreeEXECENVDATAEX` | `0xD630` | 109 | UnwindData |  |
| 51 | `WinStationFreeMemory` | `0xE550` | 29 | UnwindData |  |
| 79 | `WinStationGetTermSrvCountersValue` | `0xEBF0` | 343 | UnwindData |  |
| 131 | `WinStationSendWindowMessage` | `0xFC10` | 935 | UnwindData |  |
| 136 | `WinStationSetLastWinlogonNotification` | `0x102C0` | 450 | UnwindData |  |
| 94 | `WinStationOpenServerA` | `0x109D0` | 268 | UnwindData |  |
| 61 | `WinStationGetAllUserSessions` | `0x10B80` | 900 | UnwindData |  |
| 99 | `WinStationPreCreateGlassReplacementSessionEx` | `0x10F10` | 1,008 | UnwindData |  |
| 115 | `WinStationRegisterConsoleNotification` | `0x11650` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `WinStationRegisterSessionNotification` | `0x11650` | 112 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 92 | `WinStationNegotiateSession` | `0x116C0` | 574 | UnwindData |  |
| 22 | `WTSRegisterSessionNotificationEx` | `0x11910` | 154 | UnwindData |  |
| 116 | `WinStationRegisterConsoleNotificationEx` | `0x119B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `WinStationRegisterConsoleNotificationEx2` | `0x119B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `WinStationRegisterSessionNotificationEx` | `0x119B0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 30 | `WinStationCloseServer` | `0x119F0` | 36 | UnwindData |  |
| 27 | `WinStationBroadcastSystemMessage` | `0x11B00` | 758 | UnwindData |  |
| 42 | `WinStationEnumerateExW` | `0x12220` | 713 | UnwindData |  |
| 52 | `WinStationFreePropertyValue` | `0x12920` | 113 | UnwindData |  |
| 72 | `WinStationGetLoggedOnCount` | `0x12F10` | 353 | UnwindData |  |
| 97 | `WinStationOpenServerW` | `0x13080` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `WinStationWaitSystemEvent` | `0x13090` | 1,037 | UnwindData |  |
| 102 | `WinStationQueryEnforcementCore` | `0x134B0` | 486 | UnwindData |  |
| 125 | `WinStationReportLoggedOnCompleted` | `0x136A0` | 378 | UnwindData |  |
| 96 | `WinStationOpenServerExW` | `0x13990` | 144 | UnwindData |  |
| 56 | `WinStationFreeUserSessionInfo` | `0x13A30` | 53 | UnwindData |  |
| 145 | `WinStationSystemShutdownStarted` | `0x13EC0` | 360 | UnwindData |  |
| 55 | `WinStationFreeUserCredentials` | `0x14600` | 84 | UnwindData |  |
| 98 | `WinStationPreCreateGlassReplacementSession` | `0x14680` | 1,152 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 104 | `WinStationQueryInformationW` | `0x14B00` | 574 | UnwindData |  |
| 95 | `WinStationOpenServerExA` | `0x22F00` | 268 | UnwindData |  |
| 25 | `WinStationActiveSessionExists` | `0x26E70` | 279 | UnwindData |  |
| 32 | `WinStationConnectAndLockDesktop` | `0x26F90` | 288 | UnwindData |  |
| 35 | `WinStationConnectW` | `0x270C0` | 381 | UnwindData |  |
| 39 | `WinStationEnableChildSessions` | `0x27250` | 231 | UnwindData |  |
| 40 | `WinStationEnumerateA` | `0x27340` | 259 | UnwindData |  |
| 41 | `WinStationEnumerateContainerSessions` | `0x27450` | 249 | UnwindData |  |
| 44 | `WinStationEnumerateProcesses` | `0x27550` | 165 | UnwindData |  |
| 54 | `WinStationFreeUserCertificates` | `0x27600` | 59 | UnwindData |  |
| 62 | `WinStationGetChildSessionId` | `0x27650` | 250 | UnwindData |  |
| 67 | `WinStationGetDeviceId` | `0x27750` | 266 | UnwindData |  |
| 68 | `WinStationGetInitialApplication` | `0x27860` | 336 | UnwindData |  |
| 74 | `WinStationGetParentSessionId` | `0x279C0` | 286 | UnwindData |  |
| 78 | `WinStationGetSessionIds` | `0x27AF0` | 378 | UnwindData |  |
| 80 | `WinStationGetUserCertificates` | `0x27C70` | 548 | UnwindData |  |
| 85 | `WinStationIsChildSessionsEnabled` | `0x27EA0` | 275 | UnwindData |  |
| 109 | `WinStationRcmShadow2` | `0x27FC0` | 344 | UnwindData |  |
| 127 | `WinStationReset` | `0x28120` | 203 | UnwindData |  |
| 128 | `WinStationRevertFromServicesSession` | `0x28200` | 212 | UnwindData |  |
| 129 | `WinStationSendMessageA` | `0x282E0` | 334 | UnwindData |  |
| 130 | `WinStationSendMessageW` | `0x28440` | 819 | UnwindData |  |
| 135 | `WinStationSetInformationW` | `0x28780` | 297 | UnwindData |  |
| 139 | `WinStationShadow` | `0x288B0` | 373 | UnwindData |  |
| 140 | `WinStationShadowAccessCheck` | `0x28A30` | 289 | UnwindData |  |
| 141 | `WinStationShadowStop` | `0x28B60` | 323 | UnwindData |  |
| 142 | `WinStationShadowStop2` | `0x28CB0` | 262 | UnwindData |  |
| 143 | `WinStationShutdownSystem` | `0x28DC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `WinStationSwitchToServicesSession` | `0x28DD0` | 212 | UnwindData |  |
| 148 | `WinStationTerminateProcess` | `0x28EB0` | 401 | UnwindData |  |
| 153 | `WinStationVerify` | `0x29050` | 324 | UnwindData |  |
| 154 | `WinStationVirtualOpen` | `0x291A0` | 147 | UnwindData |  |
| 160 | `_WinStationBeepOpen` | `0x29240` | 66 | UnwindData |  |
| 174 | `_WinStationShadowTarget` | `0x29290` | 105 | UnwindData |  |
| 175 | `_WinStationShadowTarget2` | `0x29300` | 724 | UnwindData |  |
| 172 | `_WinStationReadRegistry` | `0x295E0` | 2,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 173 | `_WinStationSessionInitialized` | `0x295E0` | 2,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 176 | `_WinStationShadowTargetSetup` | `0x295E0` | 2,048 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `WinStationFreeConsoleNotification` | `0x29DE0` | 49 | UnwindData |  |
| 53 | `WinStationFreeSessionNotification` | `0x29DE0` | 49 | UnwindData |  |
| 119 | `WinStationRegisterNotificationEvent` | `0x29E20` | 28 | UnwindData |  |
| 37 | `WinStationCreateChildSessionTransport` | `0x2A2A0` | 206 | UnwindData |  |
| 133 | `WinStationSetAutologonPassword` | `0x2A380` | 236 | UnwindData |  |
| 36 | `WinStationConsumeCacheSession` | `0x2A6C0` | 262 | UnwindData |  |
| 71 | `WinStationGetLastWinlogonNotification` | `0x2A7D0` | 359 | UnwindData |  |
| 76 | `WinStationGetRedirectAuthInfo` | `0x2A940` | 294 | UnwindData |  |
| 77 | `WinStationGetRestrictedLogonInfo` | `0x2AA70` | 288 | UnwindData |  |
| 81 | `WinStationGetUserCredentials` | `0x2ABA0` | 803 | UnwindData |  |
| 82 | `WinStationGetUserProfile` | `0x2AED0` | 277 | UnwindData |  |
| 84 | `WinStationIsBoundToCacheTerminal` | `0x2AFF0` | 270 | UnwindData |  |
| 87 | `WinStationIsHelpAssistantSession` | `0x2B110` | 50 | UnwindData |  |
| 110 | `WinStationRedirectErrorMessage` | `0x2B150` | 215 | UnwindData |  |
| 111 | `WinStationRedirectLogonBeginPainting` | `0x2B230` | 220 | UnwindData |  |
| 112 | `WinStationRedirectLogonError` | `0x2B320` | 316 | UnwindData |  |
| 113 | `WinStationRedirectLogonMessage` | `0x2B470` | 291 | UnwindData |  |
| 114 | `WinStationRedirectLogonStatus` | `0x2B5A0` | 255 | UnwindData |  |
| 126 | `WinStationReportUIResult` | `0x2B6B0` | 212 | UnwindData |  |
| 147 | `WinStationTerminateGlassReplacementSession` | `0x2B790` | 339 | UnwindData |  |
| 152 | `WinStationUserLoginAccessCheck` | `0x2B8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 181 | `_WinStationWaitForConnectEx` | `0x2B910` | 255 | UnwindData |  |
| 2 | `LogonIdFromWinStationNameW` | `0x2BA20` | 814 | UnwindData |  |
| 60 | `WinStationGetAllSessionsW` | `0x2BD60` | 471 | UnwindData |  |
| 5 | `ServerLicensingClose` | `0x2C600` | 77 | UnwindData |  |
| 6 | `ServerLicensingDeactivateCurrentPolicy` | `0x2C660` | 164 | UnwindData |  |
| 7 | `ServerLicensingFreePolicyInformation` | `0x2C710` | 87 | UnwindData |  |
| 8 | `ServerLicensingGetAadInfo` | `0x2C770` | 335 | UnwindData |  |
| 9 | `ServerLicensingGetAvailablePolicyIds` | `0x2C8D0` | 239 | UnwindData |  |
| 10 | `ServerLicensingGetPolicy` | `0x2C9D0` | 201 | UnwindData |  |
| 11 | `ServerLicensingGetPolicyInformationA` | `0x2CAA0` | 99 | UnwindData |  |
| 12 | `ServerLicensingGetPolicyInformationW` | `0x2CB10` | 345 | UnwindData |  |
| 13 | `ServerLicensingLoadPolicy` | `0x2CC70` | 29 | UnwindData |  |
| 18 | `ServerLicensingUnloadPolicy` | `0x2CC70` | 29 | UnwindData |  |
| 14 | `ServerLicensingOpenA` | `0x2CCA0` | 43 | UnwindData |  |
| 15 | `ServerLicensingOpenW` | `0x2CCE0` | 325 | UnwindData |  |
| 16 | `ServerLicensingSetAadInfo` | `0x2CE30` | 300 | UnwindData |  |
| 17 | `ServerLicensingSetPolicy` | `0x2CF70` | 191 | UnwindData |  |
| 132 | `WinStationServerPing` | `0x2D040` | 164 | UnwindData |  |
| 1 | `LogonIdFromWinStationNameA` | `0x2D0F0` | 46 | UnwindData |  |
| 3 | `RemoteAssistancePrepareSystemRestore` | `0x2D130` | 46 | UnwindData |  |
| 4 | `ServerGetInternetConnectorStatus` | `0x2D170` | 46 | UnwindData |  |
| 19 | `ServerQueryInetConnectorInformationA` | `0x2D1B0` | 46 | UnwindData |  |
| 20 | `ServerQueryInetConnectorInformationW` | `0x2D1F0` | 46 | UnwindData |  |
| 21 | `ServerSetInternetConnectorStatus` | `0x2D230` | 46 | UnwindData |  |
| 24 | `WinStationActivateLicense` | `0x2D270` | 46 | UnwindData |  |
| 26 | `WinStationAutoReconnect` | `0x2D2B0` | 46 | UnwindData |  |
| 28 | `WinStationCheckAccess` | `0x2D2F0` | 46 | UnwindData |  |
| 29 | `WinStationCheckLoopBack` | `0x2D330` | 46 | UnwindData |  |
| 31 | `WinStationConnectA` | `0x2D370` | 46 | UnwindData |  |
| 33 | `WinStationConnectCallback` | `0x2D3B0` | 46 | UnwindData |  |
| 34 | `WinStationConnectEx` | `0x2D3F0` | 49 | UnwindData |  |
| 43 | `WinStationEnumerateLicenses` | `0x2D430` | 46 | UnwindData |  |
| 46 | `WinStationEnumerate_IndexedA` | `0x2D470` | 46 | UnwindData |  |
| 47 | `WinStationEnumerate_IndexedW` | `0x2D4B0` | 46 | UnwindData |  |
| 57 | `WinStationGenerateLicense` | `0x2D4F0` | 46 | UnwindData |  |
| 69 | `WinStationGetLanAdapterNameA` | `0x2D530` | 46 | UnwindData |  |
| 70 | `WinStationGetLanAdapterNameW` | `0x2D570` | 46 | UnwindData |  |
| 73 | `WinStationGetMachinePolicy` | `0x2D5B0` | 46 | UnwindData |  |
| 83 | `WinStationInstallLicense` | `0x2D5F0` | 46 | UnwindData |  |
| 90 | `WinStationNameFromLogonIdA` | `0x2D630` | 46 | UnwindData |  |
| 93 | `WinStationNtsdDebug` | `0x2D670` | 46 | UnwindData |  |
| 100 | `WinStationQueryAllowConcurrentConnections` | `0x2D6B0` | 46 | UnwindData |  |
| 103 | `WinStationQueryInformationA` | `0x2D6F0` | 46 | UnwindData |  |
| 105 | `WinStationQueryLicense` | `0x2D730` | 46 | UnwindData |  |
| 106 | `WinStationQueryLogonCredentialsW` | `0x2D770` | 46 | UnwindData |  |
| 108 | `WinStationQueryUpdateRequired` | `0x2D7B0` | 46 | UnwindData |  |
| 122 | `WinStationRemoveLicense` | `0x2D7F0` | 46 | UnwindData |  |
| 123 | `WinStationRenameA` | `0x2D830` | 46 | UnwindData |  |
| 124 | `WinStationRenameW` | `0x2D870` | 46 | UnwindData |  |
| 134 | `WinStationSetInformationA` | `0x2D8B0` | 46 | UnwindData |  |
| 137 | `WinStationSetPoolCount` | `0x2D8F0` | 46 | UnwindData |  |
| 157 | `_NWLogonQueryAdmin` | `0x2D930` | 46 | UnwindData |  |
| 158 | `_NWLogonSetAdmin` | `0x2D970` | 46 | UnwindData |  |
| 159 | `_WinStationAnnoyancePopup` | `0x2D9B0` | 46 | UnwindData |  |
| 161 | `_WinStationBreakPoint` | `0x2D9F0` | 46 | UnwindData |  |
| 162 | `_WinStationCallback` | `0x2DA30` | 46 | UnwindData |  |
| 163 | `_WinStationCheckForApplicationName` | `0x2DA70` | 46 | UnwindData |  |
| 164 | `_WinStationFUSCanRemoteUserDisconnect` | `0x2DAB0` | 46 | UnwindData |  |
| 165 | `_WinStationGetApplicationInfo` | `0x2DAF0` | 46 | UnwindData |  |
| 166 | `_WinStationNotifyDisconnectPipe` | `0x2DB30` | 46 | UnwindData |  |
| 167 | `_WinStationNotifyLogoff` | `0x2DB70` | 46 | UnwindData |  |
| 168 | `_WinStationNotifyLogon` | `0x2DBB0` | 46 | UnwindData |  |
| 169 | `_WinStationNotifyNewSession` | `0x2DBF0` | 46 | UnwindData |  |
| 170 | `_WinStationOpenSessionDirectory` | `0x2DC30` | 46 | UnwindData |  |
| 171 | `_WinStationReInitializeSecurity` | `0x2DC70` | 46 | UnwindData |  |
| 177 | `_WinStationUpdateClientCachedCredentials` | `0x2DCB0` | 46 | UnwindData |  |
| 178 | `_WinStationUpdateSettings` | `0x2DCF0` | 46 | UnwindData |  |
| 179 | `_WinStationUpdateUserConfig` | `0x2DD30` | 46 | UnwindData |  |
| 107 | `WinStationQuerySessionVirtualIP` | `0x2FE30` | 396 | UnwindData |  |
| 138 | `WinStationSetRenderHint` | `0x2FFD0` | 157 | UnwindData |  |

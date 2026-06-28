# Binary Specification: wlanapi.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\wlanapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `85dcd53e90c45406ab53cacb8221c725dce28f1303cdf977d82fe79599925fa3`
* **Total Exported Functions:** 286

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 202 | `WlanNotifyVsIeProviderExInt` | `0x2370` | 29 | UnwindData |  |
| 268 | `WlanTryUpgradeCurrentConnectionAuthCipher` | `0x2C80` | 2,922 | UnwindData |  |
| 189 | `WlanInternalNonDisruptiveScanEx` | `0x3F40` | 1,271 | UnwindData |  |
| 215 | `WlanPrivateQueryInterface` | `0x4440` | 643 | UnwindData |  |
| 227 | `WlanQueryInterface` | `0x46D0` | 2,024 | UnwindData |  |
| 191 | `WlanInternalScan` | `0x4EC0` | 399 | UnwindData |  |
| 19 | `QueryNetconStatus` | `0x5060` | 661 | UnwindData |  |
| 204 | `WlanOpenHandle` | `0x5300` | 893 | UnwindData |  |
| 187 | `WlanInternalGetNetworkBssListWithFTMData` | `0x6390` | 78 | UnwindData |  |
| 156 | `WlanGetNetworkBssList` | `0x6870` | 2,044 | UnwindData |  |
| 163 | `WlanGetProfileMetadataWithProfileGuid` | `0x70D0` | 1,301 | UnwindData |  |
| 131 | `WlanAllocateMemory` | `0x7AB0` | 140 | UnwindData |  |
| 7 | `AcmGenerateConnectionId` | `0x7D00` | 66 | UnwindData |  |
| 9 | `AcmGenerateNetworkId` | `0x7DF0` | 81 | UnwindData |  |
| 271 | `WlanUtf8SsidToDisplayName` | `0x8410` | 312 | UnwindData |  |
| 234 | `WlanRegisterNotification` | `0x8980` | 29 | UnwindData |  |
| 134 | `WlanCloseHandle` | `0x9070` | 543 | UnwindData |  |
| 211 | `WlanPrivateGetAvailableNetworkList` | `0x9C80` | 1,492 | UnwindData |  |
| 145 | `WlanEnumInterfaces` | `0xA520` | 740 | UnwindData |  |
| 245 | `WlanSetInterface` | `0xABC0` | 523 | UnwindData |  |
| 212 | `WlanPrivateGetBssInfo` | `0xADE0` | 574 | UnwindData |  |
| 140 | `WlanDeviceServiceCommand` | `0xB030` | 921 | UnwindData |  |
| 235 | `WlanRegisterVirtualStationNotification` | `0xB3D0` | 587 | UnwindData |  |
| 161 | `WlanGetProfileList` | `0xB630` | 713 | UnwindData |  |
| 157 | `WlanGetProfile` | `0xBCD0` | 1,991 | UnwindData |  |
| 206 | `WlanPrivateCanDeleteProfile` | `0xEA80` | 663 | UnwindData |  |
| 150 | `WlanGetAvailableNetworkList` | `0xFD40` | 274 | UnwindData |  |
| 160 | `WlanGetProfileIndex` | `0x10830` | 303 | UnwindData |  |
| 258 | `WlanSignalValueToBar` | `0x109E0` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `WlanGetSecuritySettings` | `0x10C20` | 753 | UnwindData |  |
| 46 | `WFDFreeMemoryInt` | `0x10F20` | 53 | UnwindData |  |
| 147 | `WlanFreeMemory` | `0x10F20` | 53 | UnwindData |  |
| 197 | `WlanLowPrivFreeMemory` | `0x10F20` | 53 | UnwindData |  |
| 162 | `WlanGetProfileMetadata` | `0x11060` | 359 | UnwindData |  |
| 153 | `WlanGetFilterList` | `0x111D0` | 592 | UnwindData |  |
| 259 | `WlanSignalValueToBarEx` | `0x11430` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `QueryNetconVirtualCharacteristic` | `0x11500` | 333 | UnwindData |  |
| 230 | `WlanQueryVirtualInterfaceType` | `0x11660` | 393 | UnwindData |  |
| 225 | `WlanQueryAutoConfigParameter` | `0x117F0` | 744 | UnwindData |  |
| 154 | `WlanGetInterfaceCapability` | `0x11CE0` | 725 | UnwindData |  |
| 250 | `WlanSetProfileList` | `0x12140` | 634 | UnwindData |  |
| 4 | `WlanWcmGetProfileList` | `0x126A0` | 400 | UnwindData |  |
| 184 | `WlanIhvControl` | `0x12840` | 882 | UnwindData |  |
| 214 | `WlanPrivateQuery11adPairedConfig` | `0x12E40` | 582 | UnwindData |  |
| 164 | `WlanGetProfileSsidList` | `0x130E0` | 533 | UnwindData |  |
| 284 | `WpParseProfileXml` | `0x133B0` | 414 | UnwindData |  |
| 167 | `WlanGetStoredRadioState` | `0x13DD0` | 300 | UnwindData |  |
| 231 | `WlanReasonCodeToString` | `0x13F90` | 101 | UnwindData |  |
| 165 | `WlanGetRadioInformation` | `0x14770` | 304 | UnwindData |  |
| 260 | `WlanSsidToDisplayName` | `0x148E0` | 585 | UnwindData |  |
| 144 | `WlanEnumAllInterfaces` | `0x14BD0` | 325 | UnwindData |  |
| 239 | `WlanScan` | `0x15030` | 771 | UnwindData |  |
| 54 | `WFDGetVisibleDevicesExInt` | `0x15340` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `WlanSetProfileMetadata` | `0x15530` | 282 | UnwindData |  |
| 151 | `WlanGetAvailableNetworkList2` | `0x156C0` | 247 | UnwindData |  |
| 176 | `WlanHostedNetworkQueryStatus` | `0x157C0` | 579 | UnwindData |  |
| 203 | `WlanNotifyVsIeProviderInt` | `0x15A10` | 29 | UnwindData |  |
| 267 | `WlanStringToUtf8Ssid` | `0x15DD0` | 294 | UnwindData |  |
| 94 | `WFDQueryPropertyInt` | `0x15F10` | 2,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `WlanRegisterDeviceServiceNotification` | `0x16A80` | 607 | UnwindData |  |
| 218 | `WlanPrivateSetInterface` | `0x17290` | 510 | UnwindData |  |
| 30 | `WFDCloseHandle` | `0x17AB0` | 1,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `WFDCloseHandleInt` | `0x17AB0` | 1,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `WlanPrivateSetProfile` | `0x18090` | 658 | UnwindData |  |
| 159 | `WlanGetProfileEapUserDataInfo` | `0x18330` | 278 | UnwindData |  |
| 51 | `WFDGetPrimaryAdapterStateInt` | `0x18450` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `WFDOpenHandle` | `0x18460` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `WFDOpenHandleInt` | `0x18460` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `WFDSetPropertyInt` | `0x186B0` | 3,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `WFDRegisterNotificationInt` | `0x19360` | 43 | UnwindData |  |
| 130 | `WiFiDisplaySetSinkStateInt` | `0x194D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `WFDDiscoverDevicesExInt` | `0x194E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `WFDLowPrivIsWfdSupportedInt` | `0x194F0` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `WiFiDisplayResetSinkStateInt` | `0x195D0` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `WiFiDisplaySetSinkClientHandleInt` | `0x19B10` | 18,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `WlanConnect` | `0x1E400` | 84 | UnwindData |  |
| 136 | `WlanConnectEx` | `0x1E460` | 84 | UnwindData |  |
| 139 | `WlanDeleteProfile` | `0x1E4C0` | 23 | UnwindData |  |
| 141 | `WlanDisconnect` | `0x1E4E0` | 754 | UnwindData |  |
| 146 | `WlanExtractPsdIEDataList` | `0x1E7E0` | 1,155 | UnwindData |  |
| 158 | `WlanGetProfileCustomUserData` | `0x1EC70` | 710 | UnwindData |  |
| 168 | `WlanGetSupportedDeviceServices` | `0x1EF40` | 622 | UnwindData |  |
| 169 | `WlanHostedNetworkForceStart` | `0x1F1C0` | 177 | UnwindData |  |
| 170 | `WlanHostedNetworkForceStop` | `0x1F280` | 177 | UnwindData |  |
| 173 | `WlanHostedNetworkInitSettings` | `0x1F340` | 177 | UnwindData |  |
| 174 | `WlanHostedNetworkQueryProperty` | `0x1F400` | 655 | UnwindData |  |
| 175 | `WlanHostedNetworkQuerySecondaryKey` | `0x1F6A0` | 829 | UnwindData |  |
| 178 | `WlanHostedNetworkRefreshSecuritySettings` | `0x1F9F0` | 177 | UnwindData |  |
| 179 | `WlanHostedNetworkSetProperty` | `0x1FAB0` | 681 | UnwindData |  |
| 180 | `WlanHostedNetworkSetSecondaryKey` | `0x1FD60` | 706 | UnwindData |  |
| 182 | `WlanHostedNetworkStartUsing` | `0x20030` | 174 | UnwindData |  |
| 183 | `WlanHostedNetworkStopUsing` | `0x200F0` | 177 | UnwindData |  |
| 208 | `WlanPrivateDeleteProfile` | `0x201B0` | 602 | UnwindData |  |
| 216 | `WlanPrivateQuerySignalStrength` | `0x20410` | 376 | UnwindData |  |
| 237 | `WlanRenameProfile` | `0x20590` | 621 | UnwindData |  |
| 238 | `WlanSaveTemporaryProfile` | `0x20810` | 662 | UnwindData |  |
| 242 | `WlanSetAutoConfigParameter` | `0x20AB0` | 494 | UnwindData |  |
| 244 | `WlanSetFilterList` | `0x20CB0` | 482 | UnwindData |  |
| 246 | `WlanSetProfile` | `0x20EA0` | 73 | UnwindData |  |
| 247 | `WlanSetProfileCustomUserData` | `0x20EF0` | 645 | UnwindData |  |
| 248 | `WlanSetProfileEapUserData` | `0x21180` | 688 | UnwindData |  |
| 249 | `WlanSetProfileEapXmlUserData` | `0x21440` | 1,525 | UnwindData |  |
| 98 | `WFDSetAdditionalIEsInt` | `0x21A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WlanGetProfileKeyInfo` | `0x21A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `WlanQueryPreConnectInput` | `0x21A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `WlanSetProfileListForOffload` | `0x21A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `WlanWfdStartGO` | `0x21A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `WlanWfdStopGO` | `0x21A40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `WlanSetProfilePosition` | `0x21A50` | 633 | UnwindData |  |
| 255 | `WlanSetPsdIEDataList` | `0x21CD0` | 511 | UnwindData |  |
| 256 | `WlanSetSecuritySettings` | `0x21EE0` | 577 | UnwindData |  |
| 269 | `WlanUpdateBasicProfileSecurity` | `0x22130` | 631 | UnwindData |  |
| 28 | `WFDCancelOpenSession` | `0x223B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `WFDCancelOpenSessionInt` | `0x223B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `WFDCloseSession` | `0x223C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `WFDCloseSessionInt` | `0x223C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `WFDOpenLegacySession` | `0x223D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `WFDStartOpenSession` | `0x223E0` | 37 | UnwindData |  |
| 127 | `WFDUpdateDeviceVisibility` | `0x22410` | 20,032 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `WlanWcmDisconnect` | `0x27250` | 218 | UnwindData |  |
| 3 | `WlanWcmGetInterface` | `0x27330` | 279 | UnwindData |  |
| 5 | `WlanWcmSetInterface` | `0x27450` | 274 | UnwindData |  |
| 6 | `WlanWcmSetProfile` | `0x27570` | 460 | UnwindData |  |
| 27 | `WFDCancelListenerPairWithOOB` | `0x280A0` | 723 | UnwindData |  |
| 33 | `WFDCloseOOBPairingSession` | `0x28380` | 653 | UnwindData |  |
| 50 | `WFDGetOOBBlob` | `0x28620` | 808 | UnwindData |  |
| 56 | `WFDIsInterfaceWiFiDirect` | `0x28950` | 292 | UnwindData |  |
| 57 | `WFDIsWiFiDirectRunningOnWiFiAdapter` | `0x28A80` | 252 | UnwindData |  |
| 90 | `WFDParseOOBBlob` | `0x28B90` | 207 | UnwindData |  |
| 91 | `WFDParseOOBBlobTypeAndGetPayloadInt` | `0x28C70` | 349 | UnwindData |  |
| 104 | `WFDStartListenerPairWithOOB` | `0x28DE0` | 1,669 | UnwindData |  |
| 133 | `WlanCancelPlap` | `0x295C0` | 217 | UnwindData |  |
| 137 | `WlanConnectWithInput` | `0x296A0` | 652 | UnwindData |  |
| 138 | `WlanDeinitPlapParams` | `0x29940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `WlanDoPlap` | `0x29960` | 4,370 | UnwindData |  |
| 143 | `WlanDoesBssMatchSecurity` | `0x2AA80` | 449 | UnwindData |  |
| 155 | `WlanGetMFPNegotiated` | `0x2AC50` | 248 | UnwindData |  |
| 171 | `WlanHostedNetworkFreeWCNSettings` | `0x2AD50` | 173 | UnwindData |  |
| 172 | `WlanHostedNetworkHlpQueryEverUsed` | `0x2AE10` | 194 | UnwindData |  |
| 177 | `WlanHostedNetworkQueryWCNSettings` | `0x2AEE0` | 224 | UnwindData |  |
| 181 | `WlanHostedNetworkSetWCNSettings` | `0x2AFD0` | 224 | UnwindData |  |
| 185 | `WlanInitPlapParams` | `0x2B0C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `WlanInternalCancelFTMRequest` | `0x2B0E0` | 494 | UnwindData |  |
| 188 | `WlanInternalNonDisruptiveScan` | `0x2B2E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `WlanInternalRequestFTM` | `0x2B2F0` | 1,278 | UnwindData |  |
| 193 | `WlanIsNetworkSuppressed` | `0x2B800` | 409 | UnwindData |  |
| 194 | `WlanIsUIRequestPending` | `0x2B9A0` | 297 | UnwindData |  |
| 207 | `WlanPrivateClearAnqpCache` | `0x2BAD0` | 253 | UnwindData |  |
| 209 | `WlanPrivateGetAnqpCacheResponse` | `0x2BBE0` | 313 | UnwindData |  |
| 210 | `WlanPrivateGetAnqpVenueUrl` | `0x2BD20` | 335 | UnwindData |  |
| 213 | `WlanPrivateParseAnqpRawData` | `0x2BE80` | 315 | UnwindData |  |
| 217 | `WlanPrivateRefreshAnqpCache` | `0x2BFD0` | 299 | UnwindData |  |
| 219 | `WlanPrivateSetLocationPrivacyFlags` | `0x2C110` | 166 | UnwindData |  |
| 228 | `WlanQueryPlapCredentials` | `0x2C1C0` | 366 | UnwindData |  |
| 232 | `WlanRefreshConnections` | `0x2C340` | 259 | UnwindData |  |
| 236 | `WlanRemoveUIForwardingNetworkList` | `0x2C450` | 217 | UnwindData |  |
| 240 | `WlanSendUIResponse` | `0x2C530` | 235 | UnwindData |  |
| 254 | `WlanSetProtectedScenario` | `0x2C630` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `WlanSetUIForwardingNetworkList` | `0x2C640` | 269 | UnwindData |  |
| 261 | `WlanStartAP` | `0x2C760` | 981 | UnwindData |  |
| 262 | `WlanStartMovementDetector` | `0x2CB40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `WlanStopAP` | `0x2CB50` | 246 | UnwindData |  |
| 264 | `WlanStopMovementDetector` | `0x2CC50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `WlanStoreRadioStateOnEnteringAirPlaneMode` | `0x2CC60` | 270 | UnwindData |  |
| 270 | `WlanUpdateProfileWithAuthCipher` | `0x2CD80` | 618 | UnwindData |  |
| 274 | `WlanWfdGOSetWCNSettings` | `0x2CFF0` | 242 | UnwindData |  |
| 275 | `WlanWfdGetPeerInfo` | `0x2D0F0` | 317 | UnwindData |  |
| 23 | `WFDAbortSessionInt` | `0x2DB20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `WFDAcceptConnectRequestAndOpenSessionInt` | `0x2DB30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `WFDAcceptGroupRequestAndOpenSessionInt` | `0x2DB40` | 102 | UnwindData |  |
| 32 | `WFDCloseLegacySessionInt` | `0x2DBB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `WFDConfigureFirewallForSessionInt` | `0x2DBC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `WFDCreateDHPrivatePublicKeyPairInt` | `0x2DBD0` | 18 | UnwindData |  |
| 38 | `WFDDeclineConnectRequestInt` | `0x2DBF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `WFDDeclineGroupRequestInt` | `0x2DC00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `WFDDiscoverDeviceServiceInformationInt` | `0x2DC10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `WFDDiscoverDevicesInt` | `0x2DC20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `WFDFlushVisibleDeviceListInt` | `0x2DC30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `WFDForceDisconnectInt` | `0x2DC40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `WFDForceDisconnectLegacyPeerInt` | `0x2DC50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `WFDGetDefaultGroupProfileInt` | `0x2DC60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `WFDGetDeviceDescriptorForPendingRequestInt` | `0x2DC70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `WFDGetNFCCarrierConfigBlobInt` | `0x2DC80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `WFDGetProfileKeyInfoInt` | `0x2DC90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `WFDGetSessionEndpointPairsInt` | `0x2DCA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `WFDGetVisibleDevicesInt` | `0x2DCB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `WFDOpenLegacySessionInt` | `0x2DCC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `WFDPairCancelByDeviceAddressInt` | `0x2DCD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `WFDPairCancelInt` | `0x2DCE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `WFDPairContinuePairWithDeviceInt` | `0x2DCF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `WFDPairEnumerateCeremoniesInt` | `0x2DD00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `WFDPairSelectCeremonyInt` | `0x2DD10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `WFDPairWithDeviceAndOpenSessionExInt` | `0x2DD20` | 60 | UnwindData |  |
| 89 | `WFDPairWithDeviceAndOpenSessionInt` | `0x2DD70` | 53 | UnwindData |  |
| 92 | `WFDParseProfileXmlInt` | `0x2DDB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `WFDParseWfaNfcCarrierConfigBlobInt` | `0x2DDC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `WFDRegisterVMgrCallerInt` | `0x2DDD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `WFDResetSelectedWfdMgrInt` | `0x2DDE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `WFDSetSecondaryDeviceTypeListInt` | `0x2DDF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `WFDSetSelectedWfdMgrInt` | `0x2DE00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `WFDStartBackgroundDiscoveryInt` | `0x2DE10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `WFDStartOffloadedDiscoveryInt` | `0x2DE20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `WFDStartOpenSessionInt` | `0x2DE30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `WFDStartUsingGroupExInt` | `0x2DE40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `WFDStartUsingGroupInt` | `0x2DE50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `WFDStopBackgroundDiscoveryInt` | `0x2DE60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `WFDStopDiscoverDevicesExInt` | `0x2DE70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `WFDStopDiscoverDevicesInt` | `0x2DE80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `WFDStopOffloadedDiscoveryInt` | `0x2DE90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `WFDStopUsingGroupInt` | `0x2DEA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `WFDUnregisterVMgrCallerInt` | `0x2DEB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `WlanVMgrQueryCurrentScenariosInt` | `0x2DEC0` | 1,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `WFDCancelConnectorPairWithOOB` | `0x2E4F0` | 259 | UnwindData |  |
| 103 | `WFDStartConnectorPairWithOOB` | `0x2E600` | 463 | UnwindData |  |
| 58 | `WFDLowPrivCancelOpenSessionInt` | `0x2E980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `WFDLowPrivCloseHandleInt` | `0x2E990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `WFDLowPrivCloseLegacySessionInt` | `0x2E9A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `WFDLowPrivCloseSessionInt` | `0x2E9B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `WFDLowPrivConfigureFirewallForSessionInt` | `0x2E9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `WFDLowPrivDeclineDeviceApiConnectionRequestInt` | `0x2E9D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `WFDLowPrivGetPendingGroupRequestDetailsInt` | `0x2E9E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `WFDLowPrivGetSessionEndpointPairsInt` | `0x2E9F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `WFDLowPrivOpenHandleInt` | `0x2EA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `WFDLowPrivOpenLegacySessionInt` | `0x2EA10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `WFDLowPrivOpenSessionByDafObjectIdInt` | `0x2EA20` | 99 | UnwindData |  |
| 70 | `WFDLowPrivQueryPropertyInt` | `0x2EA90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `WFDLowPrivRegisterNotificationInt` | `0x2EAA0` | 46 | UnwindData |  |
| 72 | `WFDLowPrivRegisterVMgrCallerInt` | `0x2EAE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `WFDLowPrivSetPropertyInt` | `0x2EAF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `WFDLowPrivStartDeviceApiConnectionRequestListenerInt` | `0x2EB00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `WFDLowPrivStartUsingGroupInt` | `0x2EB10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `WFDLowPrivStopDeviceApiConnectionRequestListenerInt` | `0x2EB20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `WFDLowPrivStopUsingGroupInt` | `0x2EB30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `WFDLowPrivUnregisterVMgrCallerInt` | `0x2EB40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `WFDSvcLowPrivAcceptSessionInt` | `0x2EB50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `WFDSvcLowPrivCancelSessionInt` | `0x2EB60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `WFDSvcLowPrivCloseSessionInt` | `0x2EB70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `WFDSvcLowPrivConfigureSessionInt` | `0x2EB80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `WFDSvcLowPrivConnectSessionInt` | `0x2EB90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `WFDSvcLowPrivGetProvisioningInfoInt` | `0x2EBA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `WFDSvcLowPrivGetSessionEndpointPairsInt` | `0x2EBB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `WFDSvcLowPrivOpenAdvertiserSessionInt` | `0x2EBC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `WFDSvcLowPrivOpenSeekerSessionInt` | `0x2EBD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `WFDSvcLowPrivPublishServiceInt` | `0x2EBE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `WFDSvcLowPrivUnpublishServiceInt` | `0x2EBF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `WlanLowPrivCloseHandle` | `0x2EC00` | 445 | UnwindData |  |
| 196 | `WlanLowPrivEnumInterfaces` | `0x2EDD0` | 566 | UnwindData |  |
| 198 | `WlanLowPrivNotifyVsIeProviderInt` | `0x2F010` | 29 | UnwindData |  |
| 199 | `WlanLowPrivOpenHandle` | `0x2F040` | 795 | UnwindData |  |
| 200 | `WlanLowPrivQueryInterface` | `0x2F370` | 621 | UnwindData |  |
| 201 | `WlanLowPrivSetInterface` | `0x2F5F0` | 522 | UnwindData |  |
| 148 | `WlanGenerateProfileXmlBasicSettings` | `0x2FA30` | 90 | UnwindData |  |
| 149 | `WlanGenerateProfileXmlBasicSettingsWithTransitionMode` | `0x2FA90` | 1,053 | UnwindData |  |
| 205 | `WlanParseProfileXmlBasicSettings` | `0x2FEC0` | 623 | UnwindData |  |
| 226 | `WlanQueryCreateAllUserProfileRestricted` | `0x304C0` | 855 | UnwindData |  |
| 241 | `WlanSetAllUserProfileRestricted` | `0x30820` | 331 | UnwindData |  |
| 192 | `WlanIsActiveConsoleUser` | `0x386B0` | 316 | UnwindData |  |
| 266 | `WlanStringToSsid` | `0x38800` | 215 | UnwindData |  |
| 132 | `WlanAllocateProfileIpConfiguration` | `0x38AD0` | 253 | UnwindData |  |
| 221 | `WlanProfileIpConfigurationGetAddressList` | `0x38BE0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `WlanProfileIpConfigurationGetDnsServerConfigurationList` | `0x38C10` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `WlanProfileIpConfigurationGetDnsServerList` | `0x38C50` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `WlanProfileIpConfigurationGetGatewayList` | `0x38C80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `WlanVerifyProfileIpConfiguration` | `0x38CB0` | 251 | UnwindData |  |
| 10 | `ConvertFrequencyToBandChannel` | `0x39F10` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ConvertPassPhraseKeyStringToBuffer` | `0x3A2F0` | 289 | UnwindData |  |
| 21 | `ShouldUseWlanString` | `0x3A420` | 99 | UnwindData |  |
| 22 | `SsidToStringW` | `0x3A490` | 42 | UnwindData |  |
| 8 | `AcmGenerateConnectionIdForNotification` | `0x3C820` | 132 | UnwindData |  |
| 12 | `FreeMSMSecConfig` | `0x3DAA0` | 121 | UnwindData |  |
| 13 | `MSMSecCreateDefaultProfileStatic` | `0x3DB20` | 691 | UnwindData |  |
| 16 | `MSMSecProfileValidForSafeMode` | `0x3DDE0` | 14,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MSMSecGetCopyOfSupportedAuthCiphers` | `0x414D0` | 118 | UnwindData |  |
| 15 | `MSMSecGetNetworkCapabilitiesFromBSSDescriptionList` | `0x41550` | 560 | UnwindData |  |
| 17 | `MSMSecSanitizeAuthCipherList` | `0x41AB0` | 317 | UnwindData |  |
| 18 | `MSMSecValidateL2UIRequest` | `0x41C00` | 832 | UnwindData |  |
| 278 | `WpAllocMemory` | `0x43330` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `WpDuplicateProfile` | `0x43340` | 265 | UnwindData |  |
| 280 | `WpFreeMemory` | `0x43450` | 20 | UnwindData |  |
| 281 | `WpFreeProfile` | `0x43470` | 57 | UnwindData |  |
| 282 | `WpGenerateProfileXml` | `0x434B0` | 252 | UnwindData |  |
| 283 | `WpLoadProfile` | `0x435C0` | 319 | UnwindData |  |
| 285 | `WpSaveProfile` | `0x43A10` | 178 | UnwindData |  |
| 286 | `WpValidateProfile` | `0x43AD0` | 23,168 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `WlanGetExtensibilityInfo` | `0x49550` | 875 | UnwindData |  |
| 243 | `WlanSetExtensibilityInfo` | `0x498D0` | 501 | UnwindData |  |

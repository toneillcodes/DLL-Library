# Binary Specification: wlanapi.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\wlanapi.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `d98272cd6ed69dd6eef0d38ac6d46156c03af08459a400212357300e20b1fc12`
* **Total Exported Functions:** 286

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 202 | `WlanNotifyVsIeProviderExInt` | `0x23A0` | 29 | UnwindData |  |
| 268 | `WlanTryUpgradeCurrentConnectionAuthCipher` | `0x2CB0` | 2,922 | UnwindData |  |
| 189 | `WlanInternalNonDisruptiveScanEx` | `0x3F70` | 1,271 | UnwindData |  |
| 215 | `WlanPrivateQueryInterface` | `0x4470` | 643 | UnwindData |  |
| 227 | `WlanQueryInterface` | `0x4700` | 2,024 | UnwindData |  |
| 191 | `WlanInternalScan` | `0x4EF0` | 399 | UnwindData |  |
| 19 | `QueryNetconStatus` | `0x5090` | 661 | UnwindData |  |
| 204 | `WlanOpenHandle` | `0x5330` | 893 | UnwindData |  |
| 187 | `WlanInternalGetNetworkBssListWithFTMData` | `0x63C0` | 78 | UnwindData |  |
| 156 | `WlanGetNetworkBssList` | `0x68A0` | 2,044 | UnwindData |  |
| 163 | `WlanGetProfileMetadataWithProfileGuid` | `0x7100` | 1,301 | UnwindData |  |
| 131 | `WlanAllocateMemory` | `0x7AE0` | 140 | UnwindData |  |
| 7 | `AcmGenerateConnectionId` | `0x7D30` | 66 | UnwindData |  |
| 9 | `AcmGenerateNetworkId` | `0x7E20` | 81 | UnwindData |  |
| 271 | `WlanUtf8SsidToDisplayName` | `0x8440` | 312 | UnwindData |  |
| 234 | `WlanRegisterNotification` | `0x89B0` | 29 | UnwindData |  |
| 134 | `WlanCloseHandle` | `0x90A0` | 543 | UnwindData |  |
| 211 | `WlanPrivateGetAvailableNetworkList` | `0x9CB0` | 1,492 | UnwindData |  |
| 145 | `WlanEnumInterfaces` | `0xA550` | 740 | UnwindData |  |
| 245 | `WlanSetInterface` | `0xABF0` | 523 | UnwindData |  |
| 212 | `WlanPrivateGetBssInfo` | `0xAE10` | 574 | UnwindData |  |
| 140 | `WlanDeviceServiceCommand` | `0xB060` | 921 | UnwindData |  |
| 235 | `WlanRegisterVirtualStationNotification` | `0xB400` | 587 | UnwindData |  |
| 161 | `WlanGetProfileList` | `0xB660` | 713 | UnwindData |  |
| 157 | `WlanGetProfile` | `0xBD00` | 1,991 | UnwindData |  |
| 206 | `WlanPrivateCanDeleteProfile` | `0xEAB0` | 663 | UnwindData |  |
| 150 | `WlanGetAvailableNetworkList` | `0xFD70` | 274 | UnwindData |  |
| 160 | `WlanGetProfileIndex` | `0x10860` | 303 | UnwindData |  |
| 258 | `WlanSignalValueToBar` | `0x10A10` | 576 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 166 | `WlanGetSecuritySettings` | `0x10C50` | 753 | UnwindData |  |
| 46 | `WFDFreeMemoryInt` | `0x10F50` | 53 | UnwindData |  |
| 147 | `WlanFreeMemory` | `0x10F50` | 53 | UnwindData |  |
| 197 | `WlanLowPrivFreeMemory` | `0x10F50` | 53 | UnwindData |  |
| 162 | `WlanGetProfileMetadata` | `0x11090` | 359 | UnwindData |  |
| 153 | `WlanGetFilterList` | `0x11200` | 592 | UnwindData |  |
| 259 | `WlanSignalValueToBarEx` | `0x11460` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 20 | `QueryNetconVirtualCharacteristic` | `0x11530` | 333 | UnwindData |  |
| 230 | `WlanQueryVirtualInterfaceType` | `0x11690` | 393 | UnwindData |  |
| 225 | `WlanQueryAutoConfigParameter` | `0x11820` | 744 | UnwindData |  |
| 154 | `WlanGetInterfaceCapability` | `0x11D10` | 725 | UnwindData |  |
| 250 | `WlanSetProfileList` | `0x12170` | 634 | UnwindData |  |
| 4 | `WlanWcmGetProfileList` | `0x126D0` | 400 | UnwindData |  |
| 184 | `WlanIhvControl` | `0x12870` | 882 | UnwindData |  |
| 214 | `WlanPrivateQuery11adPairedConfig` | `0x12E70` | 582 | UnwindData |  |
| 164 | `WlanGetProfileSsidList` | `0x13110` | 533 | UnwindData |  |
| 284 | `WpParseProfileXml` | `0x133E0` | 414 | UnwindData |  |
| 167 | `WlanGetStoredRadioState` | `0x13E00` | 300 | UnwindData |  |
| 231 | `WlanReasonCodeToString` | `0x13FC0` | 101 | UnwindData |  |
| 165 | `WlanGetRadioInformation` | `0x147A0` | 304 | UnwindData |  |
| 260 | `WlanSsidToDisplayName` | `0x14910` | 585 | UnwindData |  |
| 144 | `WlanEnumAllInterfaces` | `0x14C00` | 325 | UnwindData |  |
| 239 | `WlanScan` | `0x15060` | 771 | UnwindData |  |
| 54 | `WFDGetVisibleDevicesExInt` | `0x15370` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 252 | `WlanSetProfileMetadata` | `0x15560` | 282 | UnwindData |  |
| 151 | `WlanGetAvailableNetworkList2` | `0x156F0` | 247 | UnwindData |  |
| 176 | `WlanHostedNetworkQueryStatus` | `0x157F0` | 579 | UnwindData |  |
| 203 | `WlanNotifyVsIeProviderInt` | `0x15A40` | 29 | UnwindData |  |
| 267 | `WlanStringToUtf8Ssid` | `0x15E00` | 294 | UnwindData |  |
| 94 | `WFDQueryPropertyInt` | `0x15F40` | 2,928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 233 | `WlanRegisterDeviceServiceNotification` | `0x16AB0` | 607 | UnwindData |  |
| 218 | `WlanPrivateSetInterface` | `0x172C0` | 510 | UnwindData |  |
| 30 | `WFDCloseHandle` | `0x17AE0` | 1,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 31 | `WFDCloseHandleInt` | `0x17AE0` | 1,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 220 | `WlanPrivateSetProfile` | `0x180C0` | 658 | UnwindData |  |
| 159 | `WlanGetProfileEapUserDataInfo` | `0x18360` | 278 | UnwindData |  |
| 51 | `WFDGetPrimaryAdapterStateInt` | `0x18480` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `WFDOpenHandle` | `0x18490` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `WFDOpenHandleInt` | `0x18490` | 592 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `WFDSetPropertyInt` | `0x186E0` | 3,248 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 95 | `WFDRegisterNotificationInt` | `0x19390` | 43 | UnwindData |  |
| 130 | `WiFiDisplaySetSinkStateInt` | `0x19500` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 41 | `WFDDiscoverDevicesExInt` | `0x19510` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 66 | `WFDLowPrivIsWfdSupportedInt` | `0x19520` | 224 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 128 | `WiFiDisplayResetSinkStateInt` | `0x19600` | 1,344 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 129 | `WiFiDisplaySetSinkClientHandleInt` | `0x19B40` | 18,672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 135 | `WlanConnect` | `0x1E430` | 84 | UnwindData |  |
| 136 | `WlanConnectEx` | `0x1E490` | 84 | UnwindData |  |
| 139 | `WlanDeleteProfile` | `0x1E4F0` | 23 | UnwindData |  |
| 141 | `WlanDisconnect` | `0x1E510` | 754 | UnwindData |  |
| 146 | `WlanExtractPsdIEDataList` | `0x1E810` | 1,155 | UnwindData |  |
| 158 | `WlanGetProfileCustomUserData` | `0x1ECA0` | 710 | UnwindData |  |
| 168 | `WlanGetSupportedDeviceServices` | `0x1EF70` | 622 | UnwindData |  |
| 169 | `WlanHostedNetworkForceStart` | `0x1F1F0` | 177 | UnwindData |  |
| 170 | `WlanHostedNetworkForceStop` | `0x1F2B0` | 177 | UnwindData |  |
| 173 | `WlanHostedNetworkInitSettings` | `0x1F370` | 177 | UnwindData |  |
| 174 | `WlanHostedNetworkQueryProperty` | `0x1F430` | 655 | UnwindData |  |
| 175 | `WlanHostedNetworkQuerySecondaryKey` | `0x1F6D0` | 829 | UnwindData |  |
| 178 | `WlanHostedNetworkRefreshSecuritySettings` | `0x1FA20` | 177 | UnwindData |  |
| 179 | `WlanHostedNetworkSetProperty` | `0x1FAE0` | 681 | UnwindData |  |
| 180 | `WlanHostedNetworkSetSecondaryKey` | `0x1FD90` | 706 | UnwindData |  |
| 182 | `WlanHostedNetworkStartUsing` | `0x20060` | 174 | UnwindData |  |
| 183 | `WlanHostedNetworkStopUsing` | `0x20120` | 177 | UnwindData |  |
| 208 | `WlanPrivateDeleteProfile` | `0x201E0` | 602 | UnwindData |  |
| 216 | `WlanPrivateQuerySignalStrength` | `0x20440` | 376 | UnwindData |  |
| 237 | `WlanRenameProfile` | `0x205C0` | 621 | UnwindData |  |
| 238 | `WlanSaveTemporaryProfile` | `0x20840` | 662 | UnwindData |  |
| 242 | `WlanSetAutoConfigParameter` | `0x20AE0` | 494 | UnwindData |  |
| 244 | `WlanSetFilterList` | `0x20CE0` | 482 | UnwindData |  |
| 246 | `WlanSetProfile` | `0x20ED0` | 73 | UnwindData |  |
| 247 | `WlanSetProfileCustomUserData` | `0x20F20` | 645 | UnwindData |  |
| 248 | `WlanSetProfileEapUserData` | `0x211B0` | 688 | UnwindData |  |
| 249 | `WlanSetProfileEapXmlUserData` | `0x21470` | 1,525 | UnwindData |  |
| 98 | `WFDSetAdditionalIEsInt` | `0x21A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `WlanGetProfileKeyInfo` | `0x21A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 229 | `WlanQueryPreConnectInput` | `0x21A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 251 | `WlanSetProfileListForOffload` | `0x21A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 276 | `WlanWfdStartGO` | `0x21A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 277 | `WlanWfdStopGO` | `0x21A70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 253 | `WlanSetProfilePosition` | `0x21A80` | 633 | UnwindData |  |
| 255 | `WlanSetPsdIEDataList` | `0x21D00` | 511 | UnwindData |  |
| 256 | `WlanSetSecuritySettings` | `0x21F10` | 577 | UnwindData |  |
| 269 | `WlanUpdateBasicProfileSecurity` | `0x22160` | 631 | UnwindData |  |
| 28 | `WFDCancelOpenSession` | `0x223E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `WFDCancelOpenSessionInt` | `0x223E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 34 | `WFDCloseSession` | `0x223F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `WFDCloseSessionInt` | `0x223F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `WFDOpenLegacySession` | `0x22400` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 106 | `WFDStartOpenSession` | `0x22410` | 37 | UnwindData |  |
| 127 | `WFDUpdateDeviceVisibility` | `0x22440` | 19,744 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `WlanWcmDisconnect` | `0x27160` | 218 | UnwindData |  |
| 3 | `WlanWcmGetInterface` | `0x27240` | 279 | UnwindData |  |
| 5 | `WlanWcmSetInterface` | `0x27360` | 274 | UnwindData |  |
| 6 | `WlanWcmSetProfile` | `0x27480` | 460 | UnwindData |  |
| 27 | `WFDCancelListenerPairWithOOB` | `0x27F30` | 723 | UnwindData |  |
| 33 | `WFDCloseOOBPairingSession` | `0x28210` | 653 | UnwindData |  |
| 50 | `WFDGetOOBBlob` | `0x284B0` | 808 | UnwindData |  |
| 56 | `WFDIsInterfaceWiFiDirect` | `0x287E0` | 292 | UnwindData |  |
| 57 | `WFDIsWiFiDirectRunningOnWiFiAdapter` | `0x28910` | 252 | UnwindData |  |
| 90 | `WFDParseOOBBlob` | `0x28A20` | 207 | UnwindData |  |
| 91 | `WFDParseOOBBlobTypeAndGetPayloadInt` | `0x28B00` | 349 | UnwindData |  |
| 104 | `WFDStartListenerPairWithOOB` | `0x28C70` | 1,669 | UnwindData |  |
| 133 | `WlanCancelPlap` | `0x29450` | 217 | UnwindData |  |
| 137 | `WlanConnectWithInput` | `0x29530` | 652 | UnwindData |  |
| 138 | `WlanDeinitPlapParams` | `0x297D0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `WlanDoPlap` | `0x297F0` | 4,370 | UnwindData |  |
| 143 | `WlanDoesBssMatchSecurity` | `0x2A910` | 449 | UnwindData |  |
| 155 | `WlanGetMFPNegotiated` | `0x2AAE0` | 248 | UnwindData |  |
| 171 | `WlanHostedNetworkFreeWCNSettings` | `0x2ABE0` | 173 | UnwindData |  |
| 172 | `WlanHostedNetworkHlpQueryEverUsed` | `0x2ACA0` | 194 | UnwindData |  |
| 177 | `WlanHostedNetworkQueryWCNSettings` | `0x2AD70` | 224 | UnwindData |  |
| 181 | `WlanHostedNetworkSetWCNSettings` | `0x2AE60` | 224 | UnwindData |  |
| 185 | `WlanInitPlapParams` | `0x2AF50` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 186 | `WlanInternalCancelFTMRequest` | `0x2AF70` | 494 | UnwindData |  |
| 188 | `WlanInternalNonDisruptiveScan` | `0x2B170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 190 | `WlanInternalRequestFTM` | `0x2B180` | 1,278 | UnwindData |  |
| 193 | `WlanIsNetworkSuppressed` | `0x2B690` | 409 | UnwindData |  |
| 194 | `WlanIsUIRequestPending` | `0x2B830` | 297 | UnwindData |  |
| 207 | `WlanPrivateClearAnqpCache` | `0x2B960` | 253 | UnwindData |  |
| 209 | `WlanPrivateGetAnqpCacheResponse` | `0x2BA70` | 313 | UnwindData |  |
| 210 | `WlanPrivateGetAnqpVenueUrl` | `0x2BBB0` | 335 | UnwindData |  |
| 213 | `WlanPrivateParseAnqpRawData` | `0x2BD10` | 315 | UnwindData |  |
| 217 | `WlanPrivateRefreshAnqpCache` | `0x2BE60` | 299 | UnwindData |  |
| 219 | `WlanPrivateSetLocationPrivacyFlags` | `0x2BFA0` | 166 | UnwindData |  |
| 228 | `WlanQueryPlapCredentials` | `0x2C050` | 366 | UnwindData |  |
| 232 | `WlanRefreshConnections` | `0x2C1D0` | 259 | UnwindData |  |
| 236 | `WlanRemoveUIForwardingNetworkList` | `0x2C2E0` | 217 | UnwindData |  |
| 240 | `WlanSendUIResponse` | `0x2C3C0` | 235 | UnwindData |  |
| 254 | `WlanSetProtectedScenario` | `0x2C4C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 257 | `WlanSetUIForwardingNetworkList` | `0x2C4D0` | 269 | UnwindData |  |
| 261 | `WlanStartAP` | `0x2C5F0` | 981 | UnwindData |  |
| 262 | `WlanStartMovementDetector` | `0x2C9D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 263 | `WlanStopAP` | `0x2C9E0` | 246 | UnwindData |  |
| 264 | `WlanStopMovementDetector` | `0x2CAE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 265 | `WlanStoreRadioStateOnEnteringAirPlaneMode` | `0x2CAF0` | 270 | UnwindData |  |
| 270 | `WlanUpdateProfileWithAuthCipher` | `0x2CC10` | 618 | UnwindData |  |
| 274 | `WlanWfdGOSetWCNSettings` | `0x2CE80` | 242 | UnwindData |  |
| 275 | `WlanWfdGetPeerInfo` | `0x2CF80` | 317 | UnwindData |  |
| 23 | `WFDAbortSessionInt` | `0x2D9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `WFDAcceptConnectRequestAndOpenSessionInt` | `0x2D9D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `WFDAcceptGroupRequestAndOpenSessionInt` | `0x2D9E0` | 102 | UnwindData |  |
| 32 | `WFDCloseLegacySessionInt` | `0x2DA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `WFDConfigureFirewallForSessionInt` | `0x2DA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `WFDCreateDHPrivatePublicKeyPairInt` | `0x2DA70` | 18 | UnwindData |  |
| 38 | `WFDDeclineConnectRequestInt` | `0x2DA90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `WFDDeclineGroupRequestInt` | `0x2DAA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 40 | `WFDDiscoverDeviceServiceInformationInt` | `0x2DAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 42 | `WFDDiscoverDevicesInt` | `0x2DAC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `WFDFlushVisibleDeviceListInt` | `0x2DAD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 44 | `WFDForceDisconnectInt` | `0x2DAE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `WFDForceDisconnectLegacyPeerInt` | `0x2DAF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 47 | `WFDGetDefaultGroupProfileInt` | `0x2DB00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `WFDGetDeviceDescriptorForPendingRequestInt` | `0x2DB10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `WFDGetNFCCarrierConfigBlobInt` | `0x2DB20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 52 | `WFDGetProfileKeyInfoInt` | `0x2DB30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 53 | `WFDGetSessionEndpointPairsInt` | `0x2DB40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 55 | `WFDGetVisibleDevicesInt` | `0x2DB50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `WFDOpenLegacySessionInt` | `0x2DB60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `WFDPairCancelByDeviceAddressInt` | `0x2DB70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `WFDPairCancelInt` | `0x2DB80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 85 | `WFDPairContinuePairWithDeviceInt` | `0x2DB90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 86 | `WFDPairEnumerateCeremoniesInt` | `0x2DBA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `WFDPairSelectCeremonyInt` | `0x2DBB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 88 | `WFDPairWithDeviceAndOpenSessionExInt` | `0x2DBC0` | 60 | UnwindData |  |
| 89 | `WFDPairWithDeviceAndOpenSessionInt` | `0x2DC10` | 53 | UnwindData |  |
| 92 | `WFDParseProfileXmlInt` | `0x2DC50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `WFDParseWfaNfcCarrierConfigBlobInt` | `0x2DC60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `WFDRegisterVMgrCallerInt` | `0x2DC70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `WFDResetSelectedWfdMgrInt` | `0x2DC80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 100 | `WFDSetSecondaryDeviceTypeListInt` | `0x2DC90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | `WFDSetSelectedWfdMgrInt` | `0x2DCA0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `WFDStartBackgroundDiscoveryInt` | `0x2DCB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | `WFDStartOffloadedDiscoveryInt` | `0x2DCC0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | `WFDStartOpenSessionInt` | `0x2DCD0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | `WFDStartUsingGroupExInt` | `0x2DCE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 109 | `WFDStartUsingGroupInt` | `0x2DCF0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | `WFDStopBackgroundDiscoveryInt` | `0x2DD00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 111 | `WFDStopDiscoverDevicesExInt` | `0x2DD10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `WFDStopDiscoverDevicesInt` | `0x2DD20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | `WFDStopOffloadedDiscoveryInt` | `0x2DD30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 114 | `WFDStopUsingGroupInt` | `0x2DD40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `WFDUnregisterVMgrCallerInt` | `0x2DD50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 272 | `WlanVMgrQueryCurrentScenariosInt` | `0x2DD60` | 1,584 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `WFDCancelConnectorPairWithOOB` | `0x2E390` | 259 | UnwindData |  |
| 103 | `WFDStartConnectorPairWithOOB` | `0x2E4A0` | 463 | UnwindData |  |
| 58 | `WFDLowPrivCancelOpenSessionInt` | `0x2E820` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 59 | `WFDLowPrivCloseHandleInt` | `0x2E830` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `WFDLowPrivCloseLegacySessionInt` | `0x2E840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `WFDLowPrivCloseSessionInt` | `0x2E850` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `WFDLowPrivConfigureFirewallForSessionInt` | `0x2E860` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `WFDLowPrivDeclineDeviceApiConnectionRequestInt` | `0x2E870` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `WFDLowPrivGetPendingGroupRequestDetailsInt` | `0x2E880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | `WFDLowPrivGetSessionEndpointPairsInt` | `0x2E890` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | `WFDLowPrivOpenHandleInt` | `0x2E8A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 68 | `WFDLowPrivOpenLegacySessionInt` | `0x2E8B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 69 | `WFDLowPrivOpenSessionByDafObjectIdInt` | `0x2E8C0` | 99 | UnwindData |  |
| 70 | `WFDLowPrivQueryPropertyInt` | `0x2E930` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 71 | `WFDLowPrivRegisterNotificationInt` | `0x2E940` | 46 | UnwindData |  |
| 72 | `WFDLowPrivRegisterVMgrCallerInt` | `0x2E980` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `WFDLowPrivSetPropertyInt` | `0x2E990` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `WFDLowPrivStartDeviceApiConnectionRequestListenerInt` | `0x2E9A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `WFDLowPrivStartUsingGroupInt` | `0x2E9B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `WFDLowPrivStopDeviceApiConnectionRequestListenerInt` | `0x2E9C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 77 | `WFDLowPrivStopUsingGroupInt` | `0x2E9D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 78 | `WFDLowPrivUnregisterVMgrCallerInt` | `0x2E9E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 115 | `WFDSvcLowPrivAcceptSessionInt` | `0x2E9F0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 116 | `WFDSvcLowPrivCancelSessionInt` | `0x2EA00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | `WFDSvcLowPrivCloseSessionInt` | `0x2EA10` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 118 | `WFDSvcLowPrivConfigureSessionInt` | `0x2EA20` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 119 | `WFDSvcLowPrivConnectSessionInt` | `0x2EA30` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `WFDSvcLowPrivGetProvisioningInfoInt` | `0x2EA40` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `WFDSvcLowPrivGetSessionEndpointPairsInt` | `0x2EA50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `WFDSvcLowPrivOpenAdvertiserSessionInt` | `0x2EA60` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `WFDSvcLowPrivOpenSeekerSessionInt` | `0x2EA70` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | `WFDSvcLowPrivPublishServiceInt` | `0x2EA80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `WFDSvcLowPrivUnpublishServiceInt` | `0x2EA90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `WlanLowPrivCloseHandle` | `0x2EAA0` | 445 | UnwindData |  |
| 196 | `WlanLowPrivEnumInterfaces` | `0x2EC70` | 566 | UnwindData |  |
| 198 | `WlanLowPrivNotifyVsIeProviderInt` | `0x2EEB0` | 29 | UnwindData |  |
| 199 | `WlanLowPrivOpenHandle` | `0x2EEE0` | 795 | UnwindData |  |
| 200 | `WlanLowPrivQueryInterface` | `0x2F210` | 621 | UnwindData |  |
| 201 | `WlanLowPrivSetInterface` | `0x2F490` | 522 | UnwindData |  |
| 148 | `WlanGenerateProfileXmlBasicSettings` | `0x2F8D0` | 90 | UnwindData |  |
| 149 | `WlanGenerateProfileXmlBasicSettingsWithTransitionMode` | `0x2F930` | 1,053 | UnwindData |  |
| 205 | `WlanParseProfileXmlBasicSettings` | `0x2FD60` | 623 | UnwindData |  |
| 226 | `WlanQueryCreateAllUserProfileRestricted` | `0x30360` | 855 | UnwindData |  |
| 241 | `WlanSetAllUserProfileRestricted` | `0x306C0` | 331 | UnwindData |  |
| 192 | `WlanIsActiveConsoleUser` | `0x38550` | 316 | UnwindData |  |
| 266 | `WlanStringToSsid` | `0x386A0` | 215 | UnwindData |  |
| 132 | `WlanAllocateProfileIpConfiguration` | `0x38970` | 253 | UnwindData |  |
| 221 | `WlanProfileIpConfigurationGetAddressList` | `0x38A80` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 222 | `WlanProfileIpConfigurationGetDnsServerConfigurationList` | `0x38AB0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 223 | `WlanProfileIpConfigurationGetDnsServerList` | `0x38AF0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 224 | `WlanProfileIpConfigurationGetGatewayList` | `0x38B20` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 273 | `WlanVerifyProfileIpConfiguration` | `0x38B50` | 251 | UnwindData |  |
| 10 | `ConvertFrequencyToBandChannel` | `0x39DB0` | 992 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `ConvertPassPhraseKeyStringToBuffer` | `0x3A190` | 289 | UnwindData |  |
| 21 | `ShouldUseWlanString` | `0x3A2C0` | 99 | UnwindData |  |
| 22 | `SsidToStringW` | `0x3A330` | 42 | UnwindData |  |
| 8 | `AcmGenerateConnectionIdForNotification` | `0x3CD30` | 132 | UnwindData |  |
| 12 | `FreeMSMSecConfig` | `0x3DFF0` | 121 | UnwindData |  |
| 13 | `MSMSecCreateDefaultProfileStatic` | `0x3E070` | 691 | UnwindData |  |
| 16 | `MSMSecProfileValidForSafeMode` | `0x3E330` | 14,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 14 | `MSMSecGetCopyOfSupportedAuthCiphers` | `0x41A70` | 118 | UnwindData |  |
| 15 | `MSMSecGetNetworkCapabilitiesFromBSSDescriptionList` | `0x41AF0` | 560 | UnwindData |  |
| 17 | `MSMSecSanitizeAuthCipherList` | `0x42050` | 317 | UnwindData |  |
| 18 | `MSMSecValidateL2UIRequest` | `0x421A0` | 832 | UnwindData |  |
| 278 | `WpAllocMemory` | `0x438D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 279 | `WpDuplicateProfile` | `0x438E0` | 265 | UnwindData |  |
| 280 | `WpFreeMemory` | `0x439F0` | 20 | UnwindData |  |
| 281 | `WpFreeProfile` | `0x43A10` | 57 | UnwindData |  |
| 282 | `WpGenerateProfileXml` | `0x43A50` | 252 | UnwindData |  |
| 283 | `WpLoadProfile` | `0x43B60` | 319 | UnwindData |  |
| 285 | `WpSaveProfile` | `0x43FB0` | 178 | UnwindData |  |
| 286 | `WpValidateProfile` | `0x44070` | 23,888 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 152 | `WlanGetExtensibilityInfo` | `0x49DC0` | 875 | UnwindData |  |
| 243 | `WlanSetExtensibilityInfo` | `0x4A140` | 501 | UnwindData |  |

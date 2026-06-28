# Binary Specification: BluetoothApis.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\BluetoothApis.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `4029fe0ec19785551c9bdc538a045d1e8750d6ab390f8a8ed1a22592bbceed1e`
* **Total Exported Functions:** 98

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 8 | `BluetoothEnableDiscovery` | `0x1110` | 178 | UnwindData |  |
| 95 | `BthpRegisterForAuthentication` | `0x13A0` | 72 | UnwindData |  |
| 82 | `BluetoothUnregisterAuthentication` | `0x1620` | 22 | UnwindData |  |
| 18 | `BluetoothFindFirstDevice` | `0x1A80` | 60 | UnwindData |  |
| 15 | `BluetoothFindDeviceClose` | `0x1ED0` | 18 | UnwindData |  |
| 51 | `BluetoothGetDeviceInfo` | `0x1F80` | 30 | UnwindData |  |
| 37 | `BluetoothFindServiceClose` | `0x22A0` | 140 | UnwindData |  |
| 56 | `BluetoothIsConnectable` | `0x2340` | 160 | UnwindData |  |
| 31 | `BluetoothFindNextRadio` | `0x25B0` | 44 | UnwindData |  |
| 36 | `BluetoothFindRadioClose` | `0x27C0` | 120 | UnwindData |  |
| 13 | `BluetoothFindBrowseGroupClose` | `0x2840` | 90 | UnwindData |  |
| 14 | `BluetoothFindClassIdClose` | `0x2840` | 90 | UnwindData |  |
| 33 | `BluetoothFindProfileDescriptorClose` | `0x2840` | 90 | UnwindData |  |
| 35 | `BluetoothFindProtocolEntryClose` | `0x2840` | 90 | UnwindData |  |
| 3 | `BthpSetServiceStateEx` | `0x28A0` | 1,998 | UnwindData |  |
| 17 | `BluetoothFindFirstClassId` | `0x3080` | 66 | UnwindData |  |
| 90 | `BthpFindPnpInfo` | `0x3440` | 644 | UnwindData |  |
| 32 | `BluetoothFindNextService` | `0x36D0` | 58 | UnwindData |  |
| 92 | `BthpInnerRecord` | `0x4370` | 36 | UnwindData |  |
| 26 | `BluetoothFindNextClassId` | `0x4530` | 89 | UnwindData |  |
| 94 | `BthpNextRecord` | `0x47A0` | 39 | UnwindData |  |
| 69 | `BluetoothSdpGetAttributeValue` | `0x4940` | 475 | UnwindData |  |
| 74 | `BluetoothSdpGetString` | `0x4B30` | 99 | UnwindData |  |
| 70 | `BluetoothSdpGetContainerElementData` | `0x5070` | 209 | UnwindData |  |
| 71 | `BluetoothSdpGetElementData` | `0x5150` | 99 | UnwindData |  |
| 22 | `BluetoothFindFirstRadio` | `0x5D00` | 84 | UnwindData |  |
| 41 | `BluetoothGATTGetCharacteristicValue` | `0x6C10` | 241 | UnwindData |  |
| 42 | `BluetoothGATTGetCharacteristics` | `0x6D10` | 236 | UnwindData |  |
| 45 | `BluetoothGATTGetIncludedServices` | `0x7050` | 212 | UnwindData |  |
| 43 | `BluetoothGATTGetDescriptorValue` | `0x7130` | 242 | UnwindData |  |
| 44 | `BluetoothGATTGetDescriptors` | `0x7230` | 230 | UnwindData |  |
| 46 | `BluetoothGATTGetServices` | `0x76A0` | 42 | UnwindData |  |
| 4 | `BluetoothAddressToString` | `0x9330` | 150 | UnwindData |  |
| 53 | `BluetoothGetRadioInfo` | `0x9680` | 67 | UnwindData |  |
| 68 | `BluetoothSdpEnumAttributes` | `0xB0D0` | 1,596 | UnwindData |  |
| 27 | `BluetoothFindNextDevice` | `0xBCC0` | 305 | UnwindData |  |
| 97 | `BthpTransposeAndExtendBytes` | `0xBF50` | 176 | UnwindData |  |
| 60 | `BluetoothIsSwiftPairEnabledByDefault` | `0xC320` | 614 | UnwindData |  |
| 61 | `BluetoothIsTopOfServiceGroup` | `0xD5C0` | 1,270 | UnwindData |  |
| 24 | `BluetoothFindFirstServiceEx` | `0xE260` | 61 | UnwindData |  |
| 47 | `BluetoothGATTRegisterEvent` | `0xFE80` | 1,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `BthpIsRadioSoftwareEnabled` | `0x103E0` | 210 | UnwindData |  |
| 65 | `BluetoothRegisterForAuthenticationEx` | `0x109D0` | 537 | UnwindData |  |
| 57 | `BluetoothIsConnectableByDefault` | `0x11140` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `BluetoothGATTUnregisterEvent` | `0x11160` | 26,432 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `DllCanUnloadNow` | `0x178A0` | 63 | UnwindData |  |
| 1 | `BthpEnableA2DPIfPresent` | `0x17FB0` | 685 | UnwindData |  |
| 2 | `BthpSetServiceState` | `0x19770` | 77 | UnwindData |  |
| 5 | `BluetoothCheckForUnsupportedGuid` | `0x1BFE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `BluetoothDisconnectDevice` | `0x1BFF0` | 238 | UnwindData |  |
| 7 | `BluetoothEnableConnectableAndDiscoverable` | `0x1C0F0` | 241 | UnwindData |  |
| 9 | `BluetoothEnableIncomingConnections` | `0x1C1F0` | 178 | UnwindData |  |
| 10 | `BluetoothEnumerateInstalledServices` | `0x1C2B0` | 596 | UnwindData |  |
| 11 | `BluetoothEnumerateInstalledServicesEx` | `0x1C510` | 728 | UnwindData |  |
| 12 | `BluetoothEnumerateLocalServices` | `0x1C7F0` | 573 | UnwindData |  |
| 16 | `BluetoothFindFirstBrowseGroup` | `0x1CA40` | 335 | UnwindData |  |
| 19 | `BluetoothFindFirstProfileDescriptor` | `0x1CBA0` | 354 | UnwindData |  |
| 20 | `BluetoothFindFirstProtocolDescriptorStack` | `0x1CD10` | 339 | UnwindData |  |
| 21 | `BluetoothFindFirstProtocolEntry` | `0x1CE70` | 299 | UnwindData |  |
| 23 | `BluetoothFindFirstService` | `0x1CFB0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `BluetoothFindNextBrowseGroup` | `0x1CFD0` | 118 | UnwindData |  |
| 28 | `BluetoothFindNextProfileDescriptor` | `0x1D050` | 273 | UnwindData |  |
| 29 | `BluetoothFindNextProtocolDescriptorStack` | `0x1D170` | 185 | UnwindData |  |
| 30 | `BluetoothFindNextProtocolEntry` | `0x1D230` | 231 | UnwindData |  |
| 34 | `BluetoothFindProtocolDescriptorStackClose` | `0x1D320` | 141 | UnwindData |  |
| 52 | `BluetoothGetLocalServiceInfo` | `0x1D3C0` | 435 | UnwindData |  |
| 54 | `BluetoothGetServicePnpInstance` | `0x1D580` | 787 | UnwindData |  |
| 55 | `BluetoothIsBluetoothServiceRunning` | `0x1D8A0` | 217 | UnwindData |  |
| 58 | `BluetoothIsDiscoverable` | `0x1D980` | 293 | UnwindData |  |
| 59 | `BluetoothIsDiscoverableByDefault` | `0x1DAB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `BluetoothIsVersionAvailable` | `0x1DAC0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `BluetoothMapStatusToError` | `0x1DAE0` | 442 | UnwindData |  |
| 64 | `BluetoothRegisterForAuthentication` | `0x1DCA0` | 541 | UnwindData |  |
| 66 | `BluetoothRegisterForAuthenticationInternal` | `0x1DED0` | 41 | UnwindData |  |
| 67 | `BluetoothRemoveDevice` | `0x1DF00` | 485 | UnwindData |  |
| 72 | `BluetoothSdpGetInnerRecord` | `0x1E0F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `BluetoothSdpGetNextRecord` | `0x1E110` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `BluetoothSendAuthenticationResponse` | `0x1E130` | 153 | UnwindData |  |
| 76 | `BluetoothSendAuthenticationResponseEx` | `0x1E1D0` | 551 | UnwindData |  |
| 77 | `BluetoothSetLocalServiceInfo` | `0x1E400` | 430 | UnwindData |  |
| 78 | `BluetoothSetServiceState` | `0x1E5C0` | 50 | UnwindData |  |
| 79 | `BluetoothSetServiceStateEx` | `0x1E600` | 55 | UnwindData |  |
| 83 | `BluetoothUpdateDeviceRecord` | `0x1E640` | 163 | UnwindData |  |
| 84 | `BthpCleanupBRDeviceNode` | `0x1E6F0` | 171 | UnwindData |  |
| 85 | `BthpCleanupDeviceLocalServices` | `0x1E7B0` | 409 | UnwindData |  |
| 86 | `BthpCleanupDeviceRemoteServices` | `0x1E950` | 316 | UnwindData |  |
| 87 | `BthpCleanupLEDeviceNodes` | `0x1EAA0` | 204 | UnwindData |  |
| 88 | `BthpEnableAllServices` | `0x1EB80` | 827 | UnwindData |  |
| 89 | `BthpEnableRadioSoftware` | `0x1EED0` | 178 | UnwindData |  |
| 96 | `BthpShouldForceAuthentication` | `0x1EF90` | 197 | UnwindData |  |
| 80 | `BluetoothSppEnableIncomingComPort` | `0x1F540` | 155 | UnwindData |  |
| 81 | `BluetoothSppFindNextOpenComPort` | `0x1F5F0` | 146 | UnwindData |  |
| 38 | `BluetoothGATTAbortReliableWrite` | `0x1F6F0` | 116 | UnwindData |  |
| 39 | `BluetoothGATTBeginReliableWrite` | `0x1F770` | 135 | UnwindData |  |
| 40 | `BluetoothGATTEndReliableWrite` | `0x1F800` | 116 | UnwindData |  |
| 48 | `BluetoothGATTSetCharacteristicValue` | `0x1F880` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `BluetoothGATTSetDescriptorValue` | `0x1F890` | 132 | UnwindData |  |
| 91 | `BthpGATTCloseSession` | `0x1F920` | 15,588 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |

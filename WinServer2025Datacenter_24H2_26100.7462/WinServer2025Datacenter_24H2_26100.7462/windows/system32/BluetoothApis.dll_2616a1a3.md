# Binary Specification: BluetoothApis.dll

## Binary Metadata
* **Original Path:** `c:\windows\system32\BluetoothApis.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `2616a1a37bb273f3c99a3738f5a09669f3548beefdaf0a43373fcd8a4baf2e29`
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
| 60 | `BluetoothIsSwiftPairEnabledByDefault` | `0xC440` | 614 | UnwindData |  |
| 61 | `BluetoothIsTopOfServiceGroup` | `0xD670` | 1,270 | UnwindData |  |
| 24 | `BluetoothFindFirstServiceEx` | `0xE290` | 61 | UnwindData |  |
| 47 | `BluetoothGATTRegisterEvent` | `0x10030` | 1,376 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 93 | `BthpIsRadioSoftwareEnabled` | `0x10590` | 210 | UnwindData |  |
| 65 | `BluetoothRegisterForAuthenticationEx` | `0x109E0` | 537 | UnwindData |  |
| 57 | `BluetoothIsConnectableByDefault` | `0x11150` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 50 | `BluetoothGATTUnregisterEvent` | `0x11170` | 26,160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `DllCanUnloadNow` | `0x177A0` | 63 | UnwindData |  |
| 1 | `BthpEnableA2DPIfPresent` | `0x17F30` | 685 | UnwindData |  |
| 2 | `BthpSetServiceState` | `0x196F0` | 77 | UnwindData |  |
| 5 | `BluetoothCheckForUnsupportedGuid` | `0x1BF00` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `BluetoothDisconnectDevice` | `0x1BF10` | 238 | UnwindData |  |
| 7 | `BluetoothEnableConnectableAndDiscoverable` | `0x1C010` | 241 | UnwindData |  |
| 9 | `BluetoothEnableIncomingConnections` | `0x1C110` | 178 | UnwindData |  |
| 10 | `BluetoothEnumerateInstalledServices` | `0x1C1D0` | 596 | UnwindData |  |
| 11 | `BluetoothEnumerateInstalledServicesEx` | `0x1C430` | 728 | UnwindData |  |
| 12 | `BluetoothEnumerateLocalServices` | `0x1C710` | 573 | UnwindData |  |
| 16 | `BluetoothFindFirstBrowseGroup` | `0x1C960` | 335 | UnwindData |  |
| 19 | `BluetoothFindFirstProfileDescriptor` | `0x1CAC0` | 354 | UnwindData |  |
| 20 | `BluetoothFindFirstProtocolDescriptorStack` | `0x1CC30` | 339 | UnwindData |  |
| 21 | `BluetoothFindFirstProtocolEntry` | `0x1CD90` | 299 | UnwindData |  |
| 23 | `BluetoothFindFirstService` | `0x1CED0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `BluetoothFindNextBrowseGroup` | `0x1CEF0` | 118 | UnwindData |  |
| 28 | `BluetoothFindNextProfileDescriptor` | `0x1CF70` | 273 | UnwindData |  |
| 29 | `BluetoothFindNextProtocolDescriptorStack` | `0x1D090` | 185 | UnwindData |  |
| 30 | `BluetoothFindNextProtocolEntry` | `0x1D150` | 231 | UnwindData |  |
| 34 | `BluetoothFindProtocolDescriptorStackClose` | `0x1D240` | 141 | UnwindData |  |
| 52 | `BluetoothGetLocalServiceInfo` | `0x1D2E0` | 435 | UnwindData |  |
| 54 | `BluetoothGetServicePnpInstance` | `0x1D4A0` | 787 | UnwindData |  |
| 55 | `BluetoothIsBluetoothServiceRunning` | `0x1D7C0` | 217 | UnwindData |  |
| 58 | `BluetoothIsDiscoverable` | `0x1D8A0` | 293 | UnwindData |  |
| 59 | `BluetoothIsDiscoverableByDefault` | `0x1D9D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 62 | `BluetoothIsVersionAvailable` | `0x1D9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 63 | `BluetoothMapStatusToError` | `0x1DA00` | 442 | UnwindData |  |
| 64 | `BluetoothRegisterForAuthentication` | `0x1DBC0` | 541 | UnwindData |  |
| 66 | `BluetoothRegisterForAuthenticationInternal` | `0x1DDF0` | 41 | UnwindData |  |
| 67 | `BluetoothRemoveDevice` | `0x1DE20` | 485 | UnwindData |  |
| 72 | `BluetoothSdpGetInnerRecord` | `0x1E010` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 73 | `BluetoothSdpGetNextRecord` | `0x1E030` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `BluetoothSendAuthenticationResponse` | `0x1E050` | 153 | UnwindData |  |
| 76 | `BluetoothSendAuthenticationResponseEx` | `0x1E0F0` | 551 | UnwindData |  |
| 77 | `BluetoothSetLocalServiceInfo` | `0x1E320` | 430 | UnwindData |  |
| 78 | `BluetoothSetServiceState` | `0x1E4E0` | 50 | UnwindData |  |
| 79 | `BluetoothSetServiceStateEx` | `0x1E520` | 55 | UnwindData |  |
| 83 | `BluetoothUpdateDeviceRecord` | `0x1E560` | 163 | UnwindData |  |
| 84 | `BthpCleanupBRDeviceNode` | `0x1E610` | 171 | UnwindData |  |
| 85 | `BthpCleanupDeviceLocalServices` | `0x1E6D0` | 409 | UnwindData |  |
| 86 | `BthpCleanupDeviceRemoteServices` | `0x1E870` | 316 | UnwindData |  |
| 87 | `BthpCleanupLEDeviceNodes` | `0x1E9C0` | 204 | UnwindData |  |
| 88 | `BthpEnableAllServices` | `0x1EAA0` | 827 | UnwindData |  |
| 89 | `BthpEnableRadioSoftware` | `0x1EDF0` | 178 | UnwindData |  |
| 96 | `BthpShouldForceAuthentication` | `0x1EEB0` | 197 | UnwindData |  |
| 80 | `BluetoothSppEnableIncomingComPort` | `0x1F460` | 155 | UnwindData |  |
| 81 | `BluetoothSppFindNextOpenComPort` | `0x1F510` | 146 | UnwindData |  |
| 38 | `BluetoothGATTAbortReliableWrite` | `0x1F610` | 116 | UnwindData |  |
| 39 | `BluetoothGATTBeginReliableWrite` | `0x1F690` | 135 | UnwindData |  |
| 40 | `BluetoothGATTEndReliableWrite` | `0x1F720` | 116 | UnwindData |  |
| 48 | `BluetoothGATTSetCharacteristicValue` | `0x1F7A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `BluetoothGATTSetDescriptorValue` | `0x1F7B0` | 132 | UnwindData |  |
| 91 | `BthpGATTCloseSession` | `0x1F840` | 15,588 | SectionBoundedDelta | *Size estimated via contiguous RVA delta.* |

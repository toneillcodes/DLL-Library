# Binary Specification: MDMAgent.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\drivers\Lenovo\udc\Service\MDMAgent.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `bcabfb20ab45adb471872111ee233a41e1e087e1d033e42fa0cfc9ed9fe42052`
* **Total Exported Functions:** 172

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 20 | `??1MDMAgentHelper@@QEAA@XZ` | `0x3EC0` | 9,200 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 33 | `??4WifiAgent@@QEAAAEAV0@AEBV0@@Z` | `0x62B0` | 1,664 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `??0MDMAgentHelper@@QEAA@XZ` | `0x6930` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??4DeviceManagerAgent@@QEAAAEAV0@$$QEAV0@@Z` | `0x6930` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??4DeviceManagerAgent@@QEAAAEAV0@AEBV0@@Z` | `0x6930` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??4MDMAgentHelper@@QEAAAEAV0@AEBV0@@Z` | `0x6930` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??4NetworkSignalStrengthHandler@UDC@@QEAAAEAV01@$$QEAV01@@Z` | `0x6930` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 29 | `??4NetworkSignalStrengthHandler@UDC@@QEAAAEAV01@AEBV01@@Z` | `0x6930` | 320 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0DeviceManagerAgent@@QEAA@$$QEAV0@@Z` | `0x6A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0DeviceManagerAgent@@QEAA@AEBV0@@Z` | `0x6A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 3 | `??0DeviceManagerAgent@@QEAA@XZ` | `0x6A70` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 48 | `?GetInstance@DeviceManagerAgent@@SAPEAV1@XZ` | `0x6A90` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `?CreateProcessInUserSession@DeviceManagerAgent@@UEAA_NV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0AEAPEAX_N2@Z` | `0x6AA0` | 340 | UnwindData |  |
| 148 | `?rebootDevice@DeviceManagerAgent@@QEAA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x6C00` | 1,872 | UnwindData |  |
| 151 | `?sendLCPNotification@DeviceManagerAgent@@QEAAXHV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x7350` | 1,883 | UnwindData |  |
| 41 | `?ConvertErrorMessageIDasString@DeviceManagerAgent@@QEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAK@Z` | `0x7AB0` | 153 | UnwindData |  |
| 42 | `?ConvertErrorMessageIDasString@GeneralAppSettingsAgent@@AEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAK@Z` | `0x7AB0` | 153 | UnwindData |  |
| 170 | `?subscribeEvents@DeviceManagerAgent@@QEAAXAEAPEAXAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@1W4_EVT_SUBSCRIBE_FLAGS@@@Z` | `0x7B50` | 262 | UnwindData |  |
| 75 | `?SubscriptionCallback@DeviceManagerAgent@@SAKW4_EVT_SUBSCRIBE_NOTIFY_ACTION@@PEAX1@Z` | `0x7C60` | 165 | UnwindData |  |
| 69 | `?ProcessWindowsEvent@DeviceManagerAgent@@QEAAKPEAX@Z` | `0x7D10` | 171 | UnwindData |  |
| 99 | `?cleanUp@DeviceManagerAgent@@QEAAXXZ` | `0x8010` | 37 | UnwindData |  |
| 65 | `?IsDeviceLocked@DeviceManagerAgent@@AEAA_NXZ` | `0x8040` | 532 | UnwindData |  |
| 67 | `?OnDeviceUnlock@DeviceManagerAgent@@QEAAXXZ` | `0x8260` | 253 | UnwindData |  |
| 4 | `??0GeneralAppSettingsAgent@@AEAA@XZ` | `0x90C0` | 71 | UnwindData |  |
| 17 | `??1GeneralAppSettingsAgent@@AEAA@XZ` | `0x9110` | 173 | UnwindData |  |
| 79 | `?__autoclassinit2@GeneralAppSettingsAgent@@QEAAX_K@Z` | `0x91C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 80 | `?__autoclassinit2@GroupPolicyAgent@@QEAAX_K@Z` | `0x91C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `?__autoclassinit2@MDMAgent@@QEAAX_K@Z` | `0x91C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 82 | `?__autoclassinit2@NetworkSettingsAgent@@QEAAX_K@Z` | `0x91C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 83 | `?__autoclassinit2@ProxySettingsAgent@@QEAAX_K@Z` | `0x91C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 84 | `?__autoclassinit2@WifiAgent@@QEAAX_K@Z` | `0x91C0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `?GetInstance@GeneralAppSettingsAgent@@SAPEAV1@XZ` | `0x91D0` | 188 | UnwindData |  |
| 56 | `?Init@GeneralAppSettingsAgent@@QEAA_NAEAVDeviceConfigSettings@@AEAVDeviceConfigPolicy@@AEAPEAX@Z` | `0x9290` | 400 | UnwindData |  |
| 77 | `?Uninit@GeneralAppSettingsAgent@@QEAAXXZ` | `0x9420` | 166 | UnwindData |  |
| 94 | `?checkAndUpdateDeviceConfigSettings@GeneralAppSettingsAgent@@QEAA_NAEBVDeviceConfigSettings@@AEBVDeviceConfigPolicy@@@Z` | `0x94D0` | 295 | UnwindData |  |
| 169 | `?shutdownInitiated@GeneralAppSettingsAgent@@QEAAXXZ` | `0x9600` | 43 | UnwindData |  |
| 131 | `?isDeviceConfigSame@GeneralAppSettingsAgent@@AEBA_NAEBVDeviceConfigSettings@@@Z` | `0x9630` | 5,681 | UnwindData |  |
| 86 | `?applyDeviceConfigSettings@GeneralAppSettingsAgent@@AEAA_NAEBVDeviceConfigSettings@@@Z` | `0xAC70` | 2,463 | UnwindData |  |
| 155 | `?setComputerName@GeneralAppSettingsAgent@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xB610` | 1,572 | UnwindData |  |
| 157 | `?setDebugloglevel@GeneralAppSettingsAgent@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xBC40` | 722 | UnwindData |  |
| 135 | `?isValidDNSHostNamesComputerName@GeneralAppSettingsAgent@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xBF20` | 607 | UnwindData |  |
| 161 | `?setTimeZone@GeneralAppSettingsAgent@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@000@Z` | `0xC180` | 2,956 | UnwindData |  |
| 140 | `?parseTimeZoneDstString@GeneralAppSettingsAgent@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAUTimeZoneDst@1@@Z` | `0xCD10` | 529 | UnwindData |  |
| 104 | `?compareTimeZoneDst@GeneralAppSettingsAgent@@AEAA_NAEBUTimeZoneDst@1@AEBU_TIME_DYNAMIC_ZONE_INFORMATION@@@Z` | `0xCF90` | 128 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 156 | `?setDateTime@GeneralAppSettingsAgent@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0xD010` | 1,583 | UnwindData |  |
| 159 | `?setLanguage@GeneralAppSettingsAgent@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xD640` | 1,057 | UnwindData |  |
| 110 | `?executePowerShellCommand@GeneralAppSettingsAgent@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xDA70` | 1,438 | UnwindData |  |
| 107 | `?executeAdminFlowsCommand@GeneralAppSettingsAgent@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xE010` | 327 | UnwindData |  |
| 108 | `?executeCommand@GeneralAppSettingsAgent@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@00@Z` | `0xE160` | 1,342 | UnwindData |  |
| 152 | `?sendLCPNotification@GeneralAppSettingsAgent@@AEAAXHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0xE6A0` | 2,235 | UnwindData |  |
| 136 | `?isValidTimeZone@GeneralAppSettingsAgent@@AEAA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0xEF60` | 76 | UnwindData |  |
| 72 | `?RunRegMonitor@GeneralAppSettingsAgent@@AEAAXXZ` | `0xF080` | 928 | UnwindData |  |
| 5 | `??0GroupPolicyAgent@@AEAA@XZ` | `0x18690` | 46 | UnwindData |  |
| 50 | `?GetInstance@GroupPolicyAgent@@SAPEAV1@XZ` | `0x18830` | 147 | UnwindData |  |
| 18 | `??1GroupPolicyAgent@@AEAA@XZ` | `0x188D0` | 195 | UnwindData |  |
| 57 | `?Init@GroupPolicyAgent@@QEAAXAEBVDeviceConfigPolicy@@@Z` | `0x189A0` | 339 | UnwindData |  |
| 120 | `?getGroupPoliciesSettings@GroupPolicyAgent@@QEAA_NAEBVDeviceConfigPolicy@@AEAVWindowsGroupPolicy@@@Z` | `0x18B10` | 496 | UnwindData |  |
| 88 | `?applyGroupPolices@GroupPolicyAgent@@AEAA_NAEAVWindowsGroupPolicy@@@Z` | `0x18D00` | 1,767 | UnwindData |  |
| 95 | `?checkAndUpdateGroupPolices@GroupPolicyAgent@@QEAAXAEBVDeviceConfigPolicy@@@Z` | `0x193F0` | 426 | UnwindData |  |
| 158 | `?setGroupPolicy@GroupPolicyAgent@@AEAA_NAEAVGroupPolicy@@PEAUIGroupPolicyObject@@@Z` | `0x195A0` | 2,138 | UnwindData |  |
| 19 | `??1MDMAgent@@UEAA@XZ` | `0x1B5F0` | 244 | UnwindData |  |
| 13 | `??0ProxySettings@@QEAA@XZ` | `0x1B780` | 144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 146 | `?proxy_mode@ProxySettings@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x1B810` | 29 | UnwindData |  |
| 167 | `?set_proxy_mode@ProxySettings@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x1B830` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | `?proxy_manual_connection_name@ProxySettings@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x1B850` | 30 | UnwindData |  |
| 164 | `?set_proxy_manual_connection_name@ProxySettings@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x1B870` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 145 | `?proxy_manual_server_address@ProxySettings@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x1B890` | 30 | UnwindData |  |
| 166 | `?set_proxy_manual_server_address@ProxySettings@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x1B8B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | `?proxy_manual_port@ProxySettings@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x1B8D0` | 30 | UnwindData |  |
| 165 | `?set_proxy_manual_port@ProxySettings@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x1B8F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 142 | `?proxy_bypass_urls@ProxySettings@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x1B910` | 33 | UnwindData |  |
| 163 | `?set_proxy_bypass_urls@ProxySettings@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x1B940` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `?proxy_bypass_local@ProxySettings@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x1B960` | 33 | UnwindData |  |
| 162 | `?set_proxy_bypass_local@ProxySettings@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x1B990` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 147 | `?proxy_setup_script_url@ProxySettings@@QEBA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@XZ` | `0x1B9B0` | 33 | UnwindData |  |
| 168 | `?set_proxy_setup_script_url@ProxySettings@@QEAAXAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x1B9E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 22 | `??1ProxySettings@@QEAA@XZ` | `0x1BA00` | 628 | UnwindData |  |
| 10 | `??0ProxySettings@@QEAA@$$QEAV0@@Z` | `0x1BC80` | 400 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 15 | `??0ProxySettingsAgent@@QEAA@AEBV0@@Z` | `0x1BE10` | 67 | UnwindData |  |
| 32 | `??4ProxySettingsAgent@@QEAAAEAV0@AEBV0@@Z` | `0x1BE60` | 57 | UnwindData |  |
| 9 | `??0NetworkSettingsAgent@@QEAA@AEBV0@@Z` | `0x1BF60` | 114 | UnwindData |  |
| 6 | `??0MDMAgent@@IEAA@XZ` | `0x1BFE0` | 287 | UnwindData |  |
| 51 | `?GetInstance@MDMAgent@@SAPEAV1@XZ` | `0x1C100` | 137 | UnwindData |  |
| 62 | `?InitLog@MDMAgent@@AEAAXXZ` | `0x1C190` | 188 | UnwindData |  |
| 58 | `?Init@MDMAgent@@UEAAXAEAPEAX@Z` | `0x1C250` | 1,003 | UnwindData |  |
| 45 | `?FullInit@MDMAgent@@UEAAXXZ` | `0x1C640` | 473 | UnwindData |  |
| 87 | `?applyGeneralAndGroupPolicySettings@MDMAgent@@EEAAXXZ` | `0x1C820` | 459 | UnwindData |  |
| 70 | `?Reinit@MDMAgent@@QEAAXXZ` | `0x1C9F0` | 394 | UnwindData |  |
| 115 | `?getDeviceConfigPolicy@MDMAgent@@EEAAXAEAVDeviceConfigPolicy@@@Z` | `0x1CB80` | 36 | UnwindData |  |
| 64 | `?Initialize@MDMAgent@@QEAAXXZ` | `0x1CBB0` | 199 | UnwindData |  |
| 76 | `?UnInit@MDMAgent@@UEAAXXZ` | `0x1CC80` | 340 | UnwindData |  |
| 68 | `?OnUDCNotification@MDMAgent@@QEAAXAEAVUDCNotificationData@@@Z` | `0x1CDE0` | 2,825 | UnwindData |  |
| 85 | `?applyDeviceConfig@MDMAgent@@EEAAXAEAVDeviceConfigPolicy@@@Z` | `0x1DDB0` | 911 | UnwindData |  |
| 46 | `?FullInitializeWorker@MDMAgent@@IEAAXXZ` | `0x1E140` | 215 | UnwindData |  |
| 52 | `?GetInstance@NetworkSettingsAgent@@SAPEAV1@XZ` | `0x20520` | 140 | UnwindData |  |
| 8 | `??0NetworkSettingsAgent@@IEAA@XZ` | `0x205B0` | 190 | UnwindData |  |
| 21 | `??1NetworkSettingsAgent@@IEAA@XZ` | `0x206B0` | 262 | UnwindData |  |
| 59 | `?Init@NetworkSettingsAgent@@QEAAHAEAVNetworkSettings@@@Z` | `0x207C0` | 46 | UnwindData |  |
| 153 | `?setAndApplyNetworkSettings@NetworkSettingsAgent@@AEAAHAEBVNetworkSettings@@@Z` | `0x207C0` | 46 | UnwindData |  |
| 89 | `?applyNetworkSettings@NetworkSettingsAgent@@MEAAHAEAVNetworkSettings@@@Z` | `0x207F0` | 1,085 | UnwindData |  |
| 122 | `?getNetworkAdapters@NetworkSettingsAgent@@QEAAHAEAV?$map@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@VAdapterProperties@NetworkCollector@@U?$less@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@V?$allocator@U?$pair@$$CBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@VAdapterProperties@NetworkCollector@@@std@@@2@@std@@@Z` | `0x20CB0` | 724 | UnwindData |  |
| 92 | `?applyTcpIpSettings@NetworkSettingsAgent@@AEAAHAEBV?$map@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@VAdapterProperties@NetworkCollector@@U?$less@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@2@V?$allocator@U?$pair@$$CBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@VAdapterProperties@NetworkCollector@@@std@@@2@@std@@AEBVNetworkSettings@@@Z` | `0x20F90` | 5,772 | UnwindData |  |
| 112 | `?getAutoIPCommand@NetworkSettingsAgent@@AEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV23@@Z` | `0x22620` | 521 | UnwindData |  |
| 128 | `?getStaticIPCommand@NetworkSettingsAgent@@AEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV23@0AEBVNetworkSettings@@@Z` | `0x22830` | 1,585 | UnwindData |  |
| 111 | `?getAutoDNSCommand@NetworkSettingsAgent@@AEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV23@@Z` | `0x22E70` | 521 | UnwindData |  |
| 127 | `?getStaticDNSCommand@NetworkSettingsAgent@@AEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV23@AEAV23@H@Z` | `0x23080` | 911 | UnwindData |  |
| 114 | `?getCommandToClearDNSServers@NetworkSettingsAgent@@AEAA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV23@@Z` | `0x23410` | 585 | UnwindData |  |
| 106 | `?enableOrDisableWifi@NetworkSettingsAgent@@AEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@0@Z` | `0x23660` | 412 | UnwindData |  |
| 119 | `?getDomainOrWorkgroupName@NetworkSettingsAgent@@AEAAHAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x23800` | 62 | UnwindData |  |
| 150 | `?sendJoinDomainOrWorkgroupAlert@NetworkSettingsAgent@@AEAAXV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@H000@Z` | `0x238F0` | 2,470 | UnwindData |  |
| 93 | `?applyWorkgroupOrDomainSettings@NetworkSettingsAgent@@AEAAHAEBVNetworkSettings@@@Z` | `0x242A0` | 4,191 | UnwindData |  |
| 109 | `?executeNetshCommand@NetworkSettingsAgent@@AEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x253C0` | 709 | UnwindData |  |
| 96 | `?checkAndUpdateNetworkSettings@NetworkSettingsAgent@@QEAAHAEBVNetworkSettings@@@Z` | `0x25690` | 28 | UnwindData |  |
| 132 | `?isNetworkSame@NetworkSettingsAgent@@IEAA_NAEBVNetworkSettings@@@Z` | `0x25700` | 5,775 | UnwindData |  |
| 103 | `?compareAdapterInfoToNetworkSettings@NetworkSettingsAgent@@IEAAHAEAVAdapterProperties@NetworkCollector@@AEBVNetworkSettings@@@Z` | `0x26D90` | 1,680 | UnwindData |  |
| 171 | `?validateIPv4AddressFormat@NetworkSettingsAgent@@IEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x27420` | 93 | UnwindData |  |
| 172 | `?validateNetworkAdapter@NetworkSettingsAgent@@IEAAHAEAVAdapterProperties@NetworkCollector@@AEBVNetworkSettings@@@Z` | `0x27480` | 523 | UnwindData |  |
| 55 | `?HandleGetSignalStrengthCommand@NetworkSignalStrengthHandler@UDC@@SA_NXZ` | `0x28460` | 453 | UnwindData |  |
| 47 | `?GetCurrentWifiRSSI@NetworkSignalStrengthHandler@UDC@@CA_NAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x28630` | 130 | UnwindData |  |
| 66 | `?IsWlanConnected@NetworkSignalStrengthHandler@UDC@@CA_NXZ` | `0x286C0` | 62 | UnwindData |  |
| 73 | `?SendSignalStrengthResponse@NetworkSignalStrengthHandler@UDC@@CAX_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x28700` | 1,241 | UnwindData |  |
| 40 | `?ConstructActionParam@NetworkSignalStrengthHandler@UDC@@CA?AV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEBV34@@Z` | `0x28BE0` | 729 | UnwindData |  |
| 12 | `??0ProxySettings@@QEAA@AEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@00000@Z` | `0x28EC0` | 429 | UnwindData |  |
| 11 | `??0ProxySettings@@QEAA@AEBV0@@Z` | `0x29070` | 204 | UnwindData |  |
| 30 | `??4ProxySettings@@QEAAAEAV0@$$QEAV0@@Z` | `0x29140` | 28 | UnwindData |  |
| 31 | `??4ProxySettings@@QEAAAEAV0@AEBV0@@Z` | `0x29160` | 232 | UnwindData |  |
| 34 | `??8ProxySettings@@QEBA_NAEBV0@@Z` | `0x29250` | 1,988 | UnwindData |  |
| 53 | `?GetInstance@ProxySettingsAgent@@SAPEAV1@XZ` | `0x29A20` | 295 | UnwindData |  |
| 14 | `??0ProxySettingsAgent@@IEAA@XZ` | `0x29B50` | 176 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | `?Init@ProxySettingsAgent@@QEAAHAEAVNetworkSettings@@@Z` | `0x29C00` | 111 | UnwindData |  |
| 71 | `?Reinit@ProxySettingsAgent@@QEAAHXZ` | `0x29C70` | 46 | UnwindData |  |
| 124 | `?getProxyMode@ProxySettingsAgent@@IEAA?AW4proxy_mode@1@V?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x29CA0` | 500 | UnwindData |  |
| 154 | `?setAndApplyProxySettings@ProxySettingsAgent@@AEAAHAEAVProxySettings@@@Z` | `0x29EA0` | 46 | UnwindData |  |
| 90 | `?applyProxySettings@ProxySettingsAgent@@AEAAHAEAVProxySettings@@@Z` | `0x29ED0` | 2,630 | UnwindData |  |
| 101 | `?clearMemory@ProxySettingsAgent@@AEAAXAEAUINTERNET_PER_CONN_OPTION_LISTW@@@Z` | `0x2A920` | 23 | UnwindData |  |
| 113 | `?getAutomaticProxyOptions@ProxySettingsAgent@@AEAAXAEAUINTERNET_PER_CONN_OPTION_LISTW@@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAVProxySettings@@@Z` | `0x2A980` | 280 | UnwindData |  |
| 121 | `?getManualProxyOptions@ProxySettingsAgent@@AEAAXAEAUINTERNET_PER_CONN_OPTION_LISTW@@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAVProxySettings@@@Z` | `0x2AAA0` | 1,333 | UnwindData |  |
| 118 | `?getDisableProxyOptions@ProxySettingsAgent@@AEAAXAEAUINTERNET_PER_CONN_OPTION_LISTW@@@Z` | `0x2AFE0` | 53 | UnwindData |  |
| 129 | `?getWcharArr@ProxySettingsAgent@@AEAAPEAGV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x2B020` | 331 | UnwindData |  |
| 133 | `?isProxySame@ProxySettingsAgent@@AEAA_NAEAVProxySettings@@@Z` | `0x2B170` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 125 | `?getProxySettings@ProxySettingsAgent@@AEAAXAEAVNetworkSettings@@AEAVProxySettings@@@Z` | `0x2B180` | 847 | UnwindData |  |
| 97 | `?checkAndUpdateProxySettings@ProxySettingsAgent@@QEAAHAEAVNetworkSettings@@@Z` | `0x2B4D0` | 341 | UnwindData |  |
| 91 | `?applyProxySettingsToBITS@ProxySettingsAgent@@AEAAHAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@W4proxy_mode@1@@Z` | `0x2B630` | 1,251 | UnwindData |  |
| 149 | `?resetProxySettingsBITS@ProxySettingsAgent@@AEAAHXZ` | `0x2BB20` | 495 | UnwindData |  |
| 126 | `?getProxySettingsFromIE@ProxySettingsAgent@@AEAAHAEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAW4proxy_mode@1@@Z` | `0x2BD10` | 797 | UnwindData |  |
| 160 | `?setProxySettingsToIE@ProxySettingsAgent@@AEAAHAEAVProxySettings@@W4proxy_mode@1@AEAV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@@Z` | `0x2C030` | 424 | UnwindData |  |
| 100 | `?cleanUp@ProxySettingsAgent@@QEAAXXZ` | `0x2C1E0` | 87 | UnwindData |  |
| 23 | `??1ProxySettingsAgent@@UEAA@XZ` | `0x2C240` | 62 | UnwindData |  |
| 116 | `?getDeviceConfigPolicy@MDMAgentHelper@@SAXAEAVDeviceConfigPolicy@@@Z` | `0x2C280` | 36 | UnwindData |  |
| 123 | `?getNetworkSettings@MDMAgentHelper@@SAXAEBVDeviceConfigPolicy@@AEAVNetworkSettings@@@Z` | `0x2C2B0` | 263 | UnwindData |  |
| 130 | `?getWiFiSettings@MDMAgentHelper@@SA_NAEBVDeviceConfigPolicy@@AEAVNetworkWifiSettings@@@Z` | `0x2C3C0` | 512 | UnwindData |  |
| 117 | `?getDeviceConfigSettings@MDMAgentHelper@@SA_NAEAVDeviceConfigSettings@@@Z` | `0x2C5C0` | 559 | UnwindData |  |
| 44 | `?DecryptString@MDMAgentHelper@@SA_NAEBV?$basic_string@GU?$char_traits@G@std@@V?$allocator@G@2@@std@@AEAV23@@Z` | `0x2C7F0` | 707 | UnwindData |  |
| 54 | `?GetInstance@WifiAgent@@SAPEAV1@XZ` | `0x2CAC0` | 158 | UnwindData |  |
| 63 | `?InitLog@WifiAgent@@AEAAXXZ` | `0x2CB60` | 190 | UnwindData |  |
| 16 | `??0WifiAgent@@AEAA@XZ` | `0x2CC20` | 42 | UnwindData |  |
| 61 | `?Init@WifiAgent@@QEAA_NAEBVNetworkWifiSettings@@@Z` | `0x2CC50` | 123 | UnwindData |  |
| 98 | `?checkAndUpdateWifiSettings@WifiAgent@@QEAA_NAEBVNetworkWifiSettings@@@Z` | `0x2CCD0` | 202 | UnwindData |  |
| 78 | `?WaitForWifiConnectionComplete@WifiAgent@@QEAA_NK@Z` | `0x2CDA0` | 128 | UnwindData |  |
| 105 | `?createStopEventHandle@WifiAgent@@AEAAXXZ` | `0x2CE20` | 34 | UnwindData |  |
| 74 | `?SetStopEvent@WifiAgent@@QEAAXXZ` | `0x2CE50` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 24 | `??1WifiAgent@@QEAA@XZ` | `0x2CE60` | 67,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | `?closeStopEventHandle@WifiAgent@@AEAAXXZ` | `0x2CE60` | 67,792 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 35 | `??_7DeviceManagerAgent@@6B@` | `0x3D730` | 12,464 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 39 | `??_7ProxySettingsAgent@@6B@` | `0x407E0` | 5,064 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 38 | `??_7NetworkSettingsAgent@@6B@` | `0x41BA8` | 72 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??_7MDMAgent@@6BIMDMAgent@@@` | `0x41BF0` | 208 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 37 | `??_7MDMAgent@@6BIUDCAgent@@@` | `0x41CC0` | 129,696 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `?m_hSubscription@DeviceManagerAgent@@0PEAXEA` | `0x61760` | 8 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `?m_counter@DeviceManagerAgent@@0HA` | `0x61768` | 4 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 139 | `?m_rebootOnDeviceUnlock@DeviceManagerAgent@@0_NA` | `0x6176C` | 1 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `?isShutdownInitiated@GeneralAppSettingsAgent@@0_NA` | `0x6176D` | 0 | Indeterminate |  |

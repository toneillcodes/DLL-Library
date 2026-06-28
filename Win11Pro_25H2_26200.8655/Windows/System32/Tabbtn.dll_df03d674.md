# Binary Specification: Tabbtn.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\Tabbtn.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `df03d674eac95626026cd43b7ac1d5c74dfadaeff3d328a4f2e000920ca3fd3f`
* **Total Exported Functions:** 225

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 127 | `HandleTabletButtonMessages` | `0x1010` | 406 | UnwindData |  |
| 164 | `?OnMessage@CButtonMonitor@@QEAAXI_K_J@Z` | `0x1200` | 218 | UnwindData |  |
| 223 | `?WinEventProc@CButtonMonitor@@SAXPEAUHWINEVENTHOOK__@@KPEAUHWND__@@JJKK@Z` | `0x12E0` | 192 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 61 | `?Add@?$CSimpleArray@PEAVCButtonAction@@V?$CSimpleArrayEqualHelper@PEAVCButtonAction@@@ATL@@@ATL@@QEAAHAEBQEAVCButtonAction@@@Z` | `0x13A0` | 156 | UnwindData |  |
| 62 | `?Add@?$CSimpleArray@PEAVCButtonSetting@@V?$CSimpleArrayEqualHelper@PEAVCButtonSetting@@@ATL@@@ATL@@QEAAHAEBQEAVCButtonSetting@@@Z` | `0x13A0` | 156 | UnwindData |  |
| 63 | `?Add@?$CSimpleArray@PEAVCOrientation@@V?$CSimpleArrayEqualHelper@PEAVCOrientation@@@ATL@@@ATL@@QEAAHAEBQEAVCOrientation@@@Z` | `0x13A0` | 156 | UnwindData |  |
| 174 | `?RegReadDisplayOrientations@CButtonConfig@@QEAAJXZ` | `0x1450` | 939 | UnwindData |  |
| 131 | `?Init@CButtonConfig@@QEAAJH@Z` | `0x1810` | 287 | UnwindData |  |
| 16 | `??0CButtonMonitor@@QEAA@XZ` | `0x1940` | 357 | UnwindData |  |
| 14 | `??0CButtonConfig@@QEAA@XZ` | `0x1AB0` | 261 | UnwindData |  |
| 21 | `??0CFunctionNotification@@QEAA@XZ` | `0x1BC0` | 144 | UnwindData |  |
| 3 | `??0?$CSimpleArray@PEAVCButtonAction@@V?$CSimpleArrayEqualHelper@PEAVCButtonAction@@@ATL@@@ATL@@QEAA@AEBV01@@Z` | `0x1D80` | 138 | UnwindData |  |
| 5 | `??0?$CSimpleArray@PEAVCButtonSetting@@V?$CSimpleArrayEqualHelper@PEAVCButtonSetting@@@ATL@@@ATL@@QEAA@AEBV01@@Z` | `0x1D80` | 138 | UnwindData |  |
| 7 | `??0?$CSimpleArray@PEAVCOrientation@@V?$CSimpleArrayEqualHelper@PEAVCOrientation@@@ATL@@@ATL@@QEAA@AEBV01@@Z` | `0x1D80` | 138 | UnwindData |  |
| 52 | `??A?$CSimpleArray@PEAUACTION@@V?$CSimpleArrayEqualHelper@PEAUACTION@@@ATL@@@ATL@@QEAAAEAPEAUACTION@@H@Z` | `0x1E10` | 35 | UnwindData |  |
| 53 | `??A?$CSimpleArray@PEAUACTION@@V?$CSimpleArrayEqualHelper@PEAUACTION@@@ATL@@@ATL@@QEBAAEBQEAUACTION@@H@Z` | `0x1E10` | 35 | UnwindData |  |
| 54 | `??A?$CSimpleArray@PEAVCButtonAction@@V?$CSimpleArrayEqualHelper@PEAVCButtonAction@@@ATL@@@ATL@@QEAAAEAPEAVCButtonAction@@H@Z` | `0x1E10` | 35 | UnwindData |  |
| 55 | `??A?$CSimpleArray@PEAVCButtonAction@@V?$CSimpleArrayEqualHelper@PEAVCButtonAction@@@ATL@@@ATL@@QEBAAEBQEAVCButtonAction@@H@Z` | `0x1E10` | 35 | UnwindData |  |
| 56 | `??A?$CSimpleArray@PEAVCButtonSetting@@V?$CSimpleArrayEqualHelper@PEAVCButtonSetting@@@ATL@@@ATL@@QEAAAEAPEAVCButtonSetting@@H@Z` | `0x1E10` | 35 | UnwindData |  |
| 57 | `??A?$CSimpleArray@PEAVCButtonSetting@@V?$CSimpleArrayEqualHelper@PEAVCButtonSetting@@@ATL@@@ATL@@QEBAAEBQEAVCButtonSetting@@H@Z` | `0x1E10` | 35 | UnwindData |  |
| 58 | `??A?$CSimpleArray@PEAVCOrientation@@V?$CSimpleArrayEqualHelper@PEAVCOrientation@@@ATL@@@ATL@@QEAAAEAPEAVCOrientation@@H@Z` | `0x1E10` | 35 | UnwindData |  |
| 59 | `??A?$CSimpleArray@PEAVCOrientation@@V?$CSimpleArrayEqualHelper@PEAVCOrientation@@@ATL@@@ATL@@QEBAAEBQEAVCOrientation@@H@Z` | `0x1E10` | 35 | UnwindData |  |
| 67 | `?CreateExtendedActionObject@CButtonMonitor@@SAJPEAPEAUIUnknown@@@Z` | `0x1E70` | 588 | UnwindData |  |
| 144 | `?LoadSettings@CButtonConfig@@QEAAJXZ` | `0x20D0` | 245 | UnwindData |  |
| 20 | `??0CButtonSettings@@QEAA@XZ` | `0x21D0` | 147 | UnwindData |  |
| 60 | `?Add@?$CSimpleArray@PEAUACTION@@V?$CSimpleArrayEqualHelper@PEAUACTION@@@ATL@@@ATL@@QEAAHAEBQEAUACTION@@@Z` | `0x2270` | 154 | UnwindData |  |
| 135 | `?InternalSetAtIndex@?$CSimpleArray@PEAUACTION@@V?$CSimpleArrayEqualHelper@PEAUACTION@@@ATL@@@ATL@@QEAAXHAEBQEAUACTION@@@Z` | `0x23F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | `?InternalSetAtIndex@?$CSimpleArray@PEAVCButtonAction@@V?$CSimpleArrayEqualHelper@PEAVCButtonAction@@@ATL@@@ATL@@QEAAXHAEBQEAVCButtonAction@@@Z` | `0x23F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | `?InternalSetAtIndex@?$CSimpleArray@PEAVCButtonSetting@@V?$CSimpleArrayEqualHelper@PEAVCButtonSetting@@@ATL@@@ATL@@QEAAXHAEBQEAVCButtonSetting@@@Z` | `0x23F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | `?InternalSetAtIndex@?$CSimpleArray@PEAVCOrientation@@V?$CSimpleArrayEqualHelper@PEAVCOrientation@@@ATL@@@ATL@@QEAAXHAEBQEAVCOrientation@@@Z` | `0x23F0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 2 | `??0?$CSimpleArray@PEAUACTION@@V?$CSimpleArrayEqualHelper@PEAUACTION@@@ATL@@@ATL@@QEAA@XZ` | `0x2410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 4 | `??0?$CSimpleArray@PEAVCButtonAction@@V?$CSimpleArrayEqualHelper@PEAVCButtonAction@@@ATL@@@ATL@@QEAA@XZ` | `0x2410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 6 | `??0?$CSimpleArray@PEAVCButtonSetting@@V?$CSimpleArrayEqualHelper@PEAVCButtonSetting@@@ATL@@@ATL@@QEAA@XZ` | `0x2410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `??0?$CSimpleArray@PEAVCOrientation@@V?$CSimpleArrayEqualHelper@PEAVCOrientation@@@ATL@@@ATL@@QEAA@XZ` | `0x2410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 11 | `??0CActions@@QEAA@XZ` | `0x2410` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 120 | `?GetSize@?$CSimpleArray@PEAUACTION@@V?$CSimpleArrayEqualHelper@PEAUACTION@@@ATL@@@ATL@@QEBAHXZ` | `0x2430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 121 | `?GetSize@?$CSimpleArray@PEAVCButtonAction@@V?$CSimpleArrayEqualHelper@PEAVCButtonAction@@@ATL@@@ATL@@QEBAHXZ` | `0x2430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 122 | `?GetSize@?$CSimpleArray@PEAVCButtonSetting@@V?$CSimpleArrayEqualHelper@PEAVCButtonSetting@@@ATL@@@ATL@@QEBAHXZ` | `0x2430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 123 | `?GetSize@?$CSimpleArray@PEAVCOrientation@@V?$CSimpleArrayEqualHelper@PEAVCOrientation@@@ATL@@@ATL@@QEBAHXZ` | `0x2430` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 1 | `??0?$CSimpleArray@PEAUACTION@@V?$CSimpleArrayEqualHelper@PEAUACTION@@@ATL@@@ATL@@QEAA@AEBV01@@Z` | `0x2440` | 123 | UnwindData |  |
| 9 | `??0?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEAA@XZ` | `0x33A0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 10 | `??0CActions@@QEAA@AEBV0@@Z` | `0x33C0` | 24 | UnwindData |  |
| 13 | `??0CButtonConfig@@QEAA@AEBV0@@Z` | `0x33E0` | 107 | UnwindData |  |
| 15 | `??0CButtonMonitor@@QEAA@AEBV0@@Z` | `0x3460` | 302 | UnwindData |  |
| 17 | `??0CButtonSetting@@QEAA@AEBV0@@Z` | `0x35A0` | 122 | UnwindData |  |
| 19 | `??0CButtonSettings@@QEAA@AEBV0@@Z` | `0x3620` | 52 | UnwindData |  |
| 24 | `??1?$CSimpleArray@PEAUACTION@@V?$CSimpleArrayEqualHelper@PEAUACTION@@@ATL@@@ATL@@QEAA@XZ` | `0x3690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 25 | `??1?$CSimpleArray@PEAVCButtonAction@@V?$CSimpleArrayEqualHelper@PEAVCButtonAction@@@ATL@@@ATL@@QEAA@XZ` | `0x3690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 26 | `??1?$CSimpleArray@PEAVCButtonSetting@@V?$CSimpleArrayEqualHelper@PEAVCButtonSetting@@@ATL@@@ATL@@QEAA@XZ` | `0x3690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 27 | `??1?$CSimpleArray@PEAVCOrientation@@V?$CSimpleArrayEqualHelper@PEAVCOrientation@@@ATL@@@ATL@@QEAA@XZ` | `0x3690` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 28 | `??1?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEAA@XZ` | `0x36A0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 32 | `??1CButtonMonitor@@QEAA@XZ` | `0x36B0` | 168 | UnwindData |  |
| 38 | `??4?$CSimpleArray@PEAUACTION@@V?$CSimpleArrayEqualHelper@PEAUACTION@@@ATL@@@ATL@@QEAAAEAV01@AEBV01@@Z` | `0x3760` | 156 | UnwindData |  |
| 39 | `??4?$CSimpleArray@PEAVCButtonAction@@V?$CSimpleArrayEqualHelper@PEAVCButtonAction@@@ATL@@@ATL@@QEAAAEAV01@AEBV01@@Z` | `0x3810` | 156 | UnwindData |  |
| 40 | `??4?$CSimpleArray@PEAVCButtonSetting@@V?$CSimpleArrayEqualHelper@PEAVCButtonSetting@@@ATL@@@ATL@@QEAAAEAV01@AEBV01@@Z` | `0x3810` | 156 | UnwindData |  |
| 41 | `??4?$CSimpleArray@PEAVCOrientation@@V?$CSimpleArrayEqualHelper@PEAVCOrientation@@@ATL@@@ATL@@QEAAAEAV01@AEBV01@@Z` | `0x3810` | 156 | UnwindData |  |
| 42 | `??4?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEAAAEAV01@AEBV01@@Z` | `0x38C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 49 | `??4CFunctionNotification@@QEAAAEAV0@AEBV0@@Z` | `0x38C0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 43 | `??4CActions@@QEAAAEAV0@AEBV0@@Z` | `0x38E0` | 24 | UnwindData |  |
| 44 | `??4CButtonAction@@QEAAAEAV0@AEBV0@@Z` | `0x3900` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 45 | `??4CButtonConfig@@QEAAAEAV0@AEBV0@@Z` | `0x3920` | 153 | UnwindData |  |
| 46 | `??4CButtonMonitor@@QEAAAEAV0@AEBV0@@Z` | `0x39C0` | 302 | UnwindData |  |
| 47 | `??4CButtonSetting@@QEAAAEAV0@AEBV0@@Z` | `0x3B00` | 122 | UnwindData |  |
| 48 | `??4CButtonSettings@@QEAAAEAV0@AEBV0@@Z` | `0x3B80` | 52 | UnwindData |  |
| 50 | `??4CHidButton@@QEAAAEAV0@AEBV0@@Z` | `0x3BC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 51 | `??4COrientation@@QEAAAEAV0@AEBV0@@Z` | `0x3BF0` | 160 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | `?Add@?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEAAHAEBKAEBQEAVCButtonImages@@@Z` | `0x3C90` | 146 | UnwindData |  |
| 70 | `?DoBuiltInAction@CButtonMonitor@@AEAAJPEAVCButtonAction@@HH@Z` | `0x3D50` | 472 | UnwindData |  |
| 71 | `?DoButtonAction@CButtonMonitor@@AEAAJPEAVCButtonAction@@KHH@Z` | `0x3F30` | 641 | UnwindData |  |
| 72 | `?ExecuteObject@CButtonMonitor@@AEAAJPEBG0@Z` | `0x41C0` | 118 | UnwindData |  |
| 73 | `?Find@?$CSimpleArray@PEAUACTION@@V?$CSimpleArrayEqualHelper@PEAUACTION@@@ATL@@@ATL@@QEBAHAEBQEAUACTION@@@Z` | `0x4240` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 74 | `?Find@?$CSimpleArray@PEAVCButtonAction@@V?$CSimpleArrayEqualHelper@PEAVCButtonAction@@@ATL@@@ATL@@QEBAHAEBQEAVCButtonAction@@@Z` | `0x4240` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 75 | `?Find@?$CSimpleArray@PEAVCButtonSetting@@V?$CSimpleArrayEqualHelper@PEAVCButtonSetting@@@ATL@@@ATL@@QEBAHAEBQEAVCButtonSetting@@@Z` | `0x4240` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | `?Find@?$CSimpleArray@PEAVCOrientation@@V?$CSimpleArrayEqualHelper@PEAVCOrientation@@@ATL@@@ATL@@QEBAHAEBQEAVCOrientation@@@Z` | `0x4240` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 79 | `?FindKey@?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEBAHAEBK@Z` | `0x4280` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 81 | `?FindVal@?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEBAHAEBQEAVCButtonImages@@@Z` | `0x42C0` | 64 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 87 | `?GetButtonConfig@CButtonMonitor@@QEAAPEAVCButtonConfig@@XZ` | `0x4300` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 96 | `?GetData@?$CSimpleArray@PEAUACTION@@V?$CSimpleArrayEqualHelper@PEAUACTION@@@ATL@@@ATL@@QEBAPEAPEAUACTION@@XZ` | `0x4310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 97 | `?GetData@?$CSimpleArray@PEAVCButtonAction@@V?$CSimpleArrayEqualHelper@PEAVCButtonAction@@@ATL@@@ATL@@QEBAPEAPEAVCButtonAction@@XZ` | `0x4310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 98 | `?GetData@?$CSimpleArray@PEAVCButtonSetting@@V?$CSimpleArrayEqualHelper@PEAVCButtonSetting@@@ATL@@@ATL@@QEBAPEAPEAVCButtonSetting@@XZ` | `0x4310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 99 | `?GetData@?$CSimpleArray@PEAVCOrientation@@V?$CSimpleArrayEqualHelper@PEAVCOrientation@@@ATL@@@ATL@@QEBAPEAPEAVCOrientation@@XZ` | `0x4310` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | `?GetKeyAt@?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEBAAEAKH@Z` | `0x4320` | 35 | UnwindData |  |
| 124 | `?GetSize@?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEBAHXZ` | `0x4350` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 126 | `?GetValueAt@?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEBAAEAPEAVCButtonImages@@H@Z` | `0x4360` | 36 | UnwindData |  |
| 129 | `?InSession0@CButtonMonitor@@AEAAHXZ` | `0x4390` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 132 | `?Init@CButtonMonitor@@QEAAJPEAUHWND__@@@Z` | `0x43A0` | 198 | UnwindData |  |
| 139 | `?InternalSetAtIndex@?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEAAXHAEBKAEBQEAVCButtonImages@@@Z` | `0x4470` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 141 | `?IsActionUnsupported@CButtonMonitor@@SAHK@Z` | `0x44A0` | 184 | UnwindData |  |
| 145 | `?Lookup@?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEBAPEAVCButtonImages@@AEBK@Z` | `0x4560` | 43 | UnwindData |  |
| 147 | `?NotifyFnMode@CButtonMonitor@@AEAAJH@Z` | `0x45A0` | 172 | UnwindData |  |
| 148 | `?OnActionAppCommand@CButtonMonitor@@AEAAJPEAVCButtonAction@@HH@Z` | `0x4660` | 254 | UnwindData |  |
| 149 | `?OnActionContextMenu@CButtonMonitor@@AEAAJPEAVCButtonAction@@HH@Z` | `0x4770` | 197 | UnwindData |  |
| 150 | `?OnActionDisplayOff@CButtonMonitor@@AEAAJPEAVCButtonAction@@HH@Z` | `0x4840` | 184 | UnwindData |  |
| 151 | `?OnActionLaunchApp@CButtonMonitor@@AEAAJPEAVCButtonAction@@HH@Z` | `0x4900` | 594 | UnwindData |  |
| 152 | `?OnActionMouseWheel@CButtonMonitor@@AEAAJPEAVCButtonAction@@HH@Z` | `0x4B60` | 297 | UnwindData |  |
| 153 | `?OnActionSendKey@CButtonMonitor@@AEAAJPEAVCButtonAction@@HH@Z` | `0x4C90` | 517 | UnwindData |  |
| 154 | `?OnActionSetOrientation@CButtonMonitor@@AEAAJPEAVCButtonAction@@HH@Z` | `0x4EA0` | 287 | UnwindData |  |
| 155 | `?OnActionUnknown@CButtonMonitor@@AEAAJPEAVCButtonAction@@HH@Z` | `0x4FD0` | 395 | UnwindData |  |
| 156 | `?OnActionWindowsFlip3d@CButtonMonitor@@AEAAJPEAVCButtonAction@@HH@Z` | `0x5170` | 227 | UnwindData |  |
| 157 | `?OnActionWindowsFlip@CButtonMonitor@@AEAAJPEAVCButtonAction@@HH@Z` | `0x5260` | 185 | UnwindData |  |
| 158 | `?OnButtonDown@CButtonMonitor@@AEAAX_K_J@Z` | `0x5320` | 272 | UnwindData |  |
| 159 | `?OnButtonUp@CButtonMonitor@@AEAAX_K_J@Z` | `0x5440` | 177 | UnwindData |  |
| 160 | `?OnDisplayChange@CButtonMonitor@@AEAAX_K_J@Z` | `0x5500` | 55 | UnwindData |  |
| 161 | `?OnFnKeyTimer@CButtonMonitor@@AEAAXXZ` | `0x5540` | 96 | UnwindData |  |
| 162 | `?OnHoldTimer@CButtonMonitor@@AEAAXXZ` | `0x55B0` | 321 | UnwindData |  |
| 163 | `?OnInput@CButtonMonitor@@AEAAX_K_J@Z` | `0x5700` | 222 | UnwindData |  |
| 165 | `?OnRepeatTimer@CButtonMonitor@@AEAAXXZ` | `0x57F0` | 178 | UnwindData |  |
| 166 | `?OnSettingChange@CButtonMonitor@@AEAAX_K_J@Z` | `0x58B0` | 181 | UnwindData |  |
| 167 | `?OnTimer@CButtonMonitor@@AEAAX_K_J@Z` | `0x5970` | 112 | UnwindData |  |
| 168 | `?ProcessAction@CButtonMonitor@@AEAAJKH@Z` | `0x5A50` | 955 | UnwindData |  |
| 169 | `?ProcessEvent@CButtonMonitor@@AEAAJKH@Z` | `0x5E20` | 557 | UnwindData |  |
| 176 | `?RegisterButtonDevices@CButtonMonitor@@QEAAJXZ` | `0x6100` | 376 | UnwindData |  |
| 177 | `?RegisterForPopups@CButtonMonitor@@AEAAJXZ` | `0x6280` | 251 | UnwindData |  |
| 179 | `?ReleaseDownButtons@CButtonMonitor@@AEAAJXZ` | `0x6390` | 174 | UnwindData |  |
| 180 | `?ReleaseRepeatOrHoldButton@CButtonMonitor@@AEAAJXZ` | `0x6450` | 236 | UnwindData |  |
| 181 | `?Remove@?$CSimpleArray@PEAUACTION@@V?$CSimpleArrayEqualHelper@PEAUACTION@@@ATL@@@ATL@@QEAAHAEBQEAUACTION@@@Z` | `0x6550` | 43 | UnwindData |  |
| 182 | `?Remove@?$CSimpleArray@PEAVCButtonAction@@V?$CSimpleArrayEqualHelper@PEAVCButtonAction@@@ATL@@@ATL@@QEAAHAEBQEAVCButtonAction@@@Z` | `0x6550` | 43 | UnwindData |  |
| 183 | `?Remove@?$CSimpleArray@PEAVCButtonSetting@@V?$CSimpleArrayEqualHelper@PEAVCButtonSetting@@@ATL@@@ATL@@QEAAHAEBQEAVCButtonSetting@@@Z` | `0x6550` | 43 | UnwindData |  |
| 184 | `?Remove@?$CSimpleArray@PEAVCOrientation@@V?$CSimpleArrayEqualHelper@PEAVCOrientation@@@ATL@@@ATL@@QEAAHAEBQEAVCOrientation@@@Z` | `0x6550` | 43 | UnwindData |  |
| 185 | `?Remove@?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEAAHAEBK@Z` | `0x6590` | 43 | UnwindData |  |
| 186 | `?RemoveAll@?$CSimpleArray@PEAUACTION@@V?$CSimpleArrayEqualHelper@PEAUACTION@@@ATL@@@ATL@@QEAAXXZ` | `0x65D0` | 48 | UnwindData |  |
| 187 | `?RemoveAll@?$CSimpleArray@PEAVCButtonAction@@V?$CSimpleArrayEqualHelper@PEAVCButtonAction@@@ATL@@@ATL@@QEAAXXZ` | `0x65D0` | 48 | UnwindData |  |
| 188 | `?RemoveAll@?$CSimpleArray@PEAVCButtonSetting@@V?$CSimpleArrayEqualHelper@PEAVCButtonSetting@@@ATL@@@ATL@@QEAAXXZ` | `0x65D0` | 48 | UnwindData |  |
| 189 | `?RemoveAll@?$CSimpleArray@PEAVCOrientation@@V?$CSimpleArrayEqualHelper@PEAVCOrientation@@@ATL@@@ATL@@QEAAXXZ` | `0x65D0` | 48 | UnwindData |  |
| 190 | `?RemoveAll@?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEAAXXZ` | `0x6610` | 70 | UnwindData |  |
| 191 | `?RemoveAt@?$CSimpleArray@PEAUACTION@@V?$CSimpleArrayEqualHelper@PEAUACTION@@@ATL@@@ATL@@QEAAHH@Z` | `0x6660` | 89 | UnwindData |  |
| 192 | `?RemoveAt@?$CSimpleArray@PEAVCButtonAction@@V?$CSimpleArrayEqualHelper@PEAVCButtonAction@@@ATL@@@ATL@@QEAAHH@Z` | `0x6660` | 89 | UnwindData |  |
| 193 | `?RemoveAt@?$CSimpleArray@PEAVCButtonSetting@@V?$CSimpleArrayEqualHelper@PEAVCButtonSetting@@@ATL@@@ATL@@QEAAHH@Z` | `0x6660` | 89 | UnwindData |  |
| 194 | `?RemoveAt@?$CSimpleArray@PEAVCOrientation@@V?$CSimpleArrayEqualHelper@PEAVCOrientation@@@ATL@@@ATL@@QEAAHH@Z` | `0x6660` | 89 | UnwindData |  |
| 195 | `?RemoveAt@?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEAAHH@Z` | `0x66C0` | 270 | UnwindData |  |
| 197 | `?ReverseLookup@?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEBAKAEBQEAVCButtonImages@@@Z` | `0x67E0` | 42 | UnwindData |  |
| 199 | `?SendAppCommand@CButtonMonitor@@AEAAJG@Z` | `0x6810` | 491 | UnwindData |  |
| 200 | `?SendModKeys@CButtonMonitor@@CAXEH@Z` | `0x6A10` | 115 | UnwindData |  |
| 201 | `?SendVKey@CButtonMonitor@@CAXEEH@Z` | `0x6A90` | 252 | UnwindData |  |
| 203 | `?SetAt@?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEAAHAEBKAEBQEAVCButtonImages@@@Z` | `0x6BA0` | 76 | UnwindData |  |
| 204 | `?SetAtIndex@?$CSimpleArray@PEAUACTION@@V?$CSimpleArrayEqualHelper@PEAUACTION@@@ATL@@@ATL@@QEAAHHAEBQEAUACTION@@@Z` | `0x6C00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 205 | `?SetAtIndex@?$CSimpleArray@PEAVCButtonAction@@V?$CSimpleArrayEqualHelper@PEAVCButtonAction@@@ATL@@@ATL@@QEAAHHAEBQEAVCButtonAction@@@Z` | `0x6C00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 206 | `?SetAtIndex@?$CSimpleArray@PEAVCButtonSetting@@V?$CSimpleArrayEqualHelper@PEAVCButtonSetting@@@ATL@@@ATL@@QEAAHHAEBQEAVCButtonSetting@@@Z` | `0x6C00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 207 | `?SetAtIndex@?$CSimpleArray@PEAVCOrientation@@V?$CSimpleArrayEqualHelper@PEAVCOrientation@@@ATL@@@ATL@@QEAAHHAEBQEAVCOrientation@@@Z` | `0x6C00` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 208 | `?SetAtIndex@?$CSimpleMap@KPEAVCButtonImages@@V?$CSimpleMapEqualHelper@KPEAVCButtonImages@@@ATL@@@ATL@@QEAAHHAEBKAEBQEAVCButtonImages@@@Z` | `0x6C30` | 33 | UnwindData |  |
| 211 | `?SetDisplayOrientation@CButtonMonitor@@AEAAJH@Z` | `0x6C60` | 939 | UnwindData |  |
| 212 | `?SetDisplayPower@CButtonMonitor@@AEAAXH@Z` | `0x7020` | 96 | UnwindData |  |
| 215 | `?ShouldSendEscapeForBack@CButtonMonitor@@AEAAHXZ` | `0x7090` | 65 | UnwindData |  |
| 217 | `?ShowWindowSwitchWindow@CButtonMonitor@@CAJXZ` | `0x70E0` | 321 | UnwindData |  |
| 219 | `?UnregisterButtonDevices@CButtonMonitor@@QEAAJXZ` | `0x7300` | 159 | UnwindData |  |
| 22 | `??0CHidButton@@QEAA@PEAUHWND__@@II@Z` | `0x7710` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 36 | `??1CHidButton@@QEAA@XZ` | `0x7740` | 37 | UnwindData |  |
| 69 | `?DispatchHidBtnEvents@CHidButton@@QEAAJPEAUHRAWINPUT__@@@Z` | `0x7770` | 963 | UnwindData |  |
| 78 | `?FindDeviceByHandle@CHidButton@@QEAAPEAU_hidbtndev@@PEAX@Z` | `0x7B40` | 95 | UnwindData |  |
| 80 | `?FindUsage@CHidButton@@AEAAHPEAU_USAGE_AND_PAGE@@KGG@Z` | `0x7BB0` | 116 | UnwindData |  |
| 109 | `?GetHidBtnUsages@CHidButton@@AEAAHPEAU_hidbtndev@@PEAUtagRAWINPUT@@GGPEAU_USAGE_AND_PAGE@@PEAK@Z` | `0x7C30` | 343 | UnwindData |  |
| 178 | `?RegisterHidBtnDevice@CHidButton@@QEAAPEAU_hidbtndev@@PEAXPEAK@Z` | `0x7D90` | 838 | UnwindData |  |
| 220 | `?UnregisterHidBtnDevice@CHidButton@@QEAAHPEAU_hidbtndev@@PEAK@Z` | `0x80E0` | 212 | UnwindData |  |
| 12 | `??0CButtonAction@@QEAA@W4BUTTONACTION_TYPE@@@Z` | `0x81C0` | 76 | UnwindData |  |
| 18 | `??0CButtonSetting@@QEAA@XZ` | `0x8220` | 110 | UnwindData |  |
| 23 | `??0COrientation@@QEAA@XZ` | `0x82A0` | 62 | UnwindData |  |
| 29 | `??1CActions@@QEAA@XZ` | `0x82F0` | 101 | UnwindData |  |
| 30 | `??1CButtonAction@@QEAA@XZ` | `0x8360` | 54 | UnwindData |  |
| 31 | `??1CButtonConfig@@QEAA@XZ` | `0x83A0` | 225 | UnwindData |  |
| 33 | `??1CButtonSetting@@QEAA@XZ` | `0x84D0` | 356 | UnwindData |  |
| 34 | `??1CButtonSettings@@QEAA@XZ` | `0x8640` | 151 | UnwindData |  |
| 37 | `??1COrientation@@QEAA@XZ` | `0x86E0` | 40 | UnwindData |  |
| 65 | `?CanRepeat@CButtonAction@@QEBAHXZ` | `0x8760` | 59 | UnwindData |  |
| 66 | `?Clone@CButtonAction@@QEBAJPEAPEAV1@@Z` | `0x87B0` | 175 | UnwindData |  |
| 77 | `?FindActionById@CActions@@QEAAPEAUACTION@@K@Z` | `0x8930` | 178 | UnwindData |  |
| 82 | `?FreeData@CButtonAction@@QEAAXXZ` | `0x89F0` | 69 | UnwindData |  |
| 83 | `?GetActionAt@CActions@@QEAAPEAUACTION@@H@Z` | `0x8AB0` | 104 | UnwindData |  |
| 84 | `?GetActionFromOrientation@CButtonSetting@@QEAAJKPEAPEAVCButtonAction@@00@Z` | `0x8B20` | 395 | UnwindData |  |
| 85 | `?GetAllowedActions@CButtonSetting@@QEAAPEBGXZ` | `0x8CC0` | 53 | UnwindData |  |
| 86 | `?GetButtonActionType@CButtonAction@@QEBA?BW4BUTTONACTION_TYPE@@XZ` | `0x8D00` | 51 | UnwindData |  |
| 88 | `?GetButtonCount@CButtonSettings@@QEBAHXZ` | `0x8D40` | 51 | UnwindData |  |
| 89 | `?GetButtonFromId@CButtonSettings@@QEAAJKPEAPEAVCButtonSetting@@@Z` | `0x8D80` | 167 | UnwindData |  |
| 90 | `?GetButtonIdFromIndex@CButtonSettings@@QEAAKK@Z` | `0x8E30` | 39 | UnwindData |  |
| 91 | `?GetButtonIds@CButtonSettings@@QEBAJPEAKH@Z` | `0x8E60` | 159 | UnwindData |  |
| 92 | `?GetButtonName@CButtonSetting@@QEAAPEBGXZ` | `0x8F10` | 193 | UnwindData |  |
| 93 | `?GetButtonName@CButtonSettings@@QEBAPEBGH@Z` | `0x8FE0` | 83 | UnwindData |  |
| 94 | `?GetCount@CActions@@QEAAHXZ` | `0x9040` | 51 | UnwindData |  |
| 95 | `?GetCurrentDisplayOrientation@CButtonConfig@@QEAAKXZ` | `0x9080` | 76 | UnwindData |  |
| 100 | `?GetData@CButtonAction@@QEBAQEAEXZ` | `0x90E0` | 53 | UnwindData |  |
| 101 | `?GetDataDWORD@CButtonAction@@QEBA?BKXZ` | `0x9120` | 87 | UnwindData |  |
| 102 | `?GetDefSeq@COrientation@@QEAAKXZ` | `0x9180` | 51 | UnwindData |  |
| 103 | `?GetDescription@COrientation@@QEAAPEBGXZ` | `0x91C0` | 63 | UnwindData |  |
| 104 | `?GetDetailImage@CButtonSettings@@QEAAPEAUHBITMAP__@@KK@Z` | `0x9210` | 250 | UnwindData |  |
| 105 | `?GetDisallowedActions@CButtonSetting@@QEAAPEBGXZ` | `0x9310` | 53 | UnwindData |  |
| 106 | `?GetDisplayOrientationName@CButtonConfig@@QEAAPEBGK@Z` | `0x9350` | 151 | UnwindData |  |
| 107 | `?GetFlags@CButtonSetting@@QEAAKXZ` | `0x93F0` | 50 | UnwindData |  |
| 108 | `?GetFnKeyButtonId@CButtonSettings@@QEAAKXZ` | `0x9430` | 50 | UnwindData |  |
| 110 | `?GetId@CButtonAction@@QEBAKXZ` | `0x9470` | 51 | UnwindData |  |
| 111 | `?GetId@CButtonSetting@@QEAAKXZ` | `0x94B0` | 51 | UnwindData |  |
| 113 | `?GetKeyName@COrientation@@QEAAPEBGXZ` | `0x94F0` | 50 | UnwindData |  |
| 114 | `?GetLocationImage@CButtonSettings@@QEAAPEAUHBITMAP__@@KK@Z` | `0x9530` | 247 | UnwindData |  |
| 115 | `?GetMode@COrientation@@QEAAKXZ` | `0x9630` | 50 | UnwindData |  |
| 116 | `?GetOrientSeq@CButtonConfig@@QEBAKI@Z` | `0x9670` | 74 | UnwindData |  |
| 117 | `?GetOrientSeqCount@CButtonConfig@@QEBAKXZ` | `0x96C0` | 51 | UnwindData |  |
| 118 | `?GetOrientationMode@CButtonAction@@QEBAKXZ` | `0x9700` | 50 | UnwindData |  |
| 119 | `?GetRegType@CButtonAction@@QEBAKXZ` | `0x9740` | 51 | UnwindData |  |
| 125 | `?GetSize@CButtonAction@@QEBAKXZ` | `0x9780` | 51 | UnwindData |  |
| 130 | `?Init@CActions@@QEAAJXZ` | `0x97C0` | 912 | UnwindData |  |
| 133 | `?Init@COrientation@@QEAAJPEAUHKEY__@@@Z` | `0x9B60` | 338 | UnwindData |  |
| 140 | `?IsActionRepeatable@CButtonAction@@SAHK@Z` | `0x9CC0` | 293 | UnwindData |  |
| 142 | `?IsSameAction@CButtonAction@@QEBAHPEBV1@@Z` | `0x9DF0` | 136 | UnwindData |  |
| 143 | `?LoadImageDLL@CButtonSettings@@AEAAHXZ` | `0x9E80` | 183 | UnwindData |  |
| 146 | `?MakeAllUserActionsEqual@CButtonSetting@@QEAAJK@Z` | `0x9F40` | 206 | UnwindData |  |
| 170 | `?RegReadActions@CButtonConfig@@QEAAXPEAUHKEY__@@PEAVCButtonSetting@@H@Z` | `0xA2A0` | 1,624 | UnwindData |  |
| 171 | `?RegReadAndAllocate@CButtonConfig@@SAJPEAUHKEY__@@PEBGPEAKPEAPEAE2@Z` | `0xA900` | 512 | UnwindData |  |
| 172 | `?RegReadButtonSetting@CButtonConfig@@QEAAJPEAUHKEY__@@HH@Z` | `0xAB10` | 992 | UnwindData |  |
| 173 | `?RegReadButtonsSettings@CButtonConfig@@QEAAJXZ` | `0xAF00` | 597 | UnwindData |  |
| 175 | `?RegReadOrientationSeq@CButtonConfig@@QEAAJXZ` | `0xB160` | 481 | UnwindData |  |
| 196 | `?ResetDeprecatedAction@CButtonConfig@@AEAAXPEAVCButtonAction@@@Z` | `0xB350` | 247 | UnwindData |  |
| 198 | `?SaveSettings@CButtonConfig@@QEAAJXZ` | `0xB450` | 1,035 | UnwindData |  |
| 202 | `?Set@CButtonAction@@QEAAJPEBV1@@Z` | `0xB870` | 189 | UnwindData |  |
| 209 | `?SetData@CButtonAction@@QEAAJQEAEK@Z` | `0xB9B0` | 144 | UnwindData |  |
| 210 | `?SetDataDWORD@CButtonAction@@QEAAJK@Z` | `0xBA50` | 117 | UnwindData |  |
| 213 | `?SetId@CButtonAction@@QEAAXK@Z` | `0xBAD0` | 60 | UnwindData |  |
| 214 | `?ShouldButtonShowUI@CButtonSettings@@QEBAHH@Z` | `0xBB20` | 85 | UnwindData |  |
| 221 | `?UpdateButtonRates@CButtonConfig@@QEAAJXZ` | `0xBC00` | 283 | UnwindData |  |
| 222 | `?UpdateCurrentDisplayOrientation@CButtonConfig@@QEAAXXZ` | `0xBD30` | 359 | UnwindData |  |
| 134 | `InitializeTabletButtons` | `0xC490` | 95 | UnwindData |  |
| 218 | `UninitializeTabletButtons` | `0xC500` | 79 | UnwindData |  |
| 35 | `??1CFunctionNotification@@QEAA@XZ` | `0xC780` | 123 | UnwindData |  |
| 68 | `?CreateTrayWindow@CFunctionNotification@@AEAAJXZ` | `0xC810` | 222 | UnwindData |  |
| 128 | `?Hide@CFunctionNotification@@QEAAJXZ` | `0xC900` | 253 | UnwindData |  |
| 216 | `?Show@CFunctionNotification@@QEAAJXZ` | `0xCA10` | 506 | UnwindData |  |
| 224 | `?WindowProc@CFunctionNotification@@SA_JPEAUHWND__@@I_K_J@Z` | `0xCC10` | 111 | UnwindData |  |
| 225 | `?sm_dwPopupCount@CButtonMonitor@@2KA` | `0x27958` | 0 | Indeterminate |  |

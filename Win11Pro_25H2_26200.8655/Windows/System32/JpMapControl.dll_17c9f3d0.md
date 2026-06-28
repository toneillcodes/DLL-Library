# Binary Specification: JpMapControl.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\JpMapControl.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `17c9f3d04ea0704630ef8d60dd4f221a54d4db8d1ff90e380b65468337e8b719`
* **Total Exported Functions:** 17

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | `DllCanUnloadNow` | `0x3E80` | 32 | UnwindData |  |
| 2 | `DllGetActivationFactory` | `0x3EB0` | 45 | UnwindData |  |
| 3 | `DllGetClassObject` | `0x3EF0` | 65 | UnwindData |  |
| 4 | `JpIs3DSupported` | `0x28DF0` | 173 | UnwindData |  |
| 5 | `JpIsUnifiedMapsStack` | `0x28EB0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 7 | `JpMapControl_Create` | `0x28EC0` | 210 | UnwindData |  |
| 9 | `JpMapModel3DFrom3MFStreamOperation_Create` | `0x28FA0` | 246 | UnwindData |  |
| 12 | `JpOverviewMapControl_Create` | `0x290A0` | 194 | UnwindData |  |
| 13 | `JpRestrictedApiAccessCheck` | `0x29170` | 62 | UnwindData |  |
| 14 | `JpStreetsideExperience_Create` | `0x291C0` | 213 | UnwindData |  |
| 15 | `JpStreetsidePanoramaOperation_Create` | `0x292A0` | 258 | UnwindData |  |
| 6 | `JpMapControlSettings_Create` | `0x29AA0` | 164 | UnwindData |  |
| 16 | `MapSettings_GetMosBingMapsKey` | `0x29B50` | 230 | UnwindData |  |
| 17 | `MapSettings_ResetMosKeys` | `0x29C40` | 1,088 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 8 | `JpMapFactory_Create` | `0x2A080` | 171 | UnwindData |  |
| 10 | `JpMapOverlayModel_Create` | `0x2D710` | 192 | UnwindData |  |
| 11 | `JpMapStyleSheetFactory_Create` | `0x2DDC0` | 174 | UnwindData |  |

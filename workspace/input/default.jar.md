# MapleIR SSA IR Dump for AI Analysis
# Generated from: Evaluator-1.0-SNAPSHOT.jar
# Total classes: 29
# Total methods with IR: 134

## Class: dev/sim0n/evaluator/operation/DoubleMathOperation$3
Super: dev/sim0n/evaluator/operation/DoubleMathOperation
Interfaces: []
Access: final synchronized enum

### Method: <init>(Ljava/lang/String;ILjava/lang/String;)V
Access: 

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0, lvar2_0, lvar3_0, nullconst));
   return;
   

```

### Method: evaluate(DD)D
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar3_0 = lvar3_0);
   
BLOCK B:
   return {lvar1_0 / lvar3_0};
   

```


## Class: dev/sim0n/evaluator/operation/DoubleMathOperation$2
Super: dev/sim0n/evaluator/operation/DoubleMathOperation
Interfaces: []
Access: final synchronized enum

### Method: <init>(Ljava/lang/String;ILjava/lang/String;)V
Access: 

```ssa
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0, lvar2_0, lvar3_0, nullconst));
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   

```

### Method: evaluate(DD)D
Access: public

```ssa
BLOCK B:
   return {lvar1_0 - lvar3_0};
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar3_0 = lvar3_0);
   

```


## Class: dev/sim0n/evaluator/operation/DoubleMathOperation$5
Super: dev/sim0n/evaluator/operation/DoubleMathOperation
Interfaces: []
Access: final synchronized enum

### Method: <init>(Ljava/lang/String;ILjava/lang/String;)V
Access: 

```ssa
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0, lvar2_0, lvar3_0, nullconst));
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   

```

### Method: evaluate(DD)D
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar3_0 = lvar3_0);
   
BLOCK B:
   return {lvar1_0 * lvar3_0};
   

```


## Class: dev/sim0n/evaluator/operation/DoubleMathOperation$4
Super: dev/sim0n/evaluator/operation/DoubleMathOperation
Interfaces: []
Access: final synchronized enum

### Method: <init>(Ljava/lang/String;ILjava/lang/String;)V
Access: 

```ssa
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0, lvar2_0, lvar3_0, nullconst));
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   

```

### Method: evaluate(DD)D
Access: public

```ssa
BLOCK B:
   return {lvar1_0 % lvar3_0};
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar3_0 = lvar3_0);
   

```


## Class: dev/sim0n/evaluator/util/stats/Calculations
Super: java/lang/Object
Interfaces: []
Access: public synchronized

### Method: <init>()V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   _consume(lvar0_0.<init>());
   svar1_0 = new java.util.LinkedList;
   _consume(svar1_0.<init>());
   lvar0_0.intCalculations = svar1_0;
   svar1_1 = new java.util.LinkedList;
   _consume(svar1_1.<init>());
   lvar0_0.doubleCalculations = svar1_1;
   return;
   

```

### Method: run(Ldev/sim0n/evaluator/util/Log;)V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK C:
   lvar3_0 = lvar0_0.doubleCalculations.stream().filter(dynamic_invoke<java.util.function.Predicate>(java.lang.invoke.LambdaMetafactory.metafactory(methodTypeOf((Ljava/lang/Object;)Z), handleOf(dev/sim0n/evaluator/util/stats/Calculations.lambda$run$1(Ljava/lang/Double;)Z (6)), methodTypeOf((Ljava/lang/Double;)Z)))).mapToDouble(dynamic_invoke<java.util.function.ToDoubleFunction>(java.lang.invoke.LambdaMetafactory.metafactory(methodTypeOf((Ljava/lang/Object;)D), handleOf(dev/sim0n/evaluator/util/stats/Calculations.lambda$run$2(Ljava/lang/Double;)D (6)), methodTypeOf((Ljava/lang/Double;)D)))).average();
   if (lvar3_0.isPresent() != 0)
      goto E
   
BLOCK E:
   svar2_1 = new java.lang.Object[2];
   svar2_1[0] = java.lang.Double.valueOf(lvar2_0.getAsDouble());
   svar2_1[1] = java.lang.Double.valueOf(lvar3_0.getAsDouble());
   _consume(lvar1_0.print("Averages for (i, d): %s, %s", svar2_1));
   return;
   
BLOCK F:
   svar0_18 = new java.lang.AssertionError;
   _consume(svar0_18.<init>());
   throw svar0_18;
   
BLOCK B:
   _consume(lvar1_0.println("
   Computing statistics"));
   lvar2_0 = lvar0_0.intCalculations.stream().mapToInt(dynamic_invoke<java.util.function.ToIntFunction>(java.lang.invoke.LambdaMetafactory.metafactory(methodTypeOf((Ljava/lang/Object;)I), handleOf(dev/sim0n/evaluator/util/stats/Calculations.lambda$run$0(Ljava/lang/Integer;)I (6)), methodTypeOf((Ljava/lang/Integer;)I)))).average();
   if (lvar2_0.isPresent() != 0)
      goto C
   
BLOCK D:
   svar0_16 = new java.lang.AssertionError;
   _consume(svar0_16.<init>());
   throw svar0_16;
   

```

### Method: store(I)I
Access: public

```ssa
BLOCK B:
   svar0_2 = lvar0_0.intCalculations.add(java.lang.Integer.valueOf(lvar1_0));
   return lvar1_0;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   

```

### Method: store(D)D
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK B:
   svar0_2 = lvar0_0.doubleCalculations.add(java.lang.Double.valueOf(lvar1_0));
   return lvar1_0;
   

```

### Method: getIntCalculations()Ljava/util/List;
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   return lvar0_0.intCalculations;
   

```

### Method: getDoubleCalculations()Ljava/util/List;
Access: public

```ssa
BLOCK B:
   return lvar0_0.doubleCalculations;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   

```


## Class: dev/sim0n/evaluator/util/crypto/Blowfish$BlowfishECB
Super: java/lang/Object
Interfaces: []
Access: synchronized

### Method: <init>([B)V
Access: public

```ssa
BLOCK M:
   lvar7_1 = ɸ{L:lvar7_0, AA:lvar7_10};
   lvar2_9 = ɸ{L:lvar2_8, AA:lvar2_22};
   if (lvar2_9 >= 18)
      goto N
   
BLOCK B:
   _consume(lvar0_0.<init>());
   lvar0_0.m_pbox = new int[18];
   lvar2_0 = 0;
   
BLOCK L:
   lvar7_0 = 0L;
   lvar2_8 = 0;
   
BLOCK H:
   if (lvar1_0.length != 0)
      goto J
   
BLOCK AE:
   svar0_73 = {lvar5_2 << 8};
   svar1_47 = lvar1_0[lvar4_2];
   svar1_48 = {svar1_47 & 255};
   svar0_74 = {svar0_73 | svar1_48};
   lvar5_3 = svar0_74;
   lvar4_3 = {lvar4_2 + 1};
   if (lvar4_3 != lvar1_0.length)
      goto AG
   
BLOCK AF:
   lvar4_4 = 0;
   
BLOCK G:
   svar0_13 = lvar0_0.m_sbox1;
   svar2_2 = dev.sim0n.evaluator.util.crypto.Blowfish$BlowfishECB.sbox_init_1;
   svar2_3 = svar2_2[lvar2_4];
   svar0_13[lvar2_4] = svar2_3;
   svar0_15 = lvar0_0.m_sbox2;
   svar2_4 = dev.sim0n.evaluator.util.crypto.Blowfish$BlowfishECB.sbox_init_2;
   svar2_5 = svar2_4[lvar2_4];
   svar0_15[lvar2_4] = svar2_5;
   svar0_17 = lvar0_0.m_sbox3;
   svar2_6 = dev.sim0n.evaluator.util.crypto.Blowfish$BlowfishECB.sbox_init_3;
   svar2_7 = svar2_6[lvar2_4];
   svar0_17[lvar2_4] = svar2_7;
   svar0_19 = lvar0_0.m_sbox4;
   svar2_8 = dev.sim0n.evaluator.util.crypto.Blowfish$BlowfishECB.sbox_init_4;
   svar2_9 = svar2_8[lvar2_4];
   svar0_19[lvar2_4] = svar2_9;
   lvar2_5 = {lvar2_4 + 1};
   goto F
   
BLOCK O:
   lvar7_2 = ɸ{P:lvar7_3, N:lvar7_1};
   lvar2_11 = ɸ{P:lvar2_12, N:lvar2_10};
   if (lvar2_11 >= 256)
      goto Q
   
BLOCK AD:
   svar0_71 = lvar0_0.m_pbox;
   svar2_46 = svar0_71[lvar2_7];
   svar2_47 = {svar2_46 ^ lvar5_2};
   svar0_71[lvar2_7] = svar2_47;
   lvar2_23 = {lvar2_7 + 1};
   goto K
   
BLOCK N:
   lvar2_10 = 0;
   
BLOCK P:
   lvar7_3 = lvar0_0.encryptBlock(lvar7_2);
   svar0_35 = lvar0_0.m_sbox1;
   svar2_11 = {lvar7_3 >>> 32};
   svar0_35[lvar2_11] = (int)svar2_11;
   svar0_37 = lvar0_0.m_sbox1;
   svar1_23 = {lvar2_11 + 1};
   svar2_15 = {lvar7_3 & 4294967295L};
   svar0_37[svar1_23] = (int)svar2_15;
   lvar2_12 = {lvar2_11 + 2};
   goto O
   
BLOCK X:
   lvar7_8 = ɸ{W:lvar7_6, Y:lvar7_9};
   lvar2_20 = ɸ{W:lvar2_19, Y:lvar2_21};
   if (lvar2_20 >= 256)
      goto Z
   
BLOCK F:
   lvar2_4 = ɸ{G:lvar2_5, E:lvar2_3};
   if (lvar2_4 >= 256)
      goto H
   
BLOCK S:
   lvar7_5 = lvar0_0.encryptBlock(lvar7_4);
   svar0_43 = lvar0_0.m_sbox2;
   svar2_18 = {lvar7_5 >>> 32};
   svar0_43[lvar2_14] = (int)svar2_18;
   svar0_45 = lvar0_0.m_sbox2;
   svar1_28 = {lvar2_14 + 1};
   svar2_22 = {lvar7_5 & 4294967295L};
   svar0_45[svar1_28] = (int)svar2_22;
   lvar2_15 = {lvar2_14 + 2};
   goto R
   
BLOCK U:
   lvar7_6 = ɸ{V:lvar7_7, T:lvar7_4};
   lvar2_17 = ɸ{V:lvar2_18, T:lvar2_16};
   if (lvar2_17 >= 256)
      goto W
   
BLOCK W:
   lvar2_19 = 0;
   
BLOCK D:
   svar0_5 = lvar0_0.m_pbox;
   svar2_0 = dev.sim0n.evaluator.util.crypto.Blowfish$BlowfishECB.pbox_init;
   svar2_1 = svar2_0[lvar2_1];
   svar0_5[lvar2_1] = svar2_1;
   lvar2_2 = {lvar2_1 + 1};
   goto C
   
BLOCK Y:
   lvar7_9 = lvar0_0.encryptBlock(lvar7_8);
   svar0_59 = lvar0_0.m_sbox4;
   svar2_32 = {lvar7_9 >>> 32};
   svar0_59[lvar2_20] = (int)svar2_32;
   svar0_61 = lvar0_0.m_sbox4;
   svar1_38 = {lvar2_20 + 1};
   svar2_36 = {lvar7_9 & 4294967295L};
   svar0_61[svar1_38] = (int)svar2_36;
   lvar2_21 = {lvar2_20 + 2};
   goto X
   
BLOCK Z:
   return;
   
BLOCK C:
   lvar2_1 = ɸ{B:lvar2_0, D:lvar2_2};
   if (lvar2_1 >= 18)
      goto E
   
BLOCK I:
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK Q:
   lvar2_13 = 0;
   
BLOCK E:
   lvar0_0.m_sbox1 = new int[256];
   lvar0_0.m_sbox2 = new int[256];
   lvar0_0.m_sbox3 = new int[256];
   lvar0_0.m_sbox4 = new int[256];
   lvar2_3 = 0;
   
BLOCK R:
   lvar7_4 = ɸ{S:lvar7_5, Q:lvar7_2};
   lvar2_14 = ɸ{S:lvar2_15, Q:lvar2_13};
   if (lvar2_14 >= 256)
      goto T
   
BLOCK AA:
   lvar7_10 = lvar0_0.encryptBlock(lvar7_1);
   svar0_65 = lvar0_0.m_pbox;
   svar2_39 = {lvar7_10 >>> 32};
   svar0_65[lvar2_9] = (int)svar2_39;
   svar0_67 = lvar0_0.m_pbox;
   svar1_42 = {lvar2_9 + 1};
   svar2_43 = {lvar7_10 & 4294967295L};
   svar0_67[svar1_42] = (int)svar2_43;
   lvar2_22 = {lvar2_9 + 2};
   goto M
   
BLOCK K:
   lvar5_1 = ɸ{AD:lvar5_2, J:lvar5_0};
   lvar4_1 = ɸ{AD:lvar4_2, J:lvar4_0};
   lvar2_7 = ɸ{AD:lvar2_23, J:lvar2_6};
   if (lvar2_7 >= 18)
      goto L
   
BLOCK AC:
   lvar6_1 = ɸ{AG:lvar6_2, AB:lvar6_0};
   lvar5_2 = ɸ{AG:lvar5_3, AB:lvar5_1};
   lvar4_2 = ɸ{AG:lvar4_5, AB:lvar4_1};
   if (lvar6_1 >= 4)
      goto AD
   
BLOCK V:
   lvar7_7 = lvar0_0.encryptBlock(lvar7_6);
   svar0_51 = lvar0_0.m_sbox3;
   svar2_25 = {lvar7_7 >>> 32};
   svar0_51[lvar2_17] = (int)svar2_25;
   svar0_53 = lvar0_0.m_sbox3;
   svar1_33 = {lvar2_17 + 1};
   svar2_29 = {lvar7_7 & 4294967295L};
   svar0_53[svar1_33] = (int)svar2_29;
   lvar2_18 = {lvar2_17 + 2};
   goto U
   
BLOCK T:
   lvar2_16 = 0;
   
BLOCK AG:
   lvar4_5 = ɸ{AF:lvar4_4, AE:lvar4_3};
   lvar6_2 = {lvar6_1 + 1};
   goto AC
   
BLOCK J:
   lvar4_0 = 0;
   lvar5_0 = 0;
   lvar2_6 = 0;
   
BLOCK AB:
   lvar6_0 = 0;
   

```

### Method: cleanUp()V
Access: public

```ssa
BLOCK F:
   lvar1_4 = ɸ{E:lvar1_3, G:lvar1_5};
   if (lvar1_4 >= 256)
      goto H
   
BLOCK C:
   lvar1_1 = ɸ{B:lvar1_0, D:lvar1_2};
   if (lvar1_1 >= 18)
      goto E
   
BLOCK B:
   lvar1_0 = 0;
   
BLOCK H:
   return;
   
BLOCK D:
   svar0_3 = lvar0_0.m_pbox;
   svar0_3[lvar1_1] = 0;
   lvar1_2 = {lvar1_1 + 1};
   goto C
   
BLOCK E:
   lvar1_3 = 0;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK G:
   svar0_7 = lvar0_0.m_sbox1;
   svar2_2 = lvar0_0.m_sbox2;
   svar4_1 = lvar0_0.m_sbox3;
   svar6_1 = lvar0_0.m_sbox4;
   svar6_1[lvar1_4] = 0;
   svar4_1[lvar1_4] = 0;
   svar2_2[lvar1_4] = 0;
   svar0_7[lvar1_4] = 0;
   lvar1_5 = {lvar1_4 + 1};
   goto F
   

```

### Method: selfTest()Z
Access: public static

```ssa
BLOCK F:
   return 0;
   
BLOCK I:
   _consume(lvar10_0.decrypt(lvar8_0));
   svar0_37 = lvar8_0[0];
   svar1_42 = lvar6_0[0];
   if (svar0_37 != svar1_42)
      goto L
   
BLOCK J:
   svar0_39 = lvar8_0[1];
   svar1_45 = lvar6_0[1];
   if (svar0_39 == svar1_45)
      goto K
   
BLOCK B:
   lvar0_0 = new byte[8];
   lvar0_0[0] = 28;
   lvar0_0[1] = 88;
   lvar0_0[2] = 127;
   lvar0_0[3] = 28;
   lvar0_0[4] = 19;
   lvar0_0[5] = -110;
   lvar0_0[6] = 79;
   lvar0_0[7] = -17;
   lvar1_0 = new int[2];
   lvar1_0[0] = 810889768;
   lvar1_0[1] = 1836001626;
   lvar2_0 = new int[2];
   lvar2_0[0] = 1439381364;
   lvar2_0[1] = -784403967;
   lvar3_0 = new int[2];
   lvar5_0 = "Who is John Galt?".getBytes();
   lvar6_0 = new int[2];
   lvar6_0[0] = -19088744;
   lvar6_0[1] = 1985229328;
   lvar7_0 = new int[2];
   lvar7_0[0] = -862883029;
   lvar7_0[1] = -2145192316;
   lvar8_0 = new int[2];
   lvar9_0 = new dev.sim0n.evaluator.util.crypto.Blowfish$BlowfishECB;
   _consume(lvar9_0.<init>(lvar0_0));
   _consume(lvar9_0.encrypt(lvar1_0, lvar3_0));
   svar0_20 = lvar3_0[0];
   svar1_20 = lvar2_0[0];
   if (svar0_20 != svar1_20)
      goto N
   
BLOCK M:
   return 0;
   
BLOCK H:
   svar0_34 = lvar8_0[1];
   svar1_38 = lvar7_0[1];
   if (svar0_34 == svar1_38)
      goto I
   
BLOCK D:
   _consume(lvar9_0.decrypt(lvar3_0));
   svar0_25 = lvar3_0[0];
   svar1_27 = lvar1_0[0];
   if (svar0_25 != svar1_27)
      goto F
   
BLOCK K:
   return 1;
   
BLOCK A:
   
BLOCK E:
   svar0_27 = lvar3_0[1];
   svar1_30 = lvar1_0[1];
   if (svar0_27 == svar1_30)
      goto G
   
BLOCK L:
   return 0;
   
BLOCK G:
   lvar10_0 = new dev.sim0n.evaluator.util.crypto.Blowfish$BlowfishECB;
   _consume(lvar10_0.<init>(lvar5_0));
   _consume(lvar10_0.encrypt(lvar6_0, lvar8_0));
   svar0_32 = lvar8_0[0];
   svar1_35 = lvar7_0[0];
   if (svar0_32 != svar1_35)
      goto M
   
BLOCK N:
   return 0;
   
BLOCK C:
   svar0_22 = lvar3_0[1];
   svar1_23 = lvar2_0[1];
   if (svar0_22 == svar1_23)
      goto D
   

```

### Method: encryptBlock(J)J
Access: protected

```ssa
BLOCK B:
   svar1_1 = (lvar0_0.m_pbox)[0];
   lvar3_1 = {dev.sim0n.evaluator.util.crypto.Blowfish.access$000(lvar1_0) ^ svar1_1};
   svar1_3 = (lvar0_0.m_sbox1)[{lvar3_1 >>> 24}];
   svar2_4 = (lvar0_0.m_sbox2)[{{lvar3_1 >>> 16} & 255}];
   svar2_6 = (lvar0_0.m_sbox3)[{{lvar3_1 >>> 8} & 255}];
   svar2_8 = (lvar0_0.m_sbox4)[{lvar3_1 & 255}];
   svar2_10 = (lvar0_0.m_pbox)[1];
   lvar4_1 = {dev.sim0n.evaluator.util.crypto.Blowfish.access$100(lvar1_0) ^ {{({{svar1_3 + svar2_4} ^ svar2_6}) + svar2_8} ^ svar2_10}};
   svar1_9 = (lvar0_0.m_sbox1)[{lvar4_1 >>> 24}];
   svar2_14 = (lvar0_0.m_sbox2)[{{lvar4_1 >>> 16} & 255}];
   svar2_16 = (lvar0_0.m_sbox3)[{{lvar4_1 >>> 8} & 255}];
   svar2_18 = (lvar0_0.m_sbox4)[{lvar4_1 & 255}];
   svar2_20 = (lvar0_0.m_pbox)[2];
   lvar3_2 = {lvar3_1 ^ {{({{svar1_9 + svar2_14} ^ svar2_16}) + svar2_18} ^ svar2_20}};
   svar1_15 = (lvar0_0.m_sbox1)[{lvar3_2 >>> 24}];
   svar2_24 = (lvar0_0.m_sbox2)[{{lvar3_2 >>> 16} & 255}];
   svar2_26 = (lvar0_0.m_sbox3)[{{lvar3_2 >>> 8} & 255}];
   svar2_28 = (lvar0_0.m_sbox4)[{lvar3_2 & 255}];
   svar2_30 = (lvar0_0.m_pbox)[3];
   lvar4_2 = {lvar4_1 ^ {{({{svar1_15 + svar2_24} ^ svar2_26}) + svar2_28} ^ svar2_30}};
   svar1_21 = (lvar0_0.m_sbox1)[{lvar4_2 >>> 24}];
   svar2_34 = (lvar0_0.m_sbox2)[{{lvar4_2 >>> 16} & 255}];
   svar2_36 = (lvar0_0.m_sbox3)[{{lvar4_2 >>> 8} & 255}];
   svar2_38 = (lvar0_0.m_sbox4)[{lvar4_2 & 255}];
   svar2_40 = (lvar0_0.m_pbox)[4];
   lvar3_3 = {lvar3_2 ^ {{({{svar1_21 + svar2_34} ^ svar2_36}) + svar2_38} ^ svar2_40}};
   svar1_27 = (lvar0_0.m_sbox1)[{lvar3_3 >>> 24}];
   svar2_44 = (lvar0_0.m_sbox2)[{{lvar3_3 >>> 16} & 255}];
   svar2_46 = (lvar0_0.m_sbox3)[{{lvar3_3 >>> 8} & 255}];
   svar2_48 = (lvar0_0.m_sbox4)[{lvar3_3 & 255}];
   svar2_50 = (lvar0_0.m_pbox)[5];
   lvar4_3 = {lvar4_2 ^ {{({{svar1_27 + svar2_44} ^ svar2_46}) + svar2_48} ^ svar2_50}};
   svar1_33 = (lvar0_0.m_sbox1)[{lvar4_3 >>> 24}];
   svar2_54 = (lvar0_0.m_sbox2)[{{lvar4_3 >>> 16} & 255}];
   svar2_56 = (lvar0_0.m_sbox3)[{{lvar4_3 >>> 8} & 255}];
   svar2_58 = (lvar0_0.m_sbox4)[{lvar4_3 & 255}];
   svar2_60 = (lvar0_0.m_pbox)[6];
   lvar3_4 = {lvar3_3 ^ {{({{svar1_33 + svar2_54} ^ svar2_56}) + svar2_58} ^ svar2_60}};
   svar1_39 = (lvar0_0.m_sbox1)[{lvar3_4 >>> 24}];
   svar2_64 = (lvar0_0.m_sbox2)[{{lvar3_4 >>> 16} & 255}];
   svar2_66 = (lvar0_0.m_sbox3)[{{lvar3_4 >>> 8} & 255}];
   svar2_68 = (lvar0_0.m_sbox4)[{lvar3_4 & 255}];
   svar2_70 = (lvar0_0.m_pbox)[7];
   lvar4_4 = {lvar4_3 ^ {{({{svar1_39 + svar2_64} ^ svar2_66}) + svar2_68} ^ svar2_70}};
   svar1_45 = (lvar0_0.m_sbox1)[{lvar4_4 >>> 24}];
   svar2_74 = (lvar0_0.m_sbox2)[{{lvar4_4 >>> 16} & 255}];
   svar2_76 = (lvar0_0.m_sbox3)[{{lvar4_4 >>> 8} & 255}];
   svar2_78 = (lvar0_0.m_sbox4)[{lvar4_4 & 255}];
   svar2_80 = (lvar0_0.m_pbox)[8];
   lvar3_5 = {lvar3_4 ^ {{({{svar1_45 + svar2_74} ^ svar2_76}) + svar2_78} ^ svar2_80}};
   svar1_51 = (lvar0_0.m_sbox1)[{lvar3_5 >>> 24}];
   svar2_84 = (lvar0_0.m_sbox2)[{{lvar3_5 >>> 16} & 255}];
   svar2_86 = (lvar0_0.m_sbox3)[{{lvar3_5 >>> 8} & 255}];
   svar2_88 = (lvar0_0.m_sbox4)[{lvar3_5 & 255}];
   svar2_90 = (lvar0_0.m_pbox)[9];
   lvar4_5 = {lvar4_4 ^ {{({{svar1_51 + svar2_84} ^ svar2_86}) + svar2_88} ^ svar2_90}};
   svar1_57 = (lvar0_0.m_sbox1)[{lvar4_5 >>> 24}];
   svar2_94 = (lvar0_0.m_sbox2)[{{lvar4_5 >>> 16} & 255}];
   svar2_96 = (lvar0_0.m_sbox3)[{{lvar4_5 >>> 8} & 255}];
   svar2_98 = (lvar0_0.m_sbox4)[{lvar4_5 & 255}];
   svar2_100 = (lvar0_0.m_pbox)[10];
   lvar3_6 = {lvar3_5 ^ {{({{svar1_57 + svar2_94} ^ svar2_96}) + svar2_98} ^ svar2_100}};
   svar1_63 = (lvar0_0.m_sbox1)[{lvar3_6 >>> 24}];
   svar2_104 = (lvar0_0.m_sbox2)[{{lvar3_6 >>> 16} & 255}];
   svar2_106 = (lvar0_0.m_sbox3)[{{lvar3_6 >>> 8} & 255}];
   svar2_108 = (lvar0_0.m_sbox4)[{lvar3_6 & 255}];
   svar2_110 = (lvar0_0.m_pbox)[11];
   lvar4_6 = {lvar4_5 ^ {{({{svar1_63 + svar2_104} ^ svar2_106}) + svar2_108} ^ svar2_110}};
   svar1_69 = (lvar0_0.m_sbox1)[{lvar4_6 >>> 24}];
   svar2_114 = (lvar0_0.m_sbox2)[{{lvar4_6 >>> 16} & 255}];
   svar2_116 = (lvar0_0.m_sbox3)[{{lvar4_6 >>> 8} & 255}];
   svar2_118 = (lvar0_0.m_sbox4)[{lvar4_6 & 255}];
   svar2_120 = (lvar0_0.m_pbox)[12];
   lvar3_7 = {lvar3_6 ^ {{({{svar1_69 + svar2_114} ^ svar2_116}) + svar2_118} ^ svar2_120}};
   svar1_75 = (lvar0_0.m_sbox1)[{lvar3_7 >>> 24}];
   svar2_124 = (lvar0_0.m_sbox2)[{{lvar3_7 >>> 16} & 255}];
   svar2_126 = (lvar0_0.m_sbox3)[{{lvar3_7 >>> 8} & 255}];
   svar2_128 = (lvar0_0.m_sbox4)[{lvar3_7 & 255}];
   svar2_130 = (lvar0_0.m_pbox)[13];
   lvar4_7 = {lvar4_6 ^ {{({{svar1_75 + svar2_124} ^ svar2_126}) + svar2_128} ^ svar2_130}};
   svar1_81 = (lvar0_0.m_sbox1)[{lvar4_7 >>> 24}];
   svar2_134 = (lvar0_0.m_sbox2)[{{lvar4_7 >>> 16} & 255}];
   svar2_136 = (lvar0_0.m_sbox3)[{{lvar4_7 >>> 8} & 255}];
   svar2_138 = (lvar0_0.m_sbox4)[{lvar4_7 & 255}];
   svar2_140 = (lvar0_0.m_pbox)[14];
   lvar3_8 = {lvar3_7 ^ {{({{svar1_81 + svar2_134} ^ svar2_136}) + svar2_138} ^ svar2_140}};
   svar1_87 = (lvar0_0.m_sbox1)[{lvar3_8 >>> 24}];
   svar2_144 = (lvar0_0.m_sbox2)[{{lvar3_8 >>> 16} & 255}];
   svar2_146 = (lvar0_0.m_sbox3)[{{lvar3_8 >>> 8} & 255}];
   svar2_148 = (lvar0_0.m_sbox4)[{lvar3_8 & 255}];
   svar2_150 = (lvar0_0.m_pbox)[15];
   lvar4_8 = {lvar4_7 ^ {{({{svar1_87 + svar2_144} ^ svar2_146}) + svar2_148} ^ svar2_150}};
   svar1_93 = (lvar0_0.m_sbox1)[{lvar4_8 >>> 24}];
   svar2_154 = (lvar0_0.m_sbox2)[{{lvar4_8 >>> 16} & 255}];
   svar2_156 = (lvar0_0.m_sbox3)[{{lvar4_8 >>> 8} & 255}];
   svar2_158 = (lvar0_0.m_sbox4)[{lvar4_8 & 255}];
   svar2_160 = (lvar0_0.m_pbox)[16];
   svar2_162 = (lvar0_0.m_pbox)[17];
   return dev.sim0n.evaluator.util.crypto.Blowfish.access$200({lvar3_8 ^ {{({{svar1_93 + svar2_154} ^ svar2_156}) + svar2_158} ^ svar2_160}}, {lvar4_8 ^ svar2_162});
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   

```

### Method: decryptBlock(J)J
Access: protected

```ssa
BLOCK B:
   svar1_2 = (lvar0_0.m_pbox)[17];
   lvar3_1 = {dev.sim0n.evaluator.util.crypto.Blowfish.access$000(lvar1_0) ^ svar1_2};
   svar1_5 = (lvar0_0.m_sbox1)[{lvar3_1 >>> 24}];
   svar2_5 = (lvar0_0.m_sbox2)[{{lvar3_1 >>> 16} & 255}];
   svar2_8 = (lvar0_0.m_sbox3)[{{lvar3_1 >>> 8} & 255}];
   svar2_11 = (lvar0_0.m_sbox4)[{lvar3_1 & 255}];
   svar2_14 = (lvar0_0.m_pbox)[16];
   lvar4_1 = {dev.sim0n.evaluator.util.crypto.Blowfish.access$100(lvar1_0) ^ {{({{svar1_5 + svar2_5} ^ svar2_8}) + svar2_11} ^ svar2_14}};
   svar1_12 = (lvar0_0.m_sbox1)[{lvar4_1 >>> 24}];
   svar2_19 = (lvar0_0.m_sbox2)[{{lvar4_1 >>> 16} & 255}];
   svar2_22 = (lvar0_0.m_sbox3)[{{lvar4_1 >>> 8} & 255}];
   svar2_25 = (lvar0_0.m_sbox4)[{lvar4_1 & 255}];
   svar2_28 = (lvar0_0.m_pbox)[15];
   lvar3_2 = {lvar3_1 ^ {{({{svar1_12 + svar2_19} ^ svar2_22}) + svar2_25} ^ svar2_28}};
   svar1_19 = (lvar0_0.m_sbox1)[{lvar3_2 >>> 24}];
   svar2_33 = (lvar0_0.m_sbox2)[{{lvar3_2 >>> 16} & 255}];
   svar2_36 = (lvar0_0.m_sbox3)[{{lvar3_2 >>> 8} & 255}];
   svar2_39 = (lvar0_0.m_sbox4)[{lvar3_2 & 255}];
   svar2_42 = (lvar0_0.m_pbox)[14];
   lvar4_2 = {lvar4_1 ^ {{({{svar1_19 + svar2_33} ^ svar2_36}) + svar2_39} ^ svar2_42}};
   svar1_26 = (lvar0_0.m_sbox1)[{lvar4_2 >>> 24}];
   svar2_47 = (lvar0_0.m_sbox2)[{{lvar4_2 >>> 16} & 255}];
   svar2_50 = (lvar0_0.m_sbox3)[{{lvar4_2 >>> 8} & 255}];
   svar2_53 = (lvar0_0.m_sbox4)[{lvar4_2 & 255}];
   svar2_56 = (lvar0_0.m_pbox)[13];
   lvar3_3 = {lvar3_2 ^ {{({{svar1_26 + svar2_47} ^ svar2_50}) + svar2_53} ^ svar2_56}};
   svar1_33 = (lvar0_0.m_sbox1)[{lvar3_3 >>> 24}];
   svar2_61 = (lvar0_0.m_sbox2)[{{lvar3_3 >>> 16} & 255}];
   svar2_64 = (lvar0_0.m_sbox3)[{{lvar3_3 >>> 8} & 255}];
   svar2_67 = (lvar0_0.m_sbox4)[{lvar3_3 & 255}];
   svar2_70 = (lvar0_0.m_pbox)[12];
   lvar4_3 = {lvar4_2 ^ {{({{svar1_33 + svar2_61} ^ svar2_64}) + svar2_67} ^ svar2_70}};
   svar1_40 = (lvar0_0.m_sbox1)[{lvar4_3 >>> 24}];
   svar2_75 = (lvar0_0.m_sbox2)[{{lvar4_3 >>> 16} & 255}];
   svar2_78 = (lvar0_0.m_sbox3)[{{lvar4_3 >>> 8} & 255}];
   svar2_81 = (lvar0_0.m_sbox4)[{lvar4_3 & 255}];
   svar2_84 = (lvar0_0.m_pbox)[11];
   lvar3_4 = {lvar3_3 ^ {{({{svar1_40 + svar2_75} ^ svar2_78}) + svar2_81} ^ svar2_84}};
   svar1_47 = (lvar0_0.m_sbox1)[{lvar3_4 >>> 24}];
   svar2_89 = (lvar0_0.m_sbox2)[{{lvar3_4 >>> 16} & 255}];
   svar2_92 = (lvar0_0.m_sbox3)[{{lvar3_4 >>> 8} & 255}];
   svar2_95 = (lvar0_0.m_sbox4)[{lvar3_4 & 255}];
   svar2_98 = (lvar0_0.m_pbox)[10];
   lvar4_4 = {lvar4_3 ^ {{({{svar1_47 + svar2_89} ^ svar2_92}) + svar2_95} ^ svar2_98}};
   svar1_54 = (lvar0_0.m_sbox1)[{lvar4_4 >>> 24}];
   svar2_103 = (lvar0_0.m_sbox2)[{{lvar4_4 >>> 16} & 255}];
   svar2_106 = (lvar0_0.m_sbox3)[{{lvar4_4 >>> 8} & 255}];
   svar2_109 = (lvar0_0.m_sbox4)[{lvar4_4 & 255}];
   svar2_112 = (lvar0_0.m_pbox)[9];
   lvar3_5 = {lvar3_4 ^ {{({{svar1_54 + svar2_103} ^ svar2_106}) + svar2_109} ^ svar2_112}};
   svar1_61 = (lvar0_0.m_sbox1)[{lvar3_5 >>> 24}];
   svar2_117 = (lvar0_0.m_sbox2)[{{lvar3_5 >>> 16} & 255}];
   svar2_120 = (lvar0_0.m_sbox3)[{{lvar3_5 >>> 8} & 255}];
   svar2_123 = (lvar0_0.m_sbox4)[{lvar3_5 & 255}];
   svar2_126 = (lvar0_0.m_pbox)[8];
   lvar4_5 = {lvar4_4 ^ {{({{svar1_61 + svar2_117} ^ svar2_120}) + svar2_123} ^ svar2_126}};
   svar1_68 = (lvar0_0.m_sbox1)[{lvar4_5 >>> 24}];
   svar2_131 = (lvar0_0.m_sbox2)[{{lvar4_5 >>> 16} & 255}];
   svar2_134 = (lvar0_0.m_sbox3)[{{lvar4_5 >>> 8} & 255}];
   svar2_137 = (lvar0_0.m_sbox4)[{lvar4_5 & 255}];
   svar2_140 = (lvar0_0.m_pbox)[7];
   lvar3_6 = {lvar3_5 ^ {{({{svar1_68 + svar2_131} ^ svar2_134}) + svar2_137} ^ svar2_140}};
   svar1_75 = (lvar0_0.m_sbox1)[{lvar3_6 >>> 24}];
   svar2_145 = (lvar0_0.m_sbox2)[{{lvar3_6 >>> 16} & 255}];
   svar2_148 = (lvar0_0.m_sbox3)[{{lvar3_6 >>> 8} & 255}];
   svar2_151 = (lvar0_0.m_sbox4)[{lvar3_6 & 255}];
   svar2_154 = (lvar0_0.m_pbox)[6];
   lvar4_6 = {lvar4_5 ^ {{({{svar1_75 + svar2_145} ^ svar2_148}) + svar2_151} ^ svar2_154}};
   svar1_82 = (lvar0_0.m_sbox1)[{lvar4_6 >>> 24}];
   svar2_159 = (lvar0_0.m_sbox2)[{{lvar4_6 >>> 16} & 255}];
   svar2_162 = (lvar0_0.m_sbox3)[{{lvar4_6 >>> 8} & 255}];
   svar2_165 = (lvar0_0.m_sbox4)[{lvar4_6 & 255}];
   svar2_168 = (lvar0_0.m_pbox)[5];
   lvar3_7 = {lvar3_6 ^ {{({{svar1_82 + svar2_159} ^ svar2_162}) + svar2_165} ^ svar2_168}};
   svar1_89 = (lvar0_0.m_sbox1)[{lvar3_7 >>> 24}];
   svar2_173 = (lvar0_0.m_sbox2)[{{lvar3_7 >>> 16} & 255}];
   svar2_176 = (lvar0_0.m_sbox3)[{{lvar3_7 >>> 8} & 255}];
   svar2_179 = (lvar0_0.m_sbox4)[{lvar3_7 & 255}];
   svar2_182 = (lvar0_0.m_pbox)[4];
   lvar4_7 = {lvar4_6 ^ {{({{svar1_89 + svar2_173} ^ svar2_176}) + svar2_179} ^ svar2_182}};
   svar1_96 = (lvar0_0.m_sbox1)[{lvar4_7 >>> 24}];
   svar2_187 = (lvar0_0.m_sbox2)[{{lvar4_7 >>> 16} & 255}];
   svar2_190 = (lvar0_0.m_sbox3)[{{lvar4_7 >>> 8} & 255}];
   svar2_193 = (lvar0_0.m_sbox4)[{lvar4_7 & 255}];
   svar2_196 = (lvar0_0.m_pbox)[3];
   lvar3_8 = {lvar3_7 ^ {{({{svar1_96 + svar2_187} ^ svar2_190}) + svar2_193} ^ svar2_196}};
   svar1_103 = (lvar0_0.m_sbox1)[{lvar3_8 >>> 24}];
   svar2_201 = (lvar0_0.m_sbox2)[{{lvar3_8 >>> 16} & 255}];
   svar2_204 = (lvar0_0.m_sbox3)[{{lvar3_8 >>> 8} & 255}];
   svar2_207 = (lvar0_0.m_sbox4)[{lvar3_8 & 255}];
   svar2_210 = (lvar0_0.m_pbox)[2];
   lvar4_8 = {lvar4_7 ^ {{({{svar1_103 + svar2_201} ^ svar2_204}) + svar2_207} ^ svar2_210}};
   svar1_110 = (lvar0_0.m_sbox1)[{lvar4_8 >>> 24}];
   svar2_215 = (lvar0_0.m_sbox2)[{{lvar4_8 >>> 16} & 255}];
   svar2_218 = (lvar0_0.m_sbox3)[{{lvar4_8 >>> 8} & 255}];
   svar2_221 = (lvar0_0.m_sbox4)[{lvar4_8 & 255}];
   svar2_224 = (lvar0_0.m_pbox)[1];
   svar2_227 = (lvar0_0.m_pbox)[0];
   return dev.sim0n.evaluator.util.crypto.Blowfish.access$200({lvar3_8 ^ {{({{svar1_110 + svar2_215} ^ svar2_218}) + svar2_221} ^ svar2_224}}, {lvar4_8 ^ svar2_227});
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   

```

### Method: encrypt([B[B)V
Access: public

```ssa
BLOCK D:
   lvar4_0 = dev.sim0n.evaluator.util.crypto.Blowfish.access$300(lvar1_0, lvar6_1);
   lvar4_1 = lvar0_0.encryptBlock(lvar4_0);
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$400(lvar4_1, lvar2_0, lvar6_1));
   lvar6_2 = {lvar6_1 + 8};
   goto C
   
BLOCK E:
   return;
   
BLOCK B:
   lvar6_0 = 0;
   
BLOCK C:
   lvar6_1 = ɸ{D:lvar6_2, B:lvar6_0};
   if (lvar6_1 >= lvar1_0.length)
      goto E
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   

```

### Method: encrypt([B)V
Access: public

```ssa
BLOCK B:
   lvar5_0 = 0;
   
BLOCK E:
   return;
   
BLOCK D:
   lvar3_0 = dev.sim0n.evaluator.util.crypto.Blowfish.access$300(lvar1_0, lvar5_1);
   lvar3_1 = lvar0_0.encryptBlock(lvar3_0);
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$400(lvar3_1, lvar1_0, lvar5_1));
   lvar5_2 = {lvar5_1 + 8};
   goto C
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK C:
   lvar5_1 = ɸ{B:lvar5_0, D:lvar5_2};
   if (lvar5_1 >= lvar1_0.length)
      goto E
   

```

### Method: encrypt([I[I)V
Access: public

```ssa
BLOCK E:
   lvar4_0 = dev.sim0n.evaluator.util.crypto.Blowfish.access$500(lvar1_0, lvar6_1);
   lvar4_1 = lvar0_0.encryptBlock(lvar4_0);
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$600(lvar4_1, lvar2_0, lvar6_1));
   lvar6_2 = {lvar6_1 + 2};
   goto C
   
BLOCK D:
   return;
   
BLOCK C:
   lvar6_1 = ɸ{E:lvar6_2, B:lvar6_0};
   if (lvar6_1 >= lvar1_0.length)
      goto D
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   
BLOCK B:
   lvar6_0 = 0;
   

```

### Method: encrypt([I)V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK C:
   lvar5_1 = ɸ{D:lvar5_2, B:lvar5_0};
   if (lvar5_1 >= lvar1_0.length)
      goto E
   
BLOCK D:
   lvar3_0 = dev.sim0n.evaluator.util.crypto.Blowfish.access$500(lvar1_0, lvar5_1);
   lvar3_1 = lvar0_0.encryptBlock(lvar3_0);
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$600(lvar3_1, lvar1_0, lvar5_1));
   lvar5_2 = {lvar5_1 + 2};
   goto C
   
BLOCK B:
   lvar5_0 = 0;
   
BLOCK E:
   return;
   

```

### Method: encrypt([J[J)V
Access: public

```ssa
BLOCK D:
   svar3_1 = lvar1_0[lvar4_1];
   svar2_1 = lvar0_0.encryptBlock(svar3_1);
   lvar2_0[lvar4_1] = svar2_1;
   lvar4_2 = {lvar4_1 + 1};
   goto C
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   
BLOCK B:
   lvar4_0 = 0;
   
BLOCK C:
   lvar4_1 = ɸ{D:lvar4_2, B:lvar4_0};
   if (lvar4_1 >= lvar1_0.length)
      goto E
   
BLOCK E:
   return;
   

```

### Method: encrypt([J)V
Access: public

```ssa
BLOCK E:
   svar3_1 = lvar1_0[lvar3_1];
   svar2_1 = lvar0_0.encryptBlock(svar3_1);
   lvar1_0[lvar3_1] = svar2_1;
   lvar3_2 = {lvar3_1 + 1};
   goto C
   
BLOCK D:
   return;
   
BLOCK B:
   lvar3_0 = 0;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK C:
   lvar3_1 = ɸ{E:lvar3_2, B:lvar3_0};
   if (lvar3_1 >= lvar1_0.length)
      goto D
   

```

### Method: decrypt([B[B)V
Access: public

```ssa
BLOCK C:
   lvar6_1 = ɸ{B:lvar6_0, E:lvar6_2};
   if (lvar6_1 >= lvar1_0.length)
      goto D
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   
BLOCK D:
   return;
   
BLOCK B:
   lvar6_0 = 0;
   
BLOCK E:
   lvar4_0 = dev.sim0n.evaluator.util.crypto.Blowfish.access$300(lvar1_0, lvar6_1);
   lvar4_1 = lvar0_0.decryptBlock(lvar4_0);
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$400(lvar4_1, lvar2_0, lvar6_1));
   lvar6_2 = {lvar6_1 + 8};
   goto C
   

```

### Method: decrypt([B)V
Access: public

```ssa
BLOCK C:
   lvar5_1 = ɸ{D:lvar5_2, B:lvar5_0};
   if (lvar5_1 >= lvar1_0.length)
      goto E
   
BLOCK E:
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK D:
   lvar3_0 = dev.sim0n.evaluator.util.crypto.Blowfish.access$300(lvar1_0, lvar5_1);
   lvar3_1 = lvar0_0.decryptBlock(lvar3_0);
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$400(lvar3_1, lvar1_0, lvar5_1));
   lvar5_2 = {lvar5_1 + 8};
   goto C
   
BLOCK B:
   lvar5_0 = 0;
   

```

### Method: decrypt([I[I)V
Access: public

```ssa
BLOCK D:
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   
BLOCK E:
   lvar4_0 = dev.sim0n.evaluator.util.crypto.Blowfish.access$500(lvar1_0, lvar6_1);
   lvar4_1 = lvar0_0.decryptBlock(lvar4_0);
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$600(lvar4_1, lvar2_0, lvar6_1));
   lvar6_2 = {lvar6_1 + 2};
   goto C
   
BLOCK C:
   lvar6_1 = ɸ{E:lvar6_2, B:lvar6_0};
   if (lvar6_1 >= lvar1_0.length)
      goto D
   
BLOCK B:
   lvar6_0 = 0;
   

```

### Method: decrypt([I)V
Access: public

```ssa
BLOCK B:
   lvar5_0 = 0;
   
BLOCK D:
   lvar3_0 = dev.sim0n.evaluator.util.crypto.Blowfish.access$500(lvar1_0, lvar5_1);
   lvar3_1 = lvar0_0.decryptBlock(lvar3_0);
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$600(lvar3_1, lvar1_0, lvar5_1));
   lvar5_2 = {lvar5_1 + 2};
   goto C
   
BLOCK C:
   lvar5_1 = ɸ{B:lvar5_0, D:lvar5_2};
   if (lvar5_1 >= lvar1_0.length)
      goto E
   
BLOCK E:
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   

```

### Method: decrypt([J[J)V
Access: public

```ssa
BLOCK E:
   svar3_1 = lvar1_0[lvar4_1];
   svar2_1 = lvar0_0.decryptBlock(svar3_1);
   lvar2_0[lvar4_1] = svar2_1;
   lvar4_2 = {lvar4_1 + 1};
   goto C
   
BLOCK D:
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   
BLOCK B:
   lvar4_0 = 0;
   
BLOCK C:
   lvar4_1 = ɸ{E:lvar4_2, B:lvar4_0};
   if (lvar4_1 >= lvar1_0.length)
      goto D
   

```

### Method: decrypt([J)V
Access: public

```ssa
BLOCK D:
   svar3_1 = lvar1_0[lvar3_1];
   svar2_1 = lvar0_0.decryptBlock(svar3_1);
   lvar1_0[lvar3_1] = svar2_1;
   lvar3_2 = {lvar3_1 + 1};
   goto C
   
BLOCK E:
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK C:
   lvar3_1 = ɸ{D:lvar3_2, B:lvar3_0};
   if (lvar3_1 >= lvar1_0.length)
      goto E
   
BLOCK B:
   lvar3_0 = 0;
   

```

### Method: <clinit>()V
Access: static

```ssa
BLOCK B:
   svar0_1 = new int[18];
   svar0_1[0] = 608135816;
   svar0_1[1] = -2052912941;
   svar0_1[2] = 320440878;
   svar0_1[3] = 57701188;
   svar0_1[4] = -1542899678;
   svar0_1[5] = 698298832;
   svar0_1[6] = 137296536;
   svar0_1[7] = -330404727;
   svar0_1[8] = 1160258022;
   svar0_1[9] = 953160567;
   svar0_1[10] = -1101764913;
   svar0_1[11] = 887688300;
   svar0_1[12] = -1062458953;
   svar0_1[13] = -914599715;
   svar0_1[14] = 1065670069;
   svar0_1[15] = -1253635817;
   svar0_1[16] = -1843997223;
   svar0_1[17] = -1988494565;
   dev.sim0n.evaluator.util.crypto.Blowfish$BlowfishECB.pbox_init = svar0_1;
   svar0_3 = new int[256];
   svar0_3[0] = -785314906;
   svar0_3[1] = -1730169428;
   svar0_3[2] = 805139163;
   svar0_3[3] = -803545161;
   svar0_3[4] = -1193168915;
   svar0_3[5] = 1780907670;
   svar0_3[6] = -1166241723;
   svar0_3[7] = -248741991;
   svar0_3[8] = 614570311;
   svar0_3[9] = -1282315017;
   svar0_3[10] = 134345442;
   svar0_3[11] = -2054226922;
   svar0_3[12] = 1667834072;
   svar0_3[13] = 1901547113;
   svar0_3[14] = -1537671517;
   svar0_3[15] = -191677058;
   svar0_3[16] = 227898511;
   svar0_3[17] = 1921955416;
   svar0_3[18] = 1904987480;
   svar0_3[19] = -2112533778;
   svar0_3[20] = 2069144605;
   svar0_3[21] = -1034266187;
   svar0_3[22] = -1674521287;
   svar0_3[23] = 720527379;
   svar0_3[24] = -976113629;
   svar0_3[25] = 677414384;
   svar0_3[26] = -901678824;
   svar0_3[27] = -1193592593;
   svar0_3[28] = -1904616272;
   svar0_3[29] = 1614419982;
   svar0_3[30] = 1822297739;
   svar0_3[31] = -1340175810;
   svar0_3[32] = -686458943;
   svar0_3[33] = -1120842969;
   svar0_3[34] = 2024746970;
   svar0_3[35] = 1432378464;
   svar0_3[36] = -430627341;
   svar0_3[37] = -1437226092;
   svar0_3[38] = 1464375394;
   svar0_3[39] = 1676153920;
   svar0_3[40] = 1439316330;
   svar0_3[41] = 715854006;
   svar0_3[42] = -1261675468;
   svar0_3[43] = 289532110;
   svar0_3[44] = -1588296017;
   svar0_3[45] = 2087905683;
   svar0_3[46] = -1276242927;
   svar0_3[47] = 1668267050;
   svar0_3[48] = 732546397;
   svar0_3[49] = 1947742710;
   svar0_3[50] = -832815594;
   svar0_3[51] = -1685613794;
   svar0_3[52] = -1344882125;
   svar0_3[53] = 1814351708;
   svar0_3[54] = 2050118529;
   svar0_3[55] = 680887927;
   svar0_3[56] = 999245976;
   svar0_3[57] = 1800124847;
   svar0_3[58] = -994056165;
   svar0_3[59] = 1713906067;
   svar0_3[60] = 1641548236;
   svar0_3[61] = -81679983;
   svar0_3[62] = 1216130144;
   svar0_3[63] = 1575780402;
   svar0_3[64] = -276538019;
   svar0_3[65] = -377129551;
   svar0_3[66] = -601480446;
   svar0_3[67] = -345695352;
   svar0_3[68] = 596196993;
   svar0_3[69] = -745100091;
   svar0_3[70] = 258830323;
   svar0_3[71] = -2081144263;
   svar0_3[72] = 772490370;
   svar0_3[73] = -1534844924;
   svar0_3[74] = 1774776394;
   svar0_3[75] = -1642095778;
   svar0_3[76] = 566650946;
   svar0_3[77] = -152474470;
   svar0_3[78] = 1728879713;
   svar0_3[79] = -1412200208;
   svar0_3[80] = 1783734482;
   svar0_3[81] = -665571480;
   svar0_3[82] = -1777359064;
   svar0_3[83] = -1420741725;
   svar0_3[84] = 1861159788;
   svar0_3[85] = 326777828;
   svar0_3[86] = -1170476976;
   svar0_3[87] = 2130389656;
   svar0_3[88] = -1578015459;
   svar0_3[89] = 967770486;
   svar0_3[90] = 1724537150;
   svar0_3[91] = -2109534584;
   svar0_3[92] = -1930525159;
   svar0_3[93] = 1164943284;
   svar0_3[94] = 2105845187;
   svar0_3[95] = 998989502;
   svar0_3[96] = -529566248;
   svar0_3[97] = -2050940813;
   svar0_3[98] = 1075463327;
   svar0_3[99] = 1455516326;
   svar0_3[100] = 1322494562;
   svar0_3[101] = 910128902;
   svar0_3[102] = 469688178;
   svar0_3[103] = 1117454909;
   svar0_3[104] = 936433444;
   svar0_3[105] = -804646328;
   svar0_3[106] = -619713837;
   svar0_3[107] = 1240580251;
   svar0_3[108] = 122909385;
   svar0_3[109] = -2137449605;
   svar0_3[110] = 634681816;
   svar0_3[111] = -152510729;
   svar0_3[112] = -469872614;
   svar0_3[113] = -1233564613;
   svar0_3[114] = -1754472259;
   svar0_3[115] = 79693498;
   svar0_3[116] = -1045868618;
   svar0_3[117] = 1084186820;
   svar0_3[118] = 1583128258;
   svar0_3[119] = 426386531;
   svar0_3[120] = 1761308591;
   svar0_3[121] = 1047286709;
   svar0_3[122] = 322548459;
   svar0_3[123] = 995290223;
   svar0_3[124] = 1845252383;
   svar0_3[125] = -1691314900;
   svar0_3[126] = -863943356;
   svar0_3[127] = -1352745719;
   svar0_3[128] = -1092366332;
   svar0_3[129] = -567063811;
   svar0_3[130] = 1712269319;
   svar0_3[131] = 422464435;
   svar0_3[132] = -1060394921;
   svar0_3[133] = 1170764815;
   svar0_3[134] = -771006663;
   svar0_3[135] = -1177289765;
   svar0_3[136] = 1434042557;
   svar0_3[137] = 442511882;
   svar0_3[138] = -694091578;
   svar0_3[139] = 1076654713;
   svar0_3[140] = 1738483198;
   svar0_3[141] = -81812532;
   svar0_3[142] = -1901729288;
   svar0_3[143] = -617471240;
   svar0_3[144] = 1014306527;
   svar0_3[145] = -43947243;
   svar0_3[146] = 793779912;
   svar0_3[147] = -1392160085;
   svar0_3[148] = 842905082;
   svar0_3[149] = -48003232;
   svar0_3[150] = 1395751752;
   svar0_3[151] = 1040244610;
   svar0_3[152] = -1638115397;
   svar0_3[153] = -898659168;
   svar0_3[154] = 445077038;
   svar0_3[155] = -552113701;
   svar0_3[156] = -717051658;
   svar0_3[157] = 679411651;
   svar0_3[158] = -1402522938;
   svar0_3[159] = -1940957837;
   svar0_3[160] = 1767581616;
   svar0_3[161] = -1144366904;
   svar0_3[162] = -503340195;
   svar0_3[163] = -1192226400;
   svar0_3[164] = 284835224;
   svar0_3[165] = -48135240;
   svar0_3[166] = 1258075500;
   svar0_3[167] = 768725851;
   svar0_3[168] = -1705778055;
   svar0_3[169] = -1225243291;
   svar0_3[170] = -762426948;
   svar0_3[171] = 1274779536;
   svar0_3[172] = -505548070;
   svar0_3[173] = -1530167757;
   svar0_3[174] = 1660621633;
   svar0_3[175] = -823867672;
   svar0_3[176] = -283063590;
   svar0_3[177] = 913787905;
   svar0_3[178] = -797008130;
   svar0_3[179] = 737222580;
   svar0_3[180] = -1780753843;
   svar0_3[181] = -1366257256;
   svar0_3[182] = -357724559;
   svar0_3[183] = 1804850592;
   svar0_3[184] = -795946544;
   svar0_3[185] = -1345903136;
   svar0_3[186] = -1908647121;
   svar0_3[187] = -1904896841;
   svar0_3[188] = -1879645445;
   svar0_3[189] = -233690268;
   svar0_3[190] = -2004305902;
   svar0_3[191] = -1878134756;
   svar0_3[192] = 1336762016;
   svar0_3[193] = 1754252060;
   svar0_3[194] = -774901359;
   svar0_3[195] = -1280786003;
   svar0_3[196] = 791618072;
   svar0_3[197] = -1106372745;
   svar0_3[198] = -361419266;
   svar0_3[199] = -1962795103;
   svar0_3[200] = -442446833;
   svar0_3[201] = -1250986776;
   svar0_3[202] = 413987798;
   svar0_3[203] = -829824359;
   svar0_3[204] = -1264037920;
   svar0_3[205] = -49028937;
   svar0_3[206] = 2093235073;
   svar0_3[207] = -760370983;
   svar0_3[208] = 375366246;
   svar0_3[209] = -2137688315;
   svar0_3[210] = -1815317740;
   svar0_3[211] = 555357303;
   svar0_3[212] = -424861595;
   svar0_3[213] = 2008414854;
   svar0_3[214] = -950779147;
   svar0_3[215] = -73583153;
   svar0_3[216] = -338841844;
   svar0_3[217] = 2067696032;
   svar0_3[218] = -700376109;
   svar0_3[219] = -1373733303;
   svar0_3[220] = 2428461;
   svar0_3[221] = 544322398;
   svar0_3[222] = 577241275;
   svar0_3[223] = 1471733935;
   svar0_3[224] = 610547355;
   svar0_3[225] = -267798242;
   svar0_3[226] = 1432588573;
   svar0_3[227] = 1507829418;
   svar0_3[228] = 2025931657;
   svar0_3[229] = -648391809;
   svar0_3[230] = 545086370;
   svar0_3[231] = 48609733;
   svar0_3[232] = -2094660746;
   svar0_3[233] = 1653985193;
   svar0_3[234] = 298326376;
   svar0_3[235] = 1316178497;
   svar0_3[236] = -1287180854;
   svar0_3[237] = 2064951626;
   svar0_3[238] = 458293330;
   svar0_3[239] = -1705826027;
   svar0_3[240] = -703637697;
   svar0_3[241] = -1130641692;
   svar0_3[242] = 727753846;
   svar0_3[243] = -2115603456;
   svar0_3[244] = 146436021;
   svar0_3[245] = 1461446943;
   svar0_3[246] = -224990101;
   svar0_3[247] = 705550613;
   svar0_3[248] = -1235000031;
   svar0_3[249] = -407242314;
   svar0_3[250] = -13368018;
   svar0_3[251] = -981117340;
   svar0_3[252] = 1404054877;
   svar0_3[253] = -1449160799;
   svar0_3[254] = 146425753;
   svar0_3[255] = 1854211946;
   dev.sim0n.evaluator.util.crypto.Blowfish$BlowfishECB.sbox_init_1 = svar0_3;
   svar0_5 = new int[256];
   svar0_5[0] = 1266315497;
   svar0_5[1] = -1246549692;
   svar0_5[2] = -613086930;
   svar0_5[3] = -1004984797;
   svar0_5[4] = -1385257296;
   svar0_5[5] = 1235738493;
   svar0_5[6] = -1662099272;
   svar0_5[7] = -1880247706;
   svar0_5[8] = -324367247;
   svar0_5[9] = 1771706367;
   svar0_5[10] = 1449415276;
   svar0_5[11] = -1028546847;
   svar0_5[12] = 422970021;
   svar0_5[13] = 1963543593;
   svar0_5[14] = -1604775104;
   svar0_5[15] = -468174274;
   svar0_5[16] = 1062508698;
   svar0_5[17] = 1531092325;
   svar0_5[18] = 1804592342;
   svar0_5[19] = -1711849514;
   svar0_5[20] = -1580033017;
   svar0_5[21] = -269995787;
   svar0_5[22] = 1294809318;
   svar0_5[23] = -265986623;
   svar0_5[24] = 1289560198;
   svar0_5[25] = -2072974554;
   svar0_5[26] = 1669523910;
   svar0_5[27] = 35572830;
   svar0_5[28] = 157838143;
   svar0_5[29] = 1052438473;
   svar0_5[30] = 1016535060;
   svar0_5[31] = 1802137761;
   svar0_5[32] = 1753167236;
   svar0_5[33] = 1386275462;
   svar0_5[34] = -1214491899;
   svar0_5[35] = -1437595849;
   svar0_5[36] = 1040679964;
   svar0_5[37] = 2145300060;
   svar0_5[38] = -1904392980;
   svar0_5[39] = 1461121720;
   svar0_5[40] = -1338320329;
   svar0_5[41] = -263189491;
   svar0_5[42] = -266592508;
   svar0_5[43] = 33600511;
   svar0_5[44] = -1374882534;
   svar0_5[45] = 1018524850;
   svar0_5[46] = 629373528;
   svar0_5[47] = -603381315;
   svar0_5[48] = -779021319;
   svar0_5[49] = 2091462646;
   svar0_5[50] = -1808644237;
   svar0_5[51] = 586499841;
   svar0_5[52] = 988145025;
   svar0_5[53] = 935516892;
   svar0_5[54] = -927631820;
   svar0_5[55] = -1695294041;
   svar0_5[56] = -1455136442;
   svar0_5[57] = 265290510;
   svar0_5[58] = -322386114;
   svar0_5[59] = -1535828415;
   svar0_5[60] = -499593831;
   svar0_5[61] = 1005194799;
   svar0_5[62] = 847297441;
   svar0_5[63] = 406762289;
   svar0_5[64] = 1314163512;
   svar0_5[65] = 1332590856;
   svar0_5[66] = 1866599683;
   svar0_5[67] = -167115585;
   svar0_5[68] = 750260880;
   svar0_5[69] = 613907577;
   svar0_5[70] = 1450815602;
   svar0_5[71] = -1129346641;
   svar0_5[72] = -560302305;
   svar0_5[73] = -644675568;
   svar0_5[74] = -1282691566;
   svar0_5[75] = -590397650;
   svar0_5[76] = 1427272223;
   svar0_5[77] = 778793252;
   svar0_5[78] = 1343938022;
   svar0_5[79] = -1618686585;
   svar0_5[80] = 2052605720;
   svar0_5[81] = 1946737175;
   svar0_5[82] = -1130390852;
   svar0_5[83] = -380928628;
   svar0_5[84] = -327488454;
   svar0_5[85] = -612033030;
   svar0_5[86] = 1661551462;
   svar0_5[87] = -1000029230;
   svar0_5[88] = -283371449;
   svar0_5[89] = 840292616;
   svar0_5[90] = -582796489;
   svar0_5[91] = 616741398;
   svar0_5[92] = 312560963;
   svar0_5[93] = 711312465;
   svar0_5[94] = 1351876610;
   svar0_5[95] = 322626781;
   svar0_5[96] = 1910503582;
   svar0_5[97] = 271666773;
   svar0_5[98] = -2119403562;
   svar0_5[99] = 1594956187;
   svar0_5[100] = 70604529;
   svar0_5[101] = -677132437;
   svar0_5[102] = 1007753275;
   svar0_5[103] = 1495573769;
   svar0_5[104] = -225450259;
   svar0_5[105] = -1745748998;
   svar0_5[106] = -1631928532;
   svar0_5[107] = 504708206;
   svar0_5[108] = -2031925904;
   svar0_5[109] = -353800271;
   svar0_5[110] = -2045878774;
   svar0_5[111] = 1514023603;
   svar0_5[112] = 1998579484;
   svar0_5[113] = 1312622330;
   svar0_5[114] = 694541497;
   svar0_5[115] = -1712906993;
   svar0_5[116] = -2143385130;
   svar0_5[117] = 1382467621;
   svar0_5[118] = 776784248;
   svar0_5[119] = -1676627094;
   svar0_5[120] = -971698502;
   svar0_5[121] = -1797068168;
   svar0_5[122] = -1510196141;
   svar0_5[123] = 503983604;
   svar0_5[124] = -218673497;
   svar0_5[125] = 907881277;
   svar0_5[126] = 423175695;
   svar0_5[127] = 432175456;
   svar0_5[128] = 1378068232;
   svar0_5[129] = -149744970;
   svar0_5[130] = -340918674;
   svar0_5[131] = -356311194;
   svar0_5[132] = -474200683;
   svar0_5[133] = -1501837181;
   svar0_5[134] = -1317062703;
   svar0_5[135] = 26017576;
   svar0_5[136] = -1020076561;
   svar0_5[137] = -1100195163;
   svar0_5[138] = 1700274565;
   svar0_5[139] = 1756076034;
   svar0_5[140] = -288447217;
   svar0_5[141] = -617638597;
   svar0_5[142] = 720338349;
   svar0_5[143] = 1533947780;
   svar0_5[144] = 354530856;
   svar0_5[145] = 688349552;
   svar0_5[146] = -321042571;
   svar0_5[147] = 1637815568;
   svar0_5[148] = 332179504;
   svar0_5[149] = -345916010;
   svar0_5[150] = 53804574;
   svar0_5[151] = -1442618417;
   svar0_5[152] = -1250730864;
   svar0_5[153] = 1282449977;
   svar0_5[154] = -711025141;
   svar0_5[155] = -877994476;
   svar0_5[156] = -288586052;
   svar0_5[157] = 1617046695;
   svar0_5[158] = -1666491221;
   svar0_5[159] = -1292663698;
   svar0_5[160] = 1686838959;
   svar0_5[161] = 431878346;
   svar0_5[162] = -1608291911;
   svar0_5[163] = 1700445008;
   svar0_5[164] = 1080580658;
   svar0_5[165] = 1009431731;
   svar0_5[166] = 832498133;
   svar0_5[167] = -1071531785;
   svar0_5[168] = -1688990951;
   svar0_5[169] = -2023776103;
   svar0_5[170] = -1778935426;
   svar0_5[171] = 1648197032;
   svar0_5[172] = -130578278;
   svar0_5[173] = -1746719369;
   svar0_5[174] = 300782431;
   svar0_5[175] = 375919233;
   svar0_5[176] = 238389289;
   svar0_5[177] = -941219882;
   svar0_5[178] = -1763778655;
   svar0_5[179] = 2019080857;
   svar0_5[180] = 1475708069;
   svar0_5[181] = 455242339;
   svar0_5[182] = -1685863425;
   svar0_5[183] = 448939670;
   svar0_5[184] = -843904277;
   svar0_5[185] = 1395535956;
   svar0_5[186] = -1881585436;
   svar0_5[187] = 1841049896;
   svar0_5[188] = 1491858159;
   svar0_5[189] = 885456874;
   svar0_5[190] = -30872223;
   svar0_5[191] = -293847949;
   svar0_5[192] = 1565136089;
   svar0_5[193] = -396052509;
   svar0_5[194] = 1108368660;
   svar0_5[195] = 540939232;
   svar0_5[196] = 1173283510;
   svar0_5[197] = -1549095958;
   svar0_5[198] = -613658859;
   svar0_5[199] = -87339056;
   svar0_5[200] = -951913406;
   svar0_5[201] = -278217803;
   svar0_5[202] = 1699691293;
   svar0_5[203] = 1103962373;
   svar0_5[204] = -669091426;
   svar0_5[205] = -2038084153;
   svar0_5[206] = -464828566;
   svar0_5[207] = 1031889488;
   svar0_5[208] = -815619598;
   svar0_5[209] = 1535977030;
   svar0_5[210] = -58162272;
   svar0_5[211] = -1043876189;
   svar0_5[212] = 2132092099;
   svar0_5[213] = 1774941330;
   svar0_5[214] = 1199868427;
   svar0_5[215] = 1452454533;
   svar0_5[216] = 157007616;
   svar0_5[217] = -1390851939;
   svar0_5[218] = 342012276;
   svar0_5[219] = 595725824;
   svar0_5[220] = 1480756522;
   svar0_5[221] = 206960106;
   svar0_5[222] = 497939518;
   svar0_5[223] = 591360097;
   svar0_5[224] = 863170706;
   svar0_5[225] = -1919713727;
   svar0_5[226] = -698356495;
   svar0_5[227] = 1814182875;
   svar0_5[228] = 2094937945;
   svar0_5[229] = -873565088;
   svar0_5[230] = 1082520231;
   svar0_5[231] = -831049106;
   svar0_5[232] = -1509457788;
   svar0_5[233] = 435703966;
   svar0_5[234] = -386934699;
   svar0_5[235] = 1641649973;
   svar0_5[236] = -1452693590;
   svar0_5[237] = -989067582;
   svar0_5[238] = 1510255612;
   svar0_5[239] = -2146710820;
   svar0_5[240] = -1639679442;
   svar0_5[241] = -1018874748;
   svar0_5[242] = -36346107;
   svar0_5[243] = 236887753;
   svar0_5[244] = -613164077;
   svar0_5[245] = 274041037;
   svar0_5[246] = 1734335097;
   svar0_5[247] = -479771840;
   svar0_5[248] = -976997275;
   svar0_5[249] = 1899903192;
   svar0_5[250] = 1026095262;
   svar0_5[251] = -244449504;
   svar0_5[252] = 356393447;
   svar0_5[253] = -1884275382;
   svar0_5[254] = -421290197;
   svar0_5[255] = -612127241;
   dev.sim0n.evaluator.util.crypto.Blowfish$BlowfishECB.sbox_init_2 = svar0_5;
   svar0_7 = new int[256];
   svar0_7[0] = -381855128;
   svar0_7[1] = -1803468553;
   svar0_7[2] = -162781668;
   svar0_7[3] = -1805047500;
   svar0_7[4] = 1091903735;
   svar0_7[5] = 1979897079;
   svar0_7[6] = -1124832466;
   svar0_7[7] = -727580568;
   svar0_7[8] = -737663887;
   svar0_7[9] = 857797738;
   svar0_7[10] = 1136121015;
   svar0_7[11] = 1342202287;
   svar0_7[12] = 507115054;
   svar0_7[13] = -1759230650;
   svar0_7[14] = 337727348;
   svar0_7[15] = -1081374656;
   svar0_7[16] = 1301675037;
   svar0_7[17] = -1766485585;
   svar0_7[18] = 1895095763;
   svar0_7[19] = 1721773893;
   svar0_7[20] = -1078195732;
   svar0_7[21] = 62756741;
   svar0_7[22] = 2142006736;
   svar0_7[23] = 835421444;
   svar0_7[24] = -1762973773;
   svar0_7[25] = 1442658625;
   svar0_7[26] = -635090970;
   svar0_7[27] = -1412822374;
   svar0_7[28] = 676362277;
   svar0_7[29] = 1392781812;
   svar0_7[30] = 170690266;
   svar0_7[31] = -373920261;
   svar0_7[32] = 1759253602;
   svar0_7[33] = -683120384;
   svar0_7[34] = 1745797284;
   svar0_7[35] = 664899054;
   svar0_7[36] = 1329594018;
   svar0_7[37] = -393761396;
   svar0_7[38] = -1249058810;
   svar0_7[39] = 2062866102;
   svar0_7[40] = -1429332356;
   svar0_7[41] = -751345684;
   svar0_7[42] = -830954599;
   svar0_7[43] = 1080764994;
   svar0_7[44] = 553557557;
   svar0_7[45] = -638351943;
   svar0_7[46] = -298199125;
   svar0_7[47] = 991055499;
   svar0_7[48] = 499776247;
   svar0_7[49] = 1265440854;
   svar0_7[50] = 648242737;
   svar0_7[51] = -354183246;
   svar0_7[52] = 980351604;
   svar0_7[53] = -581221582;
   svar0_7[54] = 1749149687;
   svar0_7[55] = -898096901;
   svar0_7[56] = -83167922;
   svar0_7[57] = -654396521;
   svar0_7[58] = 1161844396;
   svar0_7[59] = -1169648345;
   svar0_7[60] = 1431517754;
   svar0_7[61] = 545492359;
   svar0_7[62] = -26498633;
   svar0_7[63] = -795437749;
   svar0_7[64] = 1437099964;
   svar0_7[65] = -1592419752;
   svar0_7[66] = -861329053;
   svar0_7[67] = -1713251533;
   svar0_7[68] = -1507177898;
   svar0_7[69] = 1060185593;
   svar0_7[70] = 1593081372;
   svar0_7[71] = -1876348548;
   svar0_7[72] = -34019326;
   svar0_7[73] = 69676912;
   svar0_7[74] = -2135222948;
   svar0_7[75] = 86519011;
   svar0_7[76] = -1782508216;
   svar0_7[77] = -456757982;
   svar0_7[78] = 1220612927;
   svar0_7[79] = -955283748;
   svar0_7[80] = 133810670;
   svar0_7[81] = 1090789135;
   svar0_7[82] = 1078426020;
   svar0_7[83] = 1569222167;
   svar0_7[84] = 845107691;
   svar0_7[85] = -711212847;
   svar0_7[86] = -222510705;
   svar0_7[87] = 1091646820;
   svar0_7[88] = 628848692;
   svar0_7[89] = 1613405280;
   svar0_7[90] = -537335645;
   svar0_7[91] = 526609435;
   svar0_7[92] = 236106946;
   svar0_7[93] = 48312990;
   svar0_7[94] = -1352249391;
   svar0_7[95] = -892239595;
   svar0_7[96] = 1797494240;
   svar0_7[97] = 859738849;
   svar0_7[98] = 992217954;
   svar0_7[99] = -289490654;
   svar0_7[100] = -2051890674;
   svar0_7[101] = -424014439;
   svar0_7[102] = -562951028;
   svar0_7[103] = 765654824;
   svar0_7[104] = -804095931;
   svar0_7[105] = -1783130883;
   svar0_7[106] = 1685915746;
   svar0_7[107] = -405998096;
   svar0_7[108] = 1414112111;
   svar0_7[109] = -2021832454;
   svar0_7[110] = -1013056217;
   svar0_7[111] = -214004450;
   svar0_7[112] = 172450625;
   svar0_7[113] = -1724973196;
   svar0_7[114] = 980381355;
   svar0_7[115] = -185008841;
   svar0_7[116] = -1475158944;
   svar0_7[117] = -1578377736;
   svar0_7[118] = -1726226100;
   svar0_7[119] = -613520627;
   svar0_7[120] = -964995824;
   svar0_7[121] = 1835478071;
   svar0_7[122] = 660984891;
   svar0_7[123] = -590288892;
   svar0_7[124] = -248967737;
   svar0_7[125] = -872349789;
   svar0_7[126] = -1254551662;
   svar0_7[127] = 1762651403;
   svar0_7[128] = 1719377915;
   svar0_7[129] = -824476260;
   svar0_7[130] = -1601057013;
   svar0_7[131] = -652910941;
   svar0_7[132] = -1156370552;
   svar0_7[133] = 1364962596;
   svar0_7[134] = 2073328063;
   svar0_7[135] = 1983633131;
   svar0_7[136] = 926494387;
   svar0_7[137] = -871278215;
   svar0_7[138] = -2144935273;
   svar0_7[139] = -198299347;
   svar0_7[140] = 1749200295;
   svar0_7[141] = -966120645;
   svar0_7[142] = 309677260;
   svar0_7[143] = 2016342300;
   svar0_7[144] = 1779581495;
   svar0_7[145] = -1215147545;
   svar0_7[146] = 111262694;
   svar0_7[147] = 1274766160;
   svar0_7[148] = 443224088;
   svar0_7[149] = 298511866;
   svar0_7[150] = 1025883608;
   svar0_7[151] = -488520759;
   svar0_7[152] = 1145181785;
   svar0_7[153] = 168956806;
   svar0_7[154] = -653464466;
   svar0_7[155] = -710153686;
   svar0_7[156] = 1689216846;
   svar0_7[157] = -628709281;
   svar0_7[158] = -1094719096;
   svar0_7[159] = 1692713982;
   svar0_7[160] = -1648590761;
   svar0_7[161] = -252198778;
   svar0_7[162] = 1618508792;
   svar0_7[163] = 1610833997;
   svar0_7[164] = -771914938;
   svar0_7[165] = -164094032;
   svar0_7[166] = 2001055236;
   svar0_7[167] = -684262196;
   svar0_7[168] = -2092799181;
   svar0_7[169] = -266425487;
   svar0_7[170] = -1333771897;
   svar0_7[171] = 1006657119;
   svar0_7[172] = 2006996926;
   svar0_7[173] = -1108824540;
   svar0_7[174] = 1430667929;
   svar0_7[175] = -1084739999;
   svar0_7[176] = 1314452623;
   svar0_7[177] = -220332638;
   svar0_7[178] = -193663176;
   svar0_7[179] = -2021016126;
   svar0_7[180] = 1399257539;
   svar0_7[181] = -927756684;
   svar0_7[182] = -1267338667;
   svar0_7[183] = 1190975929;
   svar0_7[184] = 2062231137;
   svar0_7[185] = -1960976508;
   svar0_7[186] = -2073424263;
   svar0_7[187] = -1856006686;
   svar0_7[188] = 1181637006;
   svar0_7[189] = 548689776;
   svar0_7[190] = -1932175983;
   svar0_7[191] = -922558900;
   svar0_7[192] = -1190417183;
   svar0_7[193] = -1149106736;
   svar0_7[194] = 296247880;
   svar0_7[195] = 1970579870;
   svar0_7[196] = -1216407114;
   svar0_7[197] = -525738999;
   svar0_7[198] = 1714227617;
   svar0_7[199] = -1003338189;
   svar0_7[200] = -396747006;
   svar0_7[201] = 166772364;
   svar0_7[202] = 1251581989;
   svar0_7[203] = 493813264;
   svar0_7[204] = 448347421;
   svar0_7[205] = 195405023;
   svar0_7[206] = -1584991729;
   svar0_7[207] = 677966185;
   svar0_7[208] = -591930749;
   svar0_7[209] = 1463355134;
   svar0_7[210] = -1578971493;
   svar0_7[211] = 1338867538;
   svar0_7[212] = 1343315457;
   svar0_7[213] = -1492745222;
   svar0_7[214] = -1610435132;
   svar0_7[215] = 233230375;
   svar0_7[216] = -1694987225;
   svar0_7[217] = 2000651841;
   svar0_7[218] = -1017099258;
   svar0_7[219] = 1638401717;
   svar0_7[220] = -266896856;
   svar0_7[221] = -1057650976;
   svar0_7[222] = 6314154;
   svar0_7[223] = 819756386;
   svar0_7[224] = 300326615;
   svar0_7[225] = 590932579;
   svar0_7[226] = 1405279636;
   svar0_7[227] = -1027467724;
   svar0_7[228] = -1144263082;
   svar0_7[229] = -1866680610;
   svar0_7[230] = -335774303;
   svar0_7[231] = -833020554;
   svar0_7[232] = 1862657033;
   svar0_7[233] = 1266418056;
   svar0_7[234] = 963775037;
   svar0_7[235] = 2089974820;
   svar0_7[236] = -2031914401;
   svar0_7[237] = 1917689273;
   svar0_7[238] = 448879540;
   svar0_7[239] = -744572676;
   svar0_7[240] = -313240200;
   svar0_7[241] = 150775221;
   svar0_7[242] = -667058989;
   svar0_7[243] = 1303187396;
   svar0_7[244] = 508620638;
   svar0_7[245] = -1318983944;
   svar0_7[246] = -1568336679;
   svar0_7[247] = 1817252668;
   svar0_7[248] = 1876281319;
   svar0_7[249] = 1457606340;
   svar0_7[250] = 908771278;
   svar0_7[251] = -574175177;
   svar0_7[252] = -677760460;
   svar0_7[253] = -1838972398;
   svar0_7[254] = 1729034894;
   svar0_7[255] = 1080033504;
   dev.sim0n.evaluator.util.crypto.Blowfish$BlowfishECB.sbox_init_3 = svar0_7;
   svar0_9 = new int[256];
   svar0_9[0] = 976866871;
   svar0_9[1] = -738527793;
   svar0_9[2] = -1413318857;
   svar0_9[3] = 1522871579;
   svar0_9[4] = 1555064734;
   svar0_9[5] = 1336096578;
   svar0_9[6] = -746444992;
   svar0_9[7] = -1715692610;
   svar0_9[8] = -720269667;
   svar0_9[9] = -1089506539;
   svar0_9[10] = -701686658;
   svar0_9[11] = -956251013;
   svar0_9[12] = -1215554709;
   svar0_9[13] = 564236357;
   svar0_9[14] = -1301368386;
   svar0_9[15] = 1781952180;
   svar0_9[16] = 1464380207;
   svar0_9[17] = -1131123079;
   svar0_9[18] = -962365742;
   svar0_9[19] = 1699332808;
   svar0_9[20] = 1393555694;
   svar0_9[21] = 1183702653;
   svar0_9[22] = -713881059;
   svar0_9[23] = 1288719814;
   svar0_9[24] = 691649499;
   svar0_9[25] = -1447410096;
   svar0_9[26] = -1399511320;
   svar0_9[27] = -1101077756;
   svar0_9[28] = -1577396752;
   svar0_9[29] = 1781354906;
   svar0_9[30] = 1676643554;
   svar0_9[31] = -1702433246;
   svar0_9[32] = -1064713544;
   svar0_9[33] = 1126444790;
   svar0_9[34] = -1524759638;
   svar0_9[35] = -1661808476;
   svar0_9[36] = -2084544070;
   svar0_9[37] = -1679201715;
   svar0_9[38] = -1880812208;
   svar0_9[39] = -1167828010;
   svar0_9[40] = 673620729;
   svar0_9[41] = -1489356063;
   svar0_9[42] = 1269405062;
   svar0_9[43] = -279616791;
   svar0_9[44] = -953159725;
   svar0_9[45] = -145557542;
   svar0_9[46] = 1057255273;
   svar0_9[47] = 2012875353;
   svar0_9[48] = -2132498155;
   svar0_9[49] = -2018474495;
   svar0_9[50] = -1693849939;
   svar0_9[51] = 993977747;
   svar0_9[52] = -376373926;
   svar0_9[53] = -1640704105;
   svar0_9[54] = 753973209;
   svar0_9[55] = 36408145;
   svar0_9[56] = -1764381638;
   svar0_9[57] = 25011837;
   svar0_9[58] = -774947114;
   svar0_9[59] = 2088578344;
   svar0_9[60] = 530523599;
   svar0_9[61] = -1376601957;
   svar0_9[62] = 1524020338;
   svar0_9[63] = 1518925132;
   svar0_9[64] = -534139791;
   svar0_9[65] = -535190042;
   svar0_9[66] = 1202760957;
   svar0_9[67] = -309069157;
   svar0_9[68] = -388774771;
   svar0_9[69] = 674977740;
   svar0_9[70] = -120232407;
   svar0_9[71] = 2031300136;
   svar0_9[72] = 2019492241;
   svar0_9[73] = -311074731;
   svar0_9[74] = -141160892;
   svar0_9[75] = -472686964;
   svar0_9[76] = 352677332;
   svar0_9[77] = -1997247046;
   svar0_9[78] = 60907813;
   svar0_9[79] = 90501309;
   svar0_9[80] = -1007968747;
   svar0_9[81] = 1016092578;
   svar0_9[82] = -1759044884;
   svar0_9[83] = -1455814870;
   svar0_9[84] = 457141659;
   svar0_9[85] = 509813237;
   svar0_9[86] = -174299397;
   svar0_9[87] = 652014361;
   svar0_9[88] = 1966332200;
   svar0_9[89] = -1319764491;
   svar0_9[90] = 55981186;
   svar0_9[91] = -1967506245;
   svar0_9[92] = 676427537;
   svar0_9[93] = -1039476232;
   svar0_9[94] = -1412673177;
   svar0_9[95] = -861040033;
   svar0_9[96] = 1307055953;
   svar0_9[97] = 942726286;
   svar0_9[98] = 933058658;
   svar0_9[99] = -1826555503;
   svar0_9[100] = -361066302;
   svar0_9[101] = -79791154;
   svar0_9[102] = 1361170020;
   svar0_9[103] = 2001714738;
   svar0_9[104] = -1464409218;
   svar0_9[105] = -1020707514;
   svar0_9[106] = 1222529897;
   svar0_9[107] = 1679025792;
   svar0_9[108] = -1565652976;
   svar0_9[109] = -580013532;
   svar0_9[110] = 1770335741;
   svar0_9[111] = 151462246;
   svar0_9[112] = -1281735158;
   svar0_9[113] = 1682292957;
   svar0_9[114] = 1483529935;
   svar0_9[115] = 471910574;
   svar0_9[116] = 1539241949;
   svar0_9[117] = 458788160;
   svar0_9[118] = -858652289;
   svar0_9[119] = 1807016891;
   svar0_9[120] = -576558466;
   svar0_9[121] = 978976581;
   svar0_9[122] = 1043663428;
   svar0_9[123] = -1129001515;
   svar0_9[124] = 1927990952;
   svar0_9[125] = -94075717;
   svar0_9[126] = -1922690386;
   svar0_9[127] = -1086558393;
   svar0_9[128] = -761535389;
   svar0_9[129] = 1412390302;
   svar0_9[130] = -1362987237;
   svar0_9[131] = -162634896;
   svar0_9[132] = 1947078029;
   svar0_9[133] = -413461673;
   svar0_9[134] = -126740879;
   svar0_9[135] = -1353482915;
   svar0_9[136] = 1077988104;
   svar0_9[137] = 1320477388;
   svar0_9[138] = 886195818;
   svar0_9[139] = 18198404;
   svar0_9[140] = -508558296;
   svar0_9[141] = -1785185763;
   svar0_9[142] = 112762804;
   svar0_9[143] = -831610808;
   svar0_9[144] = 1866414978;
   svar0_9[145] = 891333506;
   svar0_9[146] = 18488651;
   svar0_9[147] = 661792760;
   svar0_9[148] = 1628790961;
   svar0_9[149] = -409780260;
   svar0_9[150] = -1153795797;
   svar0_9[151] = 876946877;
   svar0_9[152] = -1601685023;
   svar0_9[153] = 1372485963;
   svar0_9[154] = 791857591;
   svar0_9[155] = -1608533303;
   svar0_9[156] = -534984578;
   svar0_9[157] = -1127755274;
   svar0_9[158] = -822013501;
   svar0_9[159] = -1578587449;
   svar0_9[160] = 445679433;
   svar0_9[161] = -732971622;
   svar0_9[162] = -790962485;
   svar0_9[163] = -720709064;
   svar0_9[164] = 54117162;
   svar0_9[165] = -963561881;
   svar0_9[166] = -1913048708;
   svar0_9[167] = -525259953;
   svar0_9[168] = -140617289;
   svar0_9[169] = 1140177722;
   svar0_9[170] = -220915201;
   svar0_9[171] = 668550556;
   svar0_9[172] = -1080614356;
   svar0_9[173] = 367459370;
   svar0_9[174] = 261225585;
   svar0_9[175] = -1684794075;
   svar0_9[176] = -85617823;
   svar0_9[177] = -826893077;
   svar0_9[178] = -1029151655;
   svar0_9[179] = 314222801;
   svar0_9[180] = -1228863650;
   svar0_9[181] = -486184436;
   svar0_9[182] = 282218597;
   svar0_9[183] = -888953790;
   svar0_9[184] = -521376242;
   svar0_9[185] = 379116347;
   svar0_9[186] = 1285071038;
   svar0_9[187] = 846784868;
   svar0_9[188] = -1625320142;
   svar0_9[189] = -523005217;
   svar0_9[190] = -744475605;
   svar0_9[191] = -1989021154;
   svar0_9[192] = 453669953;
   svar0_9[193] = 1268987020;
   svar0_9[194] = -977374944;
   svar0_9[195] = -1015663912;
   svar0_9[196] = -550133875;
   svar0_9[197] = -1684459730;
   svar0_9[198] = -435458233;
   svar0_9[199] = 266596637;
   svar0_9[200] = -447948204;
   svar0_9[201] = 517658769;
   svar0_9[202] = -832407089;
   svar0_9[203] = -851542417;
   svar0_9[204] = 370717030;
   svar0_9[205] = -47440635;
   svar0_9[206] = -2070949179;
   svar0_9[207] = -151313767;
   svar0_9[208] = -182193321;
   svar0_9[209] = -1506642397;
   svar0_9[210] = -1817692879;
   svar0_9[211] = 1456262402;
   svar0_9[212] = -1393524382;
   svar0_9[213] = 1517677493;
   svar0_9[214] = 1846949527;
   svar0_9[215] = -1999473716;
   svar0_9[216] = -560569710;
   svar0_9[217] = -2118563376;
   svar0_9[218] = 1280348187;
   svar0_9[219] = 1908823572;
   svar0_9[220] = -423180355;
   svar0_9[221] = 846861322;
   svar0_9[222] = 1172426758;
   svar0_9[223] = -1007518822;
   svar0_9[224] = -911584259;
   svar0_9[225] = 1655181056;
   svar0_9[226] = -1155153950;
   svar0_9[227] = 901632758;
   svar0_9[228] = 1897031941;
   svar0_9[229] = -1308360158;
   svar0_9[230] = -1228157060;
   svar0_9[231] = -847864789;
   svar0_9[232] = 1393639104;
   svar0_9[233] = 373351379;
   svar0_9[234] = 950779232;
   svar0_9[235] = 625454576;
   svar0_9[236] = -1170726756;
   svar0_9[237] = -146354570;
   svar0_9[238] = 2007998917;
   svar0_9[239] = 544563296;
   svar0_9[240] = -2050228658;
   svar0_9[241] = -1964470824;
   svar0_9[242] = 2058025392;
   svar0_9[243] = 1291430526;
   svar0_9[244] = 424198748;
   svar0_9[245] = 50039436;
   svar0_9[246] = 29584100;
   svar0_9[247] = -689184263;
   svar0_9[248] = -1865090967;
   svar0_9[249] = -1503863136;
   svar0_9[250] = 1057563949;
   svar0_9[251] = -1039604065;
   svar0_9[252] = -1219600078;
   svar0_9[253] = -831004069;
   svar0_9[254] = 1469046755;
   svar0_9[255] = 985887462;
   dev.sim0n.evaluator.util.crypto.Blowfish$BlowfishECB.sbox_init_4 = svar0_9;
   return;
   
BLOCK A:
   

```


## Class: dev/sim0n/evaluator/operation/Operation
Super: java/lang/Enum
Interfaces: []
Access: public final synchronized enum

### Method: values()[Ldev/sim0n/evaluator/operation/Operation;
Access: public static

```ssa
BLOCK B:
   return (dev.sim0n.evaluator.operation.Operation[])dev.sim0n.evaluator.operation.Operation.$VALUES.clone();
   
BLOCK A:
   

```

### Method: valueOf(Ljava/lang/String;)Ldev/sim0n/evaluator/operation/Operation;
Access: public static

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   return (dev.sim0n.evaluator.operation.Operation)java.lang.Enum.valueOf(dev.sim0n.evaluator.operation.Operation.class, lvar0_0);
   

```

### Method: <init>(Ljava/lang/String;I)V
Access: private

```ssa
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0, lvar2_0));
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   

```

### Method: <clinit>()V
Access: static

```ssa
BLOCK A:
   
BLOCK B:
   svar0_0 = new dev.sim0n.evaluator.operation.Operation;
   _consume(svar0_0.<init>("INT", 0));
   dev.sim0n.evaluator.operation.Operation.INT = svar0_0;
   svar0_1 = new dev.sim0n.evaluator.operation.Operation;
   _consume(svar0_1.<init>("DOUBLE", 1));
   dev.sim0n.evaluator.operation.Operation.DOUBLE = svar0_1;
   svar0_3 = new dev.sim0n.evaluator.operation.Operation[2];
   svar0_3[0] = dev.sim0n.evaluator.operation.Operation.INT;
   svar0_3[1] = dev.sim0n.evaluator.operation.Operation.DOUBLE;
   dev.sim0n.evaluator.operation.Operation.$VALUES = svar0_3;
   return;
   

```


## Class: dev/sim0n/evaluator/test/impl/Test2
Super: java/lang/Object
Interfaces: []
Access: public synchronized

### Method: <init>()V
Access: public

```ssa
BLOCK B:
   _consume(lvar0_0.<init>());
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   

```


## Class: dev/sim0n/evaluator/operation/IntMathOperation$1
Super: dev/sim0n/evaluator/operation/IntMathOperation
Interfaces: []
Access: final synchronized enum

### Method: <init>(Ljava/lang/String;ILjava/lang/String;)V
Access: 

```ssa
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0, lvar2_0, lvar3_0, nullconst));
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   

```

### Method: evaluate(II)I
Access: public

```ssa
BLOCK B:
   return {lvar1_0 + lvar2_0};
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   

```


## Class: dev/sim0n/evaluator/operation/IntMathOperation$3
Super: dev/sim0n/evaluator/operation/IntMathOperation
Interfaces: []
Access: final synchronized enum

### Method: <init>(Ljava/lang/String;ILjava/lang/String;)V
Access: 

```ssa
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0, lvar2_0, lvar3_0, nullconst));
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   

```

### Method: evaluate(II)I
Access: public

```ssa
BLOCK B:
   return {lvar1_0 / lvar2_0};
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   

```


## Class: dev/sim0n/evaluator/operation/IntMathOperation$2
Super: dev/sim0n/evaluator/operation/IntMathOperation
Interfaces: []
Access: final synchronized enum

### Method: <init>(Ljava/lang/String;ILjava/lang/String;)V
Access: 

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0, lvar2_0, lvar3_0, nullconst));
   return;
   

```

### Method: evaluate(II)I
Access: public

```ssa
BLOCK B:
   return {lvar1_0 - lvar2_0};
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   

```


## Class: dev/sim0n/evaluator/operation/IntMathOperation$5
Super: dev/sim0n/evaluator/operation/IntMathOperation
Interfaces: []
Access: final synchronized enum

### Method: <init>(Ljava/lang/String;ILjava/lang/String;)V
Access: 

```ssa
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0, lvar2_0, lvar3_0, nullconst));
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   

```

### Method: evaluate(II)I
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   
BLOCK B:
   return {lvar1_0 * lvar2_0};
   

```


## Class: dev/sim0n/evaluator/operation/IntMathOperation$4
Super: dev/sim0n/evaluator/operation/IntMathOperation
Interfaces: []
Access: final synchronized enum

### Method: <init>(Ljava/lang/String;ILjava/lang/String;)V
Access: 

```ssa
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0, lvar2_0, lvar3_0, nullconst));
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   

```

### Method: evaluate(II)I
Access: public

```ssa
BLOCK B:
   return {lvar1_0 % lvar2_0};
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   

```


## Class: dev/sim0n/evaluator/test/impl/annotation/TestAnnotation
Super: java/lang/Object
Interfaces: [java/lang/annotation/Annotation]
Access: public interface abstract annotation

### Method: string()Ljava/lang/String;
Access: public abstract

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   

```

### Method: intValue()I
Access: public abstract

```ssa
BLOCK B:
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   

```

### Method: doubleValue()D
Access: public abstract

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   

```


## Class: dev/sim0n/evaluator/operation/IntMathOperation$6
Super: dev/sim0n/evaluator/operation/IntMathOperation
Interfaces: []
Access: final synchronized enum

### Method: <init>(Ljava/lang/String;ILjava/lang/String;)V
Access: 

```ssa
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0, lvar2_0, lvar3_0, nullconst));
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   

```

### Method: evaluate(II)I
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   
BLOCK B:
   return {lvar1_0 ^ lvar2_0};
   

```


## Class: dev/sim0n/evaluator/util/Log
Super: java/lang/Object
Interfaces: []
Access: public synchronized

### Method: <init>()V
Access: public

```ssa
BLOCK B:
   _consume(lvar0_0.<init>());
   svar1_0 = new java.util.ArrayList;
   _consume(svar1_0.<init>());
   lvar0_0.logs = svar1_0;
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   

```

### Method: exportLog()V
Access: public

```ssa
BLOCK H:
   goto J
   
BLOCK G:
   lvar4_0 = catch();
   _consume(nullconst.addSuppressed(lvar4_0));
   goto J
   
BLOCK M:
   if (lvar2_0 == nullconst)
      goto S
   
BLOCK B:
   lvar1_0 = new java.io.File;
   _consume(lvar1_0.<init>("calculations.txt"));
   lvar2_0 = new java.io.BufferedWriter;
   svar2_1 = new java.io.FileWriter;
   _consume(svar2_1.<init>(lvar1_0));
   _consume(lvar2_0.<init>(svar2_1));
   lvar3_0 = nullconst;
   
BLOCK O:
   _consume(lvar2_0.close());
   
BLOCK R:
   lvar6_0 = catch();
   _consume(lvar3_2.addSuppressed(lvar6_0));
   goto S
   
BLOCK C:
   _consume(lvar0_0.logs.forEach(dynamic_invoke<java.util.function.Consumer>(java.lang.invoke.LambdaMetafactory.metafactory(methodTypeOf((Ljava/lang/Object;)V), handleOf(dev/sim0n/evaluator/util/Log.lambda$exportLog$0(Ljava/io/BufferedWriter;Ljava/lang/String;)V (6)), methodTypeOf((Ljava/lang/String;)V), lvar2_0))));
   _consume(lvar2_0.flush());
   
BLOCK L:
   lvar3_2 = ɸ{C:lvar3_0, L:lvar3_2, K:lvar3_1};
   lvar5_0 = catch();
   
BLOCK S:
   throw lvar5_0;
   
BLOCK J:
   return;
   
BLOCK K:
   lvar4_1 = catch();
   lvar3_1 = lvar4_1;
   throw lvar4_1;
   
BLOCK D:
   if (lvar2_0 == nullconst)
      goto J
   
BLOCK I:
   _consume(lvar2_0.close());
   goto J
   
BLOCK E:
   if (nullconst == nullconst)
      goto I
   
BLOCK Q:
   goto S
   
BLOCK P:
   _consume(lvar2_0.close());
   
BLOCK N:
   if (lvar3_2 == nullconst)
      goto O
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK F:
   _consume(lvar2_0.close());
   

```

### Method: addLog(Ljava/lang/String;)V
Access: public

```ssa
BLOCK B:
   svar0_2 = lvar0_0.logs.add(lvar1_0);
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   

```

### Method: println(Ljava/lang/String;)V
Access: public

```ssa
BLOCK B:
   _consume(lvar0_0.addLog(lvar1_0));
   _consume(java.lang.System.out.println(lvar1_0));
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   

```

### Method: print(Ljava/lang/String;[Ljava/lang/Object;)V
Access: public transient varargs

```ssa
BLOCK B:
   _consume(lvar0_0.addLog(java.lang.String.format(lvar1_0, lvar2_0)));
   svar0_2 = java.lang.System.out.printf(lvar1_0, lvar2_0);
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   

```


## Class: dev/sim0n/evaluator/Main
Super: java/lang/Object
Interfaces: []
Access: public synchronized

### Method: <init>()V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   _consume(lvar0_0.<init>());
   return;
   

```

### Method: main([Ljava/lang/String;)V
Access: public static

```ssa
BLOCK E:
   svar1_78 = ɸ{C:svar1_77, D:svar1_90};
   _consume(svar0_31.println(svar1_78));
   svar0_34 = dev.sim0n.evaluator.Main.LOG;
   if (lvar10_0.equals("hello world 123 1605479835458") == 0)
      goto G
   
BLOCK H:
   svar1_85 = ɸ{F:svar1_84, G:svar1_89};
   _consume(svar0_34.println(svar1_85));
   
BLOCK I:
   _consume(dev.sim0n.evaluator.Main.LOG.exportLog());
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   lvar1_0 = new int[25];
   lvar1_0[0] = 813;
   lvar1_0[1] = 432;
   lvar1_0[2] = 784;
   lvar1_0[3] = 409;
   lvar1_0[4] = 600;
   lvar1_0[5] = 552;
   lvar1_0[6] = 923;
   lvar1_0[7] = 51;
   lvar1_0[8] = 275;
   lvar1_0[9] = 988;
   lvar1_0[10] = 774;
   lvar1_0[11] = 74;
   lvar1_0[12] = 693;
   lvar1_0[13] = 892;
   lvar1_0[14] = 957;
   lvar1_0[15] = 398;
   lvar1_0[16] = 636;
   lvar1_0[17] = 530;
   lvar1_0[18] = 472;
   lvar1_0[19] = 769;
   lvar1_0[20] = 106;
   lvar1_0[21] = 259;
   lvar1_0[22] = 450;
   lvar1_0[23] = 893;
   lvar1_0[24] = 355;
   lvar2_0 = new double[25];
   lvar2_0[0] = 15.354279285687706D;
   lvar2_0[1] = 5.797782664265068D;
   lvar2_0[2] = 8.683696317015794D;
   lvar2_0[3] = 1.9817656768587806D;
   lvar2_0[4] = 3.535287429360438D;
   lvar2_0[5] = 4.220760053178631D;
   lvar2_0[6] = 10.807260410843776D;
   lvar2_0[7] = 9.79012425459241D;
   lvar2_0[8] = 9.862795945665074D;
   lvar2_0[9] = 0.74113233949422D;
   lvar2_0[10] = 2.422188626186955D;
   lvar2_0[11] = 9.624071224255548D;
   lvar2_0[12] = 0.21480131492236743D;
   lvar2_0[13] = 10.736554500849767D;
   lvar2_0[14] = 2.7573095161824757D;
   lvar2_0[15] = 16.295928424685112D;
   lvar2_0[16] = 1.5007304056520934D;
   lvar2_0[17] = 11.312333434915566D;
   lvar2_0[18] = 0.2805255257633217D;
   lvar2_0[19] = 2.158320252411026D;
   lvar2_0[20] = 0.0D;
   lvar2_0[21] = 8.556101546454709D;
   lvar2_0[22] = 1.1028629585647993D;
   lvar2_0[23] = 15.846849796405586D;
   lvar2_0[24] = 5.932633085882487D;
   svar0_4 = dev.sim0n.evaluator.Main.LOG;
   svar2_51 = new java.lang.Object[1];
   svar2_51[0] = java.time.LocalDate.now();
   _consume(svar0_4.println(java.lang.String.format("Today's date is %s", svar2_51)));
   lvar3_0 = dynamic_invoke<java.util.function.Supplier>(java.lang.invoke.LambdaMetafactory.metafactory(methodTypeOf(()Ljava/lang/Object;), handleOf(dev/sim0n/evaluator/Main.lambda$main$0()Ljava/lang/Integer; (6)), methodTypeOf(()Ljava/lang/Integer;)));
   lvar4_0 = dynamic_invoke<java.util.function.Supplier>(java.lang.invoke.LambdaMetafactory.metafactory(methodTypeOf(()Ljava/lang/Object;), handleOf(dev/sim0n/evaluator/Main.lambda$main$1()Ljava/lang/Integer; (6)), methodTypeOf(()Ljava/lang/Integer;)));
   _consume(dev.sim0n.evaluator.Main.LOG.println("Performing small int test..."));
   lvar5_0 = new dev.sim0n.evaluator.util.stats.Calculations;
   _consume(lvar5_0.<init>());
   _consume(((java.util.List)java.util.stream.Stream.generate(dynamic_invoke<java.util.function.Supplier>(java.lang.invoke.LambdaMetafactory.metafactory(methodTypeOf(()Ljava/lang/Object;), handleOf(dev/sim0n/evaluator/Main.lambda$main$3(Ljava/util/function/Supplier;Ldev/sim0n/evaluator/util/stats/Calculations;)Ldev/sim0n/evaluator/util/Evaluation; (6)), methodTypeOf(()Ldev/sim0n/evaluator/util/Evaluation;), lvar3_0, lvar5_0))).limit((long)({5 + ((java.lang.Integer)lvar3_0.get()).intValue()})).collect(java.util.stream.Collectors.toList())).forEach(dynamic_invoke<java.util.function.Consumer>(java.lang.invoke.LambdaMetafactory.metafactory(methodTypeOf((Ljava/lang/Object;)V), handleOf(dev/sim0n/evaluator/Main.lambda$main$4(Ljava/util/function/Supplier;Ldev/sim0n/evaluator/util/Evaluation;)V (6)), methodTypeOf((Ldev/sim0n/evaluator/util/Evaluation;)V), lvar4_0))));
   _consume(dev.sim0n.evaluator.Main.LOG.println("
   Performing random math operations..."));
   _consume(java.util.stream.IntStream.range(0, {5 + dev.sim0n.evaluator.Main.RANDOM.nextInt(20)}).forEach(dynamic_invoke<java.util.function.IntConsumer>(java.lang.invoke.LambdaMetafactory.metafactory(methodTypeOf((I)V), handleOf(dev/sim0n/evaluator/Main.lambda$main$5([ILdev/sim0n/evaluator/util/stats/Calculations;[DI)V (6)), methodTypeOf((I)V), lvar1_0, lvar5_0, lvar2_0))));
   _consume(lvar5_0.run(dev.sim0n.evaluator.Main.LOG));
   lvar7_0 = new dev.sim0n.evaluator.manager.TestManager;
   _consume(lvar7_0.<init>());
   _consume(lvar7_0.handleTests());
   _consume(dev.sim0n.evaluator.Main.LOG.println("
   Testing cryptography (Blowfish)"));
   lvar8_0 = new dev.sim0n.evaluator.util.crypto.Blowfish;
   _consume(lvar8_0.<init>("jHASf72183hjASf123"));
   lvar10_0 = lvar8_0.decryptString("5f45e43ca774e1d2611c6fc31c7e4b11ef4780e0ba9ba304b9da8b28bc86582e6745624bb00bfbc7a71f97a1e708e13bcfd6f700d77216680a52dc1d16e3a9dc2747a26466eb273d");
   _consume(java.lang.System.out.println("Testing large string"));
   svar1_72 = new java.lang.StringBuilder;
   _consume(svar1_72.<init>());
   svar0_31 = dev.sim0n.evaluator.Main.LOG;
   if ("5f45e43ca774e1d2611c6fc31c7e4b11ef4780e0ba9ba304b9da8b28bc86582e6745624bb00bfbc7a71f97a1e708e13bcfd6f700d77216680a52dc1d16e3a9dc2747a26466eb273d5f45e43ca774e1d2611c6fc31c7e4b11ef4780e0ba9ba304b9da8b28bc86582e6745624bb00bfbc7a71f97a1e708e13bcfd6f700d77216680a52dc1d16e3a9dc2747a26466eb273d".equals(svar1_72.append("5f45e43ca774e1d2611c6fc31c7e4b11ef4780e0ba9ba304b9da8b28bc86582e6745624bb00bfbc7a71f97a1e708e13bcfd6f700d77216680a52dc1d16e3a9dc2747a26466eb273d").append("5f45e43ca774e1d2611c6fc31c7e4b11ef4780e0ba9ba304b9da8b28bc86582e6745624bb00bfbc7a71f97a1e708e13bcfd6f700d77216680a52dc1d16e3a9dc2747a26466eb273d").toString()) == 0)
      goto D
   
BLOCK C:
   svar1_77 = "Successfully compared strings";
   goto E
   
BLOCK F:
   svar1_81 = new java.lang.StringBuilder;
   _consume(svar1_81.<init>());
   svar1_84 = svar1_81.append("Successfully decrypted ").append(lvar10_0).toString();
   goto H
   
BLOCK G:
   svar1_86 = new java.lang.StringBuilder;
   _consume(svar1_86.<init>());
   svar1_89 = svar1_86.append("Failed to decrypt ").append(lvar10_0).toString();
   
BLOCK D:
   svar1_90 = "Unable to compare strings";
   
BLOCK K:
   lvar14_0 = catch();
   _consume(lvar14_0.printStackTrace());
   
BLOCK J:
   goto L
   
BLOCK L:
   return;
   

```

### Method: <clinit>()V
Access: static

```ssa
BLOCK A:
   
BLOCK B:
   svar0_0 = new java.security.SecureRandom;
   _consume(svar0_0.<init>());
   dev.sim0n.evaluator.Main.RANDOM = svar0_0;
   svar0_1 = new dev.sim0n.evaluator.util.Log;
   _consume(svar0_1.<init>());
   dev.sim0n.evaluator.Main.LOG = svar0_1;
   return;
   

```


## Class: dev/sim0n/evaluator/operation/DoubleMathOperation
Super: java/lang/Enum
Interfaces: []
Access: public synchronized abstract enum

### Method: values()[Ldev/sim0n/evaluator/operation/DoubleMathOperation;
Access: public static

```ssa
BLOCK B:
   return (dev.sim0n.evaluator.operation.DoubleMathOperation[])dev.sim0n.evaluator.operation.DoubleMathOperation.$VALUES.clone();
   
BLOCK A:
   

```

### Method: valueOf(Ljava/lang/String;)Ldev/sim0n/evaluator/operation/DoubleMathOperation;
Access: public static

```ssa
BLOCK B:
   return (dev.sim0n.evaluator.operation.DoubleMathOperation)java.lang.Enum.valueOf(dev.sim0n.evaluator.operation.DoubleMathOperation.class, lvar0_0);
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   

```

### Method: evaluate(DD)D
Access: public abstract

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar3_0 = lvar3_0);
   
BLOCK B:
   

```

### Method: getDesc()Ljava/lang/String;
Access: public

```ssa
BLOCK B:
   return lvar0_0.desc;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   

```

### Method: <init>(Ljava/lang/String;ILjava/lang/String;)V
Access: private

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0, lvar2_0));
   lvar0_0.desc = lvar3_0;
   return;
   

```

### Method: <clinit>()V
Access: static

```ssa
BLOCK A:
   
BLOCK B:
   svar0_0 = new dev.sim0n.evaluator.operation.DoubleMathOperation$1;
   _consume(svar0_0.<init>("ADD", 0, "+"));
   dev.sim0n.evaluator.operation.DoubleMathOperation.ADD = svar0_0;
   svar0_1 = new dev.sim0n.evaluator.operation.DoubleMathOperation$2;
   _consume(svar0_1.<init>("SUB", 1, "-"));
   dev.sim0n.evaluator.operation.DoubleMathOperation.SUB = svar0_1;
   svar0_2 = new dev.sim0n.evaluator.operation.DoubleMathOperation$3;
   _consume(svar0_2.<init>("DIV", 2, "/"));
   dev.sim0n.evaluator.operation.DoubleMathOperation.DIV = svar0_2;
   svar0_3 = new dev.sim0n.evaluator.operation.DoubleMathOperation$4;
   _consume(svar0_3.<init>("REM", 3, "%"));
   dev.sim0n.evaluator.operation.DoubleMathOperation.REM = svar0_3;
   svar0_4 = new dev.sim0n.evaluator.operation.DoubleMathOperation$5;
   _consume(svar0_4.<init>("MUL", 4, "*"));
   dev.sim0n.evaluator.operation.DoubleMathOperation.MUL = svar0_4;
   svar0_6 = new dev.sim0n.evaluator.operation.DoubleMathOperation[5];
   svar0_6[0] = dev.sim0n.evaluator.operation.DoubleMathOperation.ADD;
   svar0_6[1] = dev.sim0n.evaluator.operation.DoubleMathOperation.SUB;
   svar0_6[2] = dev.sim0n.evaluator.operation.DoubleMathOperation.DIV;
   svar0_6[3] = dev.sim0n.evaluator.operation.DoubleMathOperation.REM;
   svar0_6[4] = dev.sim0n.evaluator.operation.DoubleMathOperation.MUL;
   dev.sim0n.evaluator.operation.DoubleMathOperation.$VALUES = svar0_6;
   return;
   

```


## Class: dev/sim0n/evaluator/util/crypto/Blowfish
Super: java/lang/Object
Interfaces: []
Access: public synchronized

### Method: <init>(Ljava/lang/String;)V
Access: public

```ssa
BLOCK B:
   _consume(lvar0_0.<init>());
   lvar2_0 = nullconst;
   
BLOCK G:
   lvar2_3 = ɸ{F:lvar2_1, E:lvar2_2};
   svar1_2 = new dev.sim0n.evaluator.util.crypto.Blowfish$BlowfishCBC;
   _consume(svar1_2.<init>(lvar2_3.digest(), 0L));
   lvar0_0.m_bfish = svar1_2;
   _consume(lvar2_3.reset());
   return;
   
BLOCK F:
   goto G
   
BLOCK C:
   lvar2_1 = java.security.MessageDigest.getInstance("SHA1");
   
BLOCK D:
   _consume(lvar2_1.update(lvar1_0.getBytes()));
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK E:
   lvar2_2 = ɸ{C:lvar2_0, D:lvar2_1};
   svar0_5 = catch();
   

```

### Method: encryptString(Ljava/lang/String;)Ljava/lang/String;
Access: public

```ssa
BLOCK D:
   lvar5_0 = catch();
   MONITOREXIT(lvar4_0);
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK E:
   throw lvar5_0;
   
BLOCK G:
   return lvar0_0.encStr(lvar1_0, lvar2_0);
   
BLOCK B:
   lvar4_0 = dev.sim0n.evaluator.util.crypto.Blowfish.m_rndGen;
   MONITORENTER(dev.sim0n.evaluator.util.crypto.Blowfish.m_rndGen);
   
BLOCK F:
   goto G
   
BLOCK C:
   lvar2_0 = dev.sim0n.evaluator.util.crypto.Blowfish.m_rndGen.nextLong();
   MONITOREXIT(dev.sim0n.evaluator.util.crypto.Blowfish.m_rndGen);
   

```

### Method: encStr(Ljava/lang/String;J)Ljava/lang/String;
Access: private

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   
BLOCK K:
   throw lvar10_0;
   
BLOCK F:
   lvar9_0 = lvar0_0.m_bfish;
   MONITORENTER(lvar0_0.m_bfish);
   
BLOCK B:
   lvar4_0 = lvar1_0.length();
   lvar5_0 = new byte[{({{lvar4_0 << 1} & -8}) + 8}];
   lvar7_0 = 0;
   lvar6_0 = 0;
   
BLOCK H:
   goto I
   
BLOCK M:
   lvar8_1 = lvar1_0.charAt(lvar6_1);
   lvar7_4 = {lvar7_1 + 1};
   svar2_6 = {lvar8_1 >> 8};
   svar2_7 = {svar2_6 & 255};
   lvar5_0[lvar7_1] = (byte)svar2_7;
   lvar7_5 = {lvar7_4 + 1};
   svar2_10 = {lvar8_1 & 255};
   lvar5_0[lvar7_4] = (byte)svar2_10;
   lvar6_2 = {lvar6_1 + 1};
   goto C
   
BLOCK D:
   svar0_12 = {lvar5_0.length - ({lvar4_0 << 1})};
   
BLOCK I:
   lvar9_1 = new byte[8];
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.longToByteArray(lvar2_0, lvar9_1, 0));
   svar0_25 = new java.lang.StringBuilder;
   _consume(svar0_25.<init>());
   return svar0_25.append(dev.sim0n.evaluator.util.crypto.Blowfish.bytesToBinHex(lvar9_1, 0, 8)).append(dev.sim0n.evaluator.util.crypto.Blowfish.bytesToBinHex(lvar5_0, 0, lvar5_0.length)).toString();
   
BLOCK J:
   lvar10_0 = catch();
   MONITOREXIT(lvar9_0);
   
BLOCK G:
   _consume(lvar0_0.m_bfish.setCBCIV(lvar2_0));
   _consume(lvar0_0.m_bfish.encrypt(lvar5_0));
   MONITOREXIT(lvar0_0.m_bfish);
   
BLOCK C:
   lvar7_1 = ɸ{B:lvar7_0, M:lvar7_5};
   lvar6_1 = ɸ{B:lvar6_0, M:lvar6_2};
   if (lvar6_1 >= lvar4_0)
      goto D
   
BLOCK L:
   lvar7_3 = {lvar7_2 + 1};
   lvar5_0[lvar7_2] = (byte)svar0_12;
   goto E
   
BLOCK E:
   lvar7_2 = ɸ{L:lvar7_3, D:lvar7_1};
   if (lvar7_2 >= lvar5_0.length)
      goto F
   

```

### Method: decryptString(Ljava/lang/String;)Ljava/lang/String;
Access: public

```ssa
BLOCK D:
   lvar3_0 = new byte[8];
   if (dev.sim0n.evaluator.util.crypto.Blowfish.binHexToBytes(lvar1_0, lvar3_0, 0, 0, 8) >= 8)
      goto F
   
BLOCK R:
   lvar6_3 = ɸ{P:lvar6_1, Q:lvar6_2};
   lvar4_2 = {lvar4_1 - lvar6_3};
   if (lvar4_2 >= 0)
      goto S
   
BLOCK H:
   lvar5_0 = new byte[lvar2_1];
   lvar4_1 = dev.sim0n.evaluator.util.crypto.Blowfish.binHexToBytes(lvar1_0, lvar5_0, 16, 0, lvar2_1);
   if (lvar4_1 >= lvar2_1)
      goto J
   
BLOCK P:
   if (lvar6_1 >= 0)
      goto R
   
BLOCK K:
   _consume(lvar0_0.m_bfish.setCBCIV(lvar3_0));
   _consume(lvar0_0.m_bfish.decrypt(lvar5_0));
   MONITOREXIT(lvar0_0.m_bfish);
   
BLOCK Q:
   lvar6_2 = 0;
   
BLOCK S:
   return dev.sim0n.evaluator.util.crypto.Blowfish.byteArrayToUNCString(lvar5_0, 0, lvar4_2);
   
BLOCK C:
   return nullconst;
   
BLOCK O:
   lvar6_1 = {lvar5_0[{lvar5_0.length - 1}] & 255};
   if (lvar6_1 > 8)
      goto Q
   
BLOCK T:
   return "";
   
BLOCK J:
   lvar6_0 = lvar0_0.m_bfish;
   MONITORENTER(lvar0_0.m_bfish);
   
BLOCK N:
   goto O
   
BLOCK F:
   lvar2_1 = {lvar2_0 + -8};
   if (lvar2_1 != 0)
      goto H
   
BLOCK L:
   lvar7_0 = catch();
   MONITOREXIT(lvar6_0);
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK B:
   lvar2_0 = {{lvar1_0.length() >> 1} & -8};
   if (lvar2_0 >= 8)
      goto D
   
BLOCK E:
   return nullconst;
   
BLOCK G:
   return "";
   
BLOCK I:
   return nullconst;
   
BLOCK M:
   throw lvar7_0;
   

```

### Method: destroy()V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   _consume(lvar0_0.m_bfish.cleanUp());
   return;
   

```

### Method: byteArrayToLong([BI)J
Access: private static

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK B:
   svar0_1 = lvar0_0[lvar1_0];
   svar2_2 = lvar0_0[{lvar1_0 + 1}];
   svar2_7 = lvar0_0[{lvar1_0 + 2}];
   svar2_12 = lvar0_0[{lvar1_0 + 3}];
   svar2_17 = lvar0_0[{lvar1_0 + 4}];
   svar2_22 = lvar0_0[{lvar1_0 + 5}];
   svar2_27 = lvar0_0[{lvar1_0 + 6}];
   svar2_32 = lvar0_0[{lvar1_0 + 7}];
   return {{{{{{{{(long)svar0_1 << 56} | {({(long)svar2_2 & 255L}) << 48}} | {({(long)svar2_7 & 255L}) << 40}} | {({(long)svar2_12 & 255L}) << 32}} | {({(long)svar2_17 & 255L}) << 24}} | {({(long)svar2_22 & 255L}) << 16}} | {({(long)svar2_27 & 255L}) << 8}} | {(long)svar2_32 & 255L}};
   

```

### Method: longToByteArray(J[BI)V
Access: private static

```ssa
BLOCK B:
   lvar2_0[lvar3_0] = (byte)(int)({lvar0_0 >>> 56});
   lvar2_0[{lvar3_0 + 1}] = (byte)(int)({{lvar0_0 >>> 48} & 255L});
   lvar2_0[{lvar3_0 + 2}] = (byte)(int)({{lvar0_0 >>> 40} & 255L});
   lvar2_0[{lvar3_0 + 3}] = (byte)(int)({{lvar0_0 >>> 32} & 255L});
   lvar2_0[{lvar3_0 + 4}] = (byte)(int)({{lvar0_0 >>> 24} & 255L});
   lvar2_0[{lvar3_0 + 5}] = (byte)(int)({{lvar0_0 >>> 16} & 255L});
   lvar2_0[{lvar3_0 + 6}] = (byte)(int)({{lvar0_0 >>> 8} & 255L});
   lvar2_0[{lvar3_0 + 7}] = (byte)(int)lvar0_0;
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   

```

### Method: intArrayToLong([II)J
Access: private static

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK B:
   svar0_1 = lvar0_0[lvar1_0];
   svar2_2 = lvar0_0[{lvar1_0 + 1}];
   return {{(long)svar0_1 << 32} | {(long)svar2_2 & 4294967295L}};
   

```

### Method: longToIntArray(J[II)V
Access: private static

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   
BLOCK B:
   lvar2_0[lvar3_0] = (int)({lvar0_0 >>> 32});
   lvar2_0[{lvar3_0 + 1}] = (int)lvar0_0;
   return;
   

```

### Method: makeLong(II)J
Access: private static

```ssa
BLOCK B:
   return {{(long)lvar1_0 << 32} | {(long)lvar0_0 & 4294967295L}};
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   

```

### Method: longLo32(J)I
Access: private static

```ssa
BLOCK B:
   return (int)lvar0_0;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   

```

### Method: longHi32(J)I
Access: private static

```ssa
BLOCK B:
   return (int)({lvar0_0 >>> 32});
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   

```

### Method: bytesToBinHex([BII)Ljava/lang/String;
Access: private static

```ssa
BLOCK E:
   return lvar3_0.toString();
   
BLOCK C:
   lvar5_1 = ɸ{B:lvar5_0, D:lvar5_2};
   lvar4_1 = ɸ{B:lvar4_0, D:lvar4_3};
   if (lvar5_1 >= lvar2_0)
      goto E
   
BLOCK B:
   lvar3_0 = new java.lang.StringBuilder;
   _consume(lvar3_0.<init>());
   _consume(lvar3_0.setLength({lvar2_0 << 1}));
   lvar4_0 = 0;
   lvar5_0 = 0;
   
BLOCK D:
   lvar4_2 = {lvar4_1 + 1};
   svar2_1 = dev.sim0n.evaluator.util.crypto.Blowfish.HEXTAB;
   svar4_1 = {lvar5_1 + lvar1_0};
   svar3_1 = lvar0_0[svar4_1];
   svar3_2 = {svar3_1 >> 4};
   svar3_3 = {svar3_2 & 15};
   svar2_2 = svar2_1[svar3_3];
   _consume(lvar3_0.setCharAt(lvar4_1, svar2_2));
   lvar4_3 = {lvar4_2 + 1};
   svar2_3 = dev.sim0n.evaluator.util.crypto.Blowfish.HEXTAB;
   svar4_5 = {lvar5_1 + lvar1_0};
   svar3_5 = lvar0_0[svar4_5];
   svar3_6 = {svar3_5 & 15};
   svar2_4 = svar2_3[svar3_6];
   _consume(lvar3_0.setCharAt(lvar4_2, svar2_4));
   lvar5_2 = {lvar5_1 + 1};
   goto C
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   

```

### Method: binHexToBytes(Ljava/lang/String;[BIII)I
Access: private static

```ssa
BLOCK E:
   lvar4_3 = lvar7_0;
   
BLOCK P:
   svar1_17 = {lvar13_0 - 97};
   svar1_19 = {(byte)svar1_17 + 10};
   svar0_33 = {(byte)svar0_20 | svar1_19};
   lvar10_5 = (byte)svar0_33;
   goto Q
   
BLOCK Q:
   lvar11_2 = ɸ{P:lvar11_1, N:lvar11_1, O:lvar11_3};
   lvar10_4 = ɸ{P:lvar10_5, N:lvar10_3, O:lvar10_2};
   lvar12_2 = {lvar12_1 + 1};
   goto I
   
BLOCK L:
   if (lvar13_0 < 48)
      goto O
   
BLOCK T:
   lvar8_3 = ɸ{R:lvar8_1, S:lvar8_2};
   lvar3_3 = ɸ{R:lvar3_1, S:lvar3_2};
   lvar9_2 = {lvar9_1 + 1};
   goto G
   
BLOCK U:
   return lvar8_1;
   
BLOCK B:
   lvar6_0 = {{lvar0_0.length() - lvar2_0} >> 1};
   if (lvar6_0 >= lvar4_0)
      goto D
   
BLOCK C:
   lvar4_1 = lvar6_0;
   
BLOCK N:
   svar1_14 = {lvar13_0 - 48};
   svar0_29 = {(byte)svar0_20 | (byte)svar1_14};
   lvar10_3 = (byte)svar0_29;
   goto Q
   
BLOCK R:
   if (lvar11_1 == 0)
      goto T
   
BLOCK I:
   lvar12_1 = ɸ{Q:lvar12_2, H:lvar12_0};
   lvar11_1 = ɸ{Q:lvar11_2, H:lvar11_0};
   lvar10_1 = ɸ{Q:lvar10_4, H:lvar10_0};
   lvar2_2 = ɸ{Q:lvar2_3, H:lvar2_1};
   if (lvar12_1 >= 2)
      goto R
   
BLOCK G:
   lvar9_1 = ɸ{T:lvar9_2, F:lvar9_0};
   lvar8_1 = ɸ{T:lvar8_3, F:lvar8_0};
   lvar3_1 = ɸ{T:lvar3_3, F:lvar3_0};
   lvar2_1 = ɸ{T:lvar2_2, F:lvar2_0};
   if (lvar9_1 >= lvar4_4)
      goto U
   
BLOCK H:
   lvar10_0 = 0;
   lvar11_0 = 1;
   lvar12_0 = 0;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   synth(lvar4_0 = lvar4_0);
   
BLOCK F:
   lvar4_4 = ɸ{E:lvar4_3, D:lvar4_2};
   lvar8_0 = 0;
   lvar9_0 = 0;
   
BLOCK M:
   if (lvar13_0 > 57)
      goto O
   
BLOCK J:
   svar0_20 = {lvar10_1 << 4};
   lvar10_2 = (byte)svar0_20;
   lvar2_3 = {lvar2_2 + 1};
   lvar13_0 = lvar0_0.charAt(lvar2_2);
   if (lvar13_0 < 97)
      goto L
   
BLOCK S:
   lvar3_2 = {lvar3_1 + 1};
   lvar1_0[lvar3_1] = lvar10_1;
   lvar8_2 = {lvar8_1 + 1};
   
BLOCK K:
   if (lvar13_0 > 102)
      goto L
   
BLOCK O:
   lvar11_3 = 0;
   
BLOCK D:
   lvar4_2 = ɸ{C:lvar4_1, B:lvar4_0};
   lvar7_0 = {lvar1_0.length - lvar3_0};
   if (lvar4_2 <= lvar7_0)
      goto F
   

```

### Method: byteArrayToUNCString([BII)Ljava/lang/String;
Access: private static

```ssa
BLOCK C:
   lvar2_2 = lvar3_0;
   
BLOCK B:
   lvar2_1 = {lvar2_0 & -2};
   lvar3_0 = {lvar0_0.length - lvar1_0};
   if (lvar3_0 >= lvar2_1)
      goto D
   
BLOCK E:
   lvar5_1 = ɸ{F:lvar5_2, D:lvar5_0};
   lvar2_4 = ɸ{F:lvar2_5, D:lvar2_3};
   lvar1_1 = ɸ{F:lvar1_2, D:lvar1_0};
   if (lvar2_4 <= 0)
      goto G
   
BLOCK G:
   return lvar4_0.toString();
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   
BLOCK F:
   lvar5_2 = {lvar5_1 + 1};
   svar2_2 = lvar0_0[lvar1_1];
   svar2_3 = {svar2_2 << 8};
   svar4_1 = {lvar1_1 + 1};
   svar3_3 = lvar0_0[svar4_1];
   svar3_4 = {svar3_3 & 255};
   svar2_4 = {svar2_3 | svar3_4};
   _consume(lvar4_0.setCharAt(lvar5_1, (char)svar2_4));
   lvar1_2 = {lvar1_1 + 2};
   lvar2_5 = {lvar2_4 + -2};
   goto E
   
BLOCK D:
   lvar2_3 = ɸ{C:lvar2_2, B:lvar2_1};
   lvar4_0 = new java.lang.StringBuilder;
   _consume(lvar4_0.<init>());
   _consume(lvar4_0.setLength({lvar2_3 >> 1}));
   lvar5_0 = 0;
   

```

### Method: <clinit>()V
Access: static

```ssa
BLOCK A:
   
BLOCK B:
   svar0_0 = new java.util.Random;
   _consume(svar0_0.<init>());
   dev.sim0n.evaluator.util.crypto.Blowfish.m_rndGen = svar0_0;
   svar0_2 = new char[16];
   svar0_2[0] = 48;
   svar0_2[1] = 49;
   svar0_2[2] = 50;
   svar0_2[3] = 51;
   svar0_2[4] = 52;
   svar0_2[5] = 53;
   svar0_2[6] = 54;
   svar0_2[7] = 55;
   svar0_2[8] = 56;
   svar0_2[9] = 57;
   svar0_2[10] = 97;
   svar0_2[11] = 98;
   svar0_2[12] = 99;
   svar0_2[13] = 100;
   svar0_2[14] = 101;
   svar0_2[15] = 102;
   dev.sim0n.evaluator.util.crypto.Blowfish.HEXTAB = svar0_2;
   return;
   

```


## Class: dev/sim0n/evaluator/operation/IntMathOperation
Super: java/lang/Enum
Interfaces: []
Access: public synchronized abstract enum

### Method: values()[Ldev/sim0n/evaluator/operation/IntMathOperation;
Access: public static

```ssa
BLOCK B:
   return (dev.sim0n.evaluator.operation.IntMathOperation[])dev.sim0n.evaluator.operation.IntMathOperation.$VALUES.clone();
   
BLOCK A:
   

```

### Method: valueOf(Ljava/lang/String;)Ldev/sim0n/evaluator/operation/IntMathOperation;
Access: public static

```ssa
BLOCK B:
   return (dev.sim0n.evaluator.operation.IntMathOperation)java.lang.Enum.valueOf(dev.sim0n.evaluator.operation.IntMathOperation.class, lvar0_0);
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   

```

### Method: evaluate(II)I
Access: public abstract

```ssa
BLOCK B:
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   

```

### Method: getDesc()Ljava/lang/String;
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   return lvar0_0.desc;
   

```

### Method: <init>(Ljava/lang/String;ILjava/lang/String;)V
Access: private

```ssa
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0, lvar2_0));
   lvar0_0.desc = lvar3_0;
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   

```

### Method: <clinit>()V
Access: static

```ssa
BLOCK B:
   svar0_0 = new dev.sim0n.evaluator.operation.IntMathOperation$1;
   _consume(svar0_0.<init>("ADD", 0, "+"));
   dev.sim0n.evaluator.operation.IntMathOperation.ADD = svar0_0;
   svar0_1 = new dev.sim0n.evaluator.operation.IntMathOperation$2;
   _consume(svar0_1.<init>("SUB", 1, "-"));
   dev.sim0n.evaluator.operation.IntMathOperation.SUB = svar0_1;
   svar0_2 = new dev.sim0n.evaluator.operation.IntMathOperation$3;
   _consume(svar0_2.<init>("DIV", 2, "/"));
   dev.sim0n.evaluator.operation.IntMathOperation.DIV = svar0_2;
   svar0_3 = new dev.sim0n.evaluator.operation.IntMathOperation$4;
   _consume(svar0_3.<init>("REM", 3, "%"));
   dev.sim0n.evaluator.operation.IntMathOperation.REM = svar0_3;
   svar0_4 = new dev.sim0n.evaluator.operation.IntMathOperation$5;
   _consume(svar0_4.<init>("MUL", 4, "*"));
   dev.sim0n.evaluator.operation.IntMathOperation.MUL = svar0_4;
   svar0_5 = new dev.sim0n.evaluator.operation.IntMathOperation$6;
   _consume(svar0_5.<init>("XOR", 5, "^"));
   dev.sim0n.evaluator.operation.IntMathOperation.XOR = svar0_5;
   svar0_7 = new dev.sim0n.evaluator.operation.IntMathOperation[6];
   svar0_7[0] = dev.sim0n.evaluator.operation.IntMathOperation.ADD;
   svar0_7[1] = dev.sim0n.evaluator.operation.IntMathOperation.SUB;
   svar0_7[2] = dev.sim0n.evaluator.operation.IntMathOperation.DIV;
   svar0_7[3] = dev.sim0n.evaluator.operation.IntMathOperation.REM;
   svar0_7[4] = dev.sim0n.evaluator.operation.IntMathOperation.MUL;
   svar0_7[5] = dev.sim0n.evaluator.operation.IntMathOperation.XOR;
   dev.sim0n.evaluator.operation.IntMathOperation.$VALUES = svar0_7;
   return;
   
BLOCK A:
   

```


## Class: dev/sim0n/evaluator/util/crypto/Blowfish$BlowfishCBC
Super: dev/sim0n/evaluator/util/crypto/Blowfish$BlowfishECB
Interfaces: []
Access: synchronized

### Method: getCBCIV()J
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   return lvar0_0.m_lCBCIV;
   

```

### Method: getCBCIV([B)V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK B:
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$400(lvar0_0.m_lCBCIV, lvar1_0, 0));
   return;
   

```

### Method: setCBCIV(J)V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK B:
   lvar0_0.m_lCBCIV = lvar1_0;
   return;
   

```

### Method: setCBCIV([B)V
Access: public

```ssa
BLOCK B:
   lvar0_0.m_lCBCIV = dev.sim0n.evaluator.util.crypto.Blowfish.access$300(lvar1_0, 0);
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   

```

### Method: <init>([B)V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0));
   _consume(lvar0_0.setCBCIV(0L));
   return;
   

```

### Method: <init>([BJ)V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0));
   _consume(lvar0_0.setCBCIV(lvar2_0));
   return;
   

```

### Method: <init>([B[B)V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0));
   _consume(lvar0_0.setCBCIV(lvar2_0));
   return;
   

```

### Method: cleanUp()V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   lvar0_0.m_lCBCIV = 0L;
   _consume(lvar0_0.cleanUp());
   return;
   

```

### Method: encryptBlockCBC(J)J
Access: private

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK B:
   lvar1_2 = lvar0_0.encryptBlock({lvar1_0 ^ lvar0_0.m_lCBCIV});
   lvar0_0.m_lCBCIV = lvar1_2;
   return lvar1_2;
   

```

### Method: decryptBlockCBC(J)J
Access: private

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK B:
   lvar1_2 = {lvar0_0.decryptBlock(lvar1_0) ^ lvar0_0.m_lCBCIV};
   lvar0_0.m_lCBCIV = lvar1_0;
   return lvar1_2;
   

```

### Method: encrypt([B[B)V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   
BLOCK B:
   lvar6_0 = 0;
   
BLOCK D:
   lvar4_0 = dev.sim0n.evaluator.util.crypto.Blowfish.access$300(lvar1_0, lvar6_1);
   lvar4_1 = lvar0_0.encryptBlockCBC(lvar4_0);
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$400(lvar4_1, lvar2_0, lvar6_1));
   lvar6_2 = {lvar6_1 + 8};
   goto C
   
BLOCK E:
   return;
   
BLOCK C:
   lvar6_1 = ɸ{D:lvar6_2, B:lvar6_0};
   if (lvar6_1 >= lvar1_0.length)
      goto E
   

```

### Method: encrypt([B)V
Access: public

```ssa
BLOCK E:
   lvar3_0 = dev.sim0n.evaluator.util.crypto.Blowfish.access$300(lvar1_0, lvar5_1);
   lvar3_1 = lvar0_0.encryptBlockCBC(lvar3_0);
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$400(lvar3_1, lvar1_0, lvar5_1));
   lvar5_2 = {lvar5_1 + 8};
   goto C
   
BLOCK C:
   lvar5_1 = ɸ{E:lvar5_2, B:lvar5_0};
   if (lvar5_1 >= lvar1_0.length)
      goto D
   
BLOCK B:
   lvar5_0 = 0;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK D:
   return;
   

```

### Method: encrypt([I[I)V
Access: public

```ssa
BLOCK E:
   return;
   
BLOCK B:
   lvar6_0 = 0;
   
BLOCK C:
   lvar6_1 = ɸ{B:lvar6_0, D:lvar6_2};
   if (lvar6_1 >= lvar1_0.length)
      goto E
   
BLOCK D:
   lvar4_0 = dev.sim0n.evaluator.util.crypto.Blowfish.access$500(lvar1_0, lvar6_1);
   lvar4_1 = lvar0_0.encryptBlockCBC(lvar4_0);
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$600(lvar4_1, lvar2_0, lvar6_1));
   lvar6_2 = {lvar6_1 + 2};
   goto C
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   

```

### Method: encrypt([I)V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK E:
   return;
   
BLOCK C:
   lvar5_1 = ɸ{B:lvar5_0, D:lvar5_2};
   if (lvar5_1 >= lvar1_0.length)
      goto E
   
BLOCK B:
   lvar5_0 = 0;
   
BLOCK D:
   lvar3_0 = dev.sim0n.evaluator.util.crypto.Blowfish.access$500(lvar1_0, lvar5_1);
   lvar3_1 = lvar0_0.encryptBlockCBC(lvar3_0);
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$600(lvar3_1, lvar1_0, lvar5_1));
   lvar5_2 = {lvar5_1 + 2};
   goto C
   

```

### Method: encrypt([J[J)V
Access: public

```ssa
BLOCK C:
   lvar4_1 = ɸ{B:lvar4_0, D:lvar4_2};
   if (lvar4_1 >= lvar1_0.length)
      goto E
   
BLOCK E:
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   
BLOCK B:
   lvar4_0 = 0;
   
BLOCK D:
   svar3_1 = lvar1_0[lvar4_1];
   svar2_1 = lvar0_0.encryptBlockCBC(svar3_1);
   lvar2_0[lvar4_1] = svar2_1;
   lvar4_2 = {lvar4_1 + 1};
   goto C
   

```

### Method: encrypt([J)V
Access: public

```ssa
BLOCK B:
   lvar3_0 = 0;
   
BLOCK C:
   lvar3_1 = ɸ{D:lvar3_2, B:lvar3_0};
   if (lvar3_1 >= lvar1_0.length)
      goto E
   
BLOCK D:
   svar3_1 = lvar1_0[lvar3_1];
   svar2_1 = lvar0_0.encryptBlockCBC(svar3_1);
   lvar1_0[lvar3_1] = svar2_1;
   lvar3_2 = {lvar3_1 + 1};
   goto C
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK E:
   return;
   

```

### Method: decrypt([B[B)V
Access: public

```ssa
BLOCK D:
   return;
   
BLOCK E:
   lvar4_0 = dev.sim0n.evaluator.util.crypto.Blowfish.access$300(lvar1_0, lvar6_1);
   lvar4_1 = lvar0_0.decryptBlockCBC(lvar4_0);
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$400(lvar4_1, lvar2_0, lvar6_1));
   lvar6_2 = {lvar6_1 + 8};
   goto C
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   
BLOCK C:
   lvar6_1 = ɸ{E:lvar6_2, B:lvar6_0};
   if (lvar6_1 >= lvar1_0.length)
      goto D
   
BLOCK B:
   lvar6_0 = 0;
   

```

### Method: decrypt([B)V
Access: public

```ssa
BLOCK B:
   lvar5_0 = 0;
   
BLOCK E:
   return;
   
BLOCK D:
   lvar3_0 = dev.sim0n.evaluator.util.crypto.Blowfish.access$300(lvar1_0, lvar5_1);
   lvar3_1 = lvar0_0.decryptBlockCBC(lvar3_0);
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$400(lvar3_1, lvar1_0, lvar5_1));
   lvar5_2 = {lvar5_1 + 8};
   goto C
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK C:
   lvar5_1 = ɸ{B:lvar5_0, D:lvar5_2};
   if (lvar5_1 >= lvar1_0.length)
      goto E
   

```

### Method: decrypt([I[I)V
Access: public

```ssa
BLOCK B:
   lvar6_0 = 0;
   
BLOCK E:
   return;
   
BLOCK D:
   lvar4_0 = dev.sim0n.evaluator.util.crypto.Blowfish.access$500(lvar1_0, lvar6_1);
   lvar4_1 = lvar0_0.decryptBlockCBC(lvar4_0);
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$600(lvar4_1, lvar2_0, lvar6_1));
   lvar6_2 = {lvar6_1 + 2};
   goto C
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   
BLOCK C:
   lvar6_1 = ɸ{B:lvar6_0, D:lvar6_2};
   if (lvar6_1 >= lvar1_0.length)
      goto E
   

```

### Method: decrypt([I)V
Access: public

```ssa
BLOCK C:
   lvar5_1 = ɸ{B:lvar5_0, D:lvar5_2};
   if (lvar5_1 >= lvar1_0.length)
      goto E
   
BLOCK E:
   return;
   
BLOCK B:
   lvar5_0 = 0;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK D:
   lvar3_0 = dev.sim0n.evaluator.util.crypto.Blowfish.access$500(lvar1_0, lvar5_1);
   lvar3_1 = lvar0_0.decryptBlockCBC(lvar3_0);
   _consume(dev.sim0n.evaluator.util.crypto.Blowfish.access$600(lvar3_1, lvar1_0, lvar5_1));
   lvar5_2 = {lvar5_1 + 2};
   goto C
   

```

### Method: decrypt([J[J)V
Access: public

```ssa
BLOCK C:
   lvar4_1 = ɸ{D:lvar4_2, B:lvar4_0};
   if (lvar4_1 >= lvar1_0.length)
      goto E
   
BLOCK E:
   return;
   
BLOCK D:
   svar3_1 = lvar1_0[lvar4_1];
   svar2_1 = lvar0_0.decryptBlockCBC(svar3_1);
   lvar2_0[lvar4_1] = svar2_1;
   lvar4_2 = {lvar4_1 + 1};
   goto C
   
BLOCK B:
   lvar4_0 = 0;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   

```

### Method: decrypt([J)V
Access: public

```ssa
BLOCK D:
   return;
   
BLOCK E:
   svar3_1 = lvar1_0[lvar3_1];
   svar2_1 = lvar0_0.decryptBlockCBC(svar3_1);
   lvar1_0[lvar3_1] = svar2_1;
   lvar3_2 = {lvar3_1 + 1};
   goto C
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK B:
   lvar3_0 = 0;
   
BLOCK C:
   lvar3_1 = ɸ{E:lvar3_2, B:lvar3_0};
   if (lvar3_1 >= lvar1_0.length)
      goto D
   

```


## Class: dev/sim0n/evaluator/manager/TestManager
Super: java/lang/Object
Interfaces: []
Access: public synchronized

### Method: <init>()V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   _consume(lvar0_0.<init>());
   svar1_0 = new java.util.ArrayList;
   _consume(svar1_0.<init>());
   lvar0_0.tests = svar1_0;
   _consume(dev.sim0n.evaluator.manager.TestManager.TEST_CLASSES.forEach(dynamic_invoke<java.util.function.Consumer>(java.lang.invoke.LambdaMetafactory.metafactory(methodTypeOf((Ljava/lang/Object;)V), handleOf(dev/sim0n/evaluator/manager/TestManager.lambda$new$0(Ljava/lang/Class;)V (7)), methodTypeOf((Ljava/lang/Class;)V), lvar0_0))));
   svar0_3 = dev.sim0n.evaluator.Main.LOG;
   svar2_2 = new java.lang.Object[1];
   svar2_2[0] = java.lang.Integer.valueOf(lvar0_0.tests.size());
   _consume(svar0_3.println(java.lang.String.format("Loaded %d tests", svar2_2)));
   return;
   

```

### Method: handleTests()V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   _consume(lvar0_0.tests.forEach(dynamic_invoke<java.util.function.Consumer>(java.lang.invoke.LambdaMetafactory.metafactory(methodTypeOf((Ljava/lang/Object;)V), handleOf(dev/sim0n/evaluator/test/Test.handle()V (9 itf)), methodTypeOf((Ldev/sim0n/evaluator/test/Test;)V)))));
   return;
   

```

### Method: <clinit>()V
Access: static

```ssa
BLOCK B:
   svar0_1 = new java.lang.Class[2];
   svar0_1[0] = dev.sim0n.evaluator.test.impl.annotation.AnnotationTest.class;
   svar0_1[1] = dev.sim0n.evaluator.test.impl.exception.OpaqueConditionTest.class;
   dev.sim0n.evaluator.manager.TestManager.TEST_CLASSES = java.util.Arrays.asList(svar0_1);
   return;
   
BLOCK A:
   

```


## Class: dev/sim0n/evaluator/Main$1
Super: java/lang/Object
Interfaces: []
Access: synchronized synthetic

### Method: <clinit>()V
Access: static

```ssa
BLOCK D:
   svar0_4 = catch();
   
BLOCK F:
   dev.sim0n.evaluator.Main$1.$SwitchMap$dev$sim0n$evaluator$operation$Operation[dev.sim0n.evaluator.operation.Operation.DOUBLE.ordinal()] = 2;
   
BLOCK B:
   dev.sim0n.evaluator.Main$1.$SwitchMap$dev$sim0n$evaluator$operation$Operation = new int[dev.sim0n.evaluator.operation.Operation.values().length];
   
BLOCK I:
   return;
   
BLOCK A:
   
BLOCK H:
   goto I
   
BLOCK C:
   dev.sim0n.evaluator.Main$1.$SwitchMap$dev$sim0n$evaluator$operation$Operation[dev.sim0n.evaluator.operation.Operation.INT.ordinal()] = 1;
   
BLOCK E:
   goto F
   
BLOCK G:
   svar0_6 = catch();
   

```


## Class: dev/sim0n/evaluator/util/Evaluation
Super: java/lang/Object
Interfaces: []
Access: public synchronized

### Method: getFirst()Ljava/lang/Number;
Access: public

```ssa
BLOCK B:
   return lvar0_0.first;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   

```

### Method: getSecond()Ljava/lang/Number;
Access: public

```ssa
BLOCK B:
   return lvar0_0.second;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   

```

### Method: getEvaluator()Ljava/util/function/Consumer;
Access: public

```ssa
BLOCK B:
   return lvar0_0.evaluator;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   

```

### Method: <init>(Ljava/lang/Number;Ljava/lang/Number;Ljava/util/function/Consumer;)V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   
BLOCK B:
   _consume(lvar0_0.<init>());
   lvar0_0.first = lvar1_0;
   lvar0_0.second = lvar2_0;
   lvar0_0.evaluator = lvar3_0;
   return;
   

```


## Class: dev/sim0n/evaluator/test/impl/annotation/AnnotationTest
Super: java/lang/Object
Interfaces: [dev/sim0n/evaluator/test/Test]
Access: public synchronized

### Method: <init>()V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   _consume(lvar0_0.<init>());
   return;
   

```

### Method: handle()V
Access: public

```ssa
BLOCK B:
   if (dev.sim0n.evaluator.test.impl.annotation.AnnotationTest.class.isAnnotationPresent(dev.sim0n.evaluator.test.impl.annotation.TestAnnotation.class) == 0)
      goto D
   
BLOCK C:
   svar0_4 = dev.sim0n.evaluator.test.impl.annotation.AnnotationTest.class.getAnnotation(dev.sim0n.evaluator.test.impl.annotation.TestAnnotation.class);
   lvar3_0 = ((dev.sim0n.evaluator.test.impl.annotation.TestAnnotation)svar0_4).string();
   lvar4_0 = ((dev.sim0n.evaluator.test.impl.annotation.TestAnnotation)svar0_4).doubleValue();
   lvar6_0 = ((dev.sim0n.evaluator.test.impl.annotation.TestAnnotation)svar0_4).intValue();
   _consume(dev.sim0n.evaluator.Main.LOG.println("Testing annotations"));
   svar0_13 = dev.sim0n.evaluator.Main.LOG;
   svar2_1 = new java.lang.Object[3];
   svar2_1[0] = lvar3_0;
   svar2_1[1] = java.lang.Double.valueOf(lvar4_0);
   svar2_1[2] = java.lang.Integer.valueOf(lvar6_0);
   _consume(svar0_13.println(java.lang.String.format("%s, %s, %d", svar2_1)));
   
BLOCK D:
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   

```


## Class: dev/sim0n/evaluator/test/impl/exception/OpaqueConditionTest
Super: java/lang/Object
Interfaces: [dev/sim0n/evaluator/test/Test]
Access: public synchronized

### Method: <init>()V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   _consume(lvar0_0.<init>());
   return;
   

```

### Method: handle()V
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK C:
   _consume(dev.sim0n.evaluator.util.crypto.AES.main(new java.lang.String[0]));
   if (dev.sim0n.evaluator.test.impl.exception.OpaqueConditionTest.data[0] != 0)
      goto D
   
BLOCK M:
   return;
   
BLOCK E:
   switch (dev.sim0n.evaluator.test.impl.exception.OpaqueConditionTest.data[1]) {
      case 0:
      	 goto	#H
      case 1:
      	 goto	#G
      default:
      	 goto	#F
   }
   
BLOCK N:
   svar0_12 = new java.lang.IllegalArgumentException;
   svar2_4 = new java.lang.StringBuilder;
   _consume(svar2_4.<init>());
   _consume(svar0_12.<init>(svar2_4.append("Failed test! Stage: ").append(lvar1_4).toString()));
   throw svar0_12;
   
BLOCK J:
   svar0_8 = catch();
   lvar1_3 = 4;
   goto L
   
BLOCK K:
   lvar2_1 = catch();
   _consume(lvar2_1.printStackTrace());
   lvar1_5 = -1;
   
BLOCK I:
   lvar1_7 = ɸ{G:lvar1_8, F:lvar1_6, H:lvar1_9};
   _consume(lvar0_0.self(lvar1_7));
   svar0_20 = new java.lang.IllegalArgumentException;
   svar2_8 = new java.lang.StringBuilder;
   _consume(svar2_8.<init>());
   _consume(svar0_20.<init>(svar2_8.append("Failed test! Stage: ").append(lvar1_7).toString()));
   throw svar0_20;
   
BLOCK B:
   
BLOCK G:
   lvar1_8 = 3;
   goto I
   
BLOCK D:
   svar0_7 = new java.lang.IllegalArgumentException;
   svar2_0 = new java.lang.StringBuilder;
   _consume(svar2_0.<init>());
   _consume(svar0_7.<init>(svar2_0.append("Failed test! Stage: ").append(2).toString()));
   throw svar0_7;
   
BLOCK F:
   lvar1_6 = -5;
   goto I
   
BLOCK H:
   lvar1_9 = -2;
   goto I
   
BLOCK L:
   lvar1_4 = ɸ{J:lvar1_3, K:lvar1_5};
   if (dev.sim0n.evaluator.test.impl.exception.OpaqueConditionTest.data[2] == lvar1_4)
      goto M
   

```

### Method: self(I)V
Access: private

```ssa
BLOCK B:
   if (lvar1_0 != 3)
      goto C
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   
BLOCK C:
   return;
   
BLOCK D:
   svar0_1 = new java.lang.IllegalStateException;
   svar2_0 = new java.lang.StringBuilder;
   _consume(svar2_0.<init>());
   _consume(svar0_1.<init>(svar2_0.append("stage=").append(lvar1_0).toString()));
   throw svar0_1;
   

```

### Method: <clinit>()V
Access: static

```ssa
BLOCK B:
   svar0_1 = new byte[5];
   svar0_1[0] = 0;
   svar0_1[1] = 1;
   svar0_1[2] = 4;
   svar0_1[3] = 3;
   svar0_1[4] = 2;
   dev.sim0n.evaluator.test.impl.exception.OpaqueConditionTest.data = svar0_1;
   return;
   
BLOCK A:
   

```


## Class: dev/sim0n/evaluator/util/crypto/AES
Super: java/lang/Object
Interfaces: []
Access: public synchronized

### Method: <init>()V
Access: public

```ssa
BLOCK B:
   _consume(lvar0_0.<init>());
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   

```

### Method: main([Ljava/lang/String;)V
Access: public static

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   lvar2_0 = dev.sim0n.evaluator.util.crypto.AES.getSecretEncryptionKey();
   lvar3_0 = dev.sim0n.evaluator.util.crypto.AES.encryptText("Hello World", lvar2_0);
   lvar4_0 = dev.sim0n.evaluator.util.crypto.AES.decryptText(lvar3_0, lvar2_0);
   _consume(java.lang.System.out.println());
   svar0_7 = java.lang.System.out;
   svar1_2 = new java.lang.StringBuilder;
   _consume(svar1_2.<init>());
   _consume(svar0_7.println(svar1_2.append("Original Text: ").append("Hello World").toString()));
   svar0_8 = java.lang.System.out;
   svar1_6 = new java.lang.StringBuilder;
   _consume(svar1_6.<init>());
   _consume(svar0_8.println(svar1_6.append("AES Key (Hex Form): ").append(dev.sim0n.evaluator.util.crypto.AES.bytesToHex(lvar2_0.getEncoded())).toString()));
   svar0_9 = java.lang.System.out;
   svar1_10 = new java.lang.StringBuilder;
   _consume(svar1_10.<init>());
   _consume(svar0_9.println(svar1_10.append("Encrypted Text (Hex Form): ").append(dev.sim0n.evaluator.util.crypto.AES.bytesToHex(lvar3_0)).toString()));
   svar0_10 = java.lang.System.out;
   svar1_14 = new java.lang.StringBuilder;
   _consume(svar1_14.<init>());
   _consume(svar0_10.println(svar1_14.append("Decrypted Text: ").append(lvar4_0).toString()));
   return;
   

```

### Method: getSecretEncryptionKey()Ljavax/crypto/SecretKey;
Access: public static

```ssa
BLOCK A:
   
BLOCK B:
   lvar0_0 = javax.crypto.KeyGenerator.getInstance("AES");
   _consume(lvar0_0.init(128));
   return lvar0_0.generateKey();
   

```

### Method: encryptText(Ljava/lang/String;Ljavax/crypto/SecretKey;)[B
Access: public static

```ssa
BLOCK B:
   lvar2_0 = javax.crypto.Cipher.getInstance("AES");
   _consume(lvar2_0.init(1, lvar1_0));
   return lvar2_0.doFinal(lvar0_0.getBytes());
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   

```

### Method: decryptText([BLjavax/crypto/SecretKey;)Ljava/lang/String;
Access: public static

```ssa
BLOCK B:
   lvar2_0 = javax.crypto.Cipher.getInstance("AES");
   _consume(lvar2_0.init(2, lvar1_0));
   svar0_5 = new java.lang.String;
   _consume(svar0_5.<init>(lvar2_0.doFinal(lvar0_0)));
   return svar0_5;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   

```

### Method: bytesToHex([B)Ljava/lang/String;
Access: public static

```ssa
BLOCK D:
   svar0_6 = new java.lang.String;
   _consume(svar0_6.<init>(lvar1_0));
   return svar0_6;
   
BLOCK E:
   svar0_8 = lvar0_0[lvar2_1];
   lvar3_0 = {svar0_8 & 255};
   svar1_7 = {lvar2_1 * 2};
   svar2_2 = dev.sim0n.evaluator.util.crypto.AES.HEX_ARRAY;
   svar3_1 = {lvar3_0 >>> 4};
   svar2_3 = svar2_2[svar3_1];
   lvar1_0[svar1_7] = svar2_3;
   svar1_9 = {lvar2_1 * 2};
   svar1_10 = {svar1_9 + 1};
   svar2_6 = dev.sim0n.evaluator.util.crypto.AES.HEX_ARRAY;
   svar3_3 = {lvar3_0 & 15};
   svar2_7 = svar2_6[svar3_3];
   lvar1_0[svar1_10] = svar2_7;
   lvar2_2 = {lvar2_1 + 1};
   goto C
   
BLOCK C:
   lvar2_1 = ɸ{E:lvar2_2, B:lvar2_0};
   if (lvar2_1 >= lvar0_0.length)
      goto D
   
BLOCK B:
   lvar1_0 = new char[{lvar0_0.length * 2}];
   lvar2_0 = 0;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   

```

### Method: <clinit>()V
Access: static

```ssa
BLOCK B:
   dev.sim0n.evaluator.util.crypto.AES.HEX_ARRAY = "0123456789ABCDEF".toCharArray();
   return;
   
BLOCK A:
   

```


## Class: dev/sim0n/evaluator/operation/DoubleMathOperation$1
Super: dev/sim0n/evaluator/operation/DoubleMathOperation
Interfaces: []
Access: final synchronized enum

### Method: <init>(Ljava/lang/String;ILjava/lang/String;)V
Access: 

```ssa
BLOCK B:
   _consume(lvar0_0.<init>(lvar1_0, lvar2_0, lvar3_0, nullconst));
   return;
   
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar2_0 = lvar2_0);
   synth(lvar3_0 = lvar3_0);
   

```

### Method: evaluate(DD)D
Access: public

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   synth(lvar1_0 = lvar1_0);
   synth(lvar3_0 = lvar3_0);
   
BLOCK B:
   return {lvar1_0 + lvar3_0};
   

```


## Class: dev/sim0n/evaluator/test/Test
Super: java/lang/Object
Interfaces: []
Access: public interface abstract

### Method: handle()V
Access: public abstract

```ssa
BLOCK A:
   synth(lvar0_0 = lvar0_0);
   
BLOCK B:
   

```



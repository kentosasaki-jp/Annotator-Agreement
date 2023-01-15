# Annotator-Agreement
Sample programs for calculating Fleiss' Kappa and Cohen's Kappa.

```
pip install scikit-learn
```

<table class="wikitable" style="margin-left: auto; margin-right: auto; border: none;">
<tbody><tr>
<th>Condition</th>
<th><span class="mwe-math-element"><span class="mwe-math-mathml-inline mwe-math-mathml-a11y" style="display: none;"><math xmlns="http://www.w3.org/1998/Math/MathML" alttext="{\displaystyle \kappa }">
  <semantics>
    <mrow class="MJX-TeXAtom-ORD">
      <mstyle displaystyle="true" scriptlevel="0">
        <mi>κ<!-- κ --></mi>
      </mstyle>
    </mrow>
    <annotation encoding="application/x-tex"></annotation>
  </semantics>
</math></span><img src="https://wikimedia.org/api/rest_v1/media/math/render/svg/54ddec2e922c5caea4e47d04feef86e782dc8e6d" class="mwe-math-fallback-image-inline" aria-hidden="true" style="vertical-align: -0.338ex; width:1.339ex; height:1.676ex;" alt="\kappa "></span></th>
<th>Interpretation
</th></tr>
<tr>
<td rowspan="6" align="center">&nbsp;<i>Subjective example:  <br> <b>only</b> for two annotators, <br>on two classes. <br> See Landis &amp; Koch 1977</i>
</td>
<td align="center">&lt; 0</td>
<td>Poor agreement
</td></tr>
<tr>
<td align="center">0.01 – 0.20</td>
<td>Slight agreement
</td></tr>
<tr>
<td align="center">0.21 – 0.40</td>
<td>Fair agreement
</td></tr>
<tr>
<td align="center">0.41 – 0.60</td>
<td>Moderate agreement
</td></tr>
<tr>
<td align="center">0.61 – 0.80</td>
<td>Substantial agreement
</td></tr>
<tr>
<td align="center">0.81 – 1.00</td>
<td>Almost perfect agreement
</td></tr>
</tbody></table>

- Fleiss, J. L. (1971). Measuring nominal scale agreement among many raters. Psychological Bulletin, 76(5), 378–382. https://doi.org/10.1037/h0031619
- Cohen, J. (1968). Weighted kappa: Nominal scale agreement provision for scaled disagreement or partial credit. Psychological Bulletin, 70(4), 213–220. https://doi.org/10.1037/h0026256

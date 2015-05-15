/*
 * Collection of examples of the usage of the 'OneMetreAlign' class
 *
 * 
 *
 */

#include "ReadTwiss.h"
#include "Aperture.h"
#include "OneMetre.h"
#include "OneMetreAlign.h"
//#include "AssignOneMetre.h"

int main ()
{

  /*
  // Test: get aperture definition within OneMetre
  OneMetreAlign Test;
  //  Test.DefineAperture(0.0, 1, 1, 1, 1);
  //  Test.DefineAperture(0.1, 2, 2, 2, 2);
  //  Test.DefineAperture(0.2, 3, 3, 3, 3);
  //  Test.DefineAperture(0.3, 4, 4, 4, 4);
  //  Test.DefineAperture(0.99999, .4, .4, .4, .4);
  Test.DefineApertureAlign(0.0, 1, 1, 1, 1,2,1);
  Test.DefineApertureAlign(0.1, 2, 2, 2, 2,2,2);
  Test.DefineApertureAlign(0.2, 3, 3, 3, 3,2,3);
  Test.DefineApertureAlign(0.3, 4, 4, 4, 4,2,4);
  Test.DefineApertureAlign(0.99999, .4, .4, .4, .4,0,0);
  Test.status();

  vector<double> pos;
  vector<Aperture> pippo;
  Test.GetApertDef(&pos, &pippo);
  for( int i = 0; i < (int) pos.size(); i++){
    cout<<pos[i]<<" "
	<<pippo[i].GetApert(1)<<" "
	<<pippo[i].GetApert(2)<<" "
	<<pippo[i].GetApert(3)<<" "
	<<pippo[i].GetApert(4)<<endl;
  }
  return 0;
  */

  /*
  // Test the assignment of apertures at 0.0 and 1.0
  OneMetreAlign Test;
  Test.empty();
  Test.DefineApertureAlign(0.0, 1, 1, 1, 1, 1, 1);
  Test.DefineApertureAlign(0.1, 2, 2, 2, 2, 2, 2);
  Test.DefineApertureAlign(0.2, 3, 3, 3, 3, 3, 3);
  Test.DefineApertureAlign(0.3, 4, 4, 4, 4, 4, 4);
  Test.status();
  Aperture Pippo = Test.GetAperture( 0.5 );
  Test.status();
  //
  cout<<"Interpolated aperture at 0.5: "<<endl;
  cout<<Pippo.GetApert(1)<<" ";
  cout<<Pippo.GetApert(2)<<" ";
  cout<<Pippo.GetApert(3)<<" ";
  cout<<Pippo.GetApert(4)<<" "<<endl;
  cout<<Test.GetAlignX( 0.5 )<<endl;
  cout<<Test.GetAlignY( 0.5 )<<endl;
  Pippo = Test.GetAperture( 0.25 );
  cout<<"Interpolated aperture at 0.25:"<<endl;
  cout<<Pippo.GetApert(1)<<" ";
  cout<<Pippo.GetApert(2)<<" ";
  cout<<Pippo.GetApert(3)<<" ";
  cout<<Pippo.GetApert(4)<<" "<<endl;;
  cout<<Test.GetAlignX( 0.25 )<<endl;
  cout<<Test.GetAlignY( 0.25 )<<endl;
  Test.status();

  return 0;
  */

  /*
  // Test the interpolation routine in "GetAperture"
  double p;
  OneMetreAlign Metre;
  Aperture Atmp;
  Metre.DefineApertureAlign(0.0, 3, 3, 3, 3, 0.0, 0.4);
  Metre.DefineApertureAlign(0.1, 2, 2, 2, 2, 0.1, 0.3);
  Metre.DefineApertureAlign(0.2, 3, 3, 3, 3, 0.05, 0.2);
  Metre.DefineApertureAlign(0.3, 4, 4, 4, 4, 0.3, 0.1);
  Metre.status();

  ofstream out("StdOneMetreAlign.dat");
  out.precision(4);
  for (int i = 0; i < 101; i++){
    p = (double)(i)/100;
    Atmp.empty();
    Atmp = Metre.GetAperture( p );
    out<<setw(10)<<p;
    out<<setw(10)<<Atmp.GetApert(1);
    out<<setw(10)<<Atmp.GetApert(2);
    out<<setw(10)<<Atmp.GetApert(3);
    out<<setw(10)<<Atmp.GetApert(4);
    out<<setw(10)<<Atmp.GetApertAlignX();
    out<<setw(10)<<Atmp.GetApertAlignY();
    out<<setw(10)<<Metre.GetAlignX( p );
    out<<setw(10)<<Metre.GetAlignY( p )<<endl;
  }
  out.close();
  */
  /*
  Metre.empty();
  Metre.DefineAperture(0., 1, 1, 1, 1);
  Metre.DefineAperture(0., 2.1, 2.1, 2.1, 2.1);
  Metre.DefineAperture(0.1, 2, 2, 2, 2);
  Metre.DefineAperture(0.2, 3, 3, 3, 3);
  Metre.DefineAperture(0.2, 3.5, 3.5, 3.5, 3.5);
  Metre.DefineAperture(0.7, 4, 4, 4, 4);
  Metre.DefineAperture(0.7, 2, 2, 2, 2);
  Metre.DefineAperture(0.9, 2.5, 2.5, 2.5, 2.5);
  Metre.DefineAperture(0.9999, 2.7, 2.7, 2.7, 2.7);
  Metre.DefineAperture(0.9999, 1, 1, 1, 1);
  Metre.status();

  Atmp = Metre.GetAperture(0.5);
  cout<<Atmp.GetApert(1)<<endl;
  Atmp.empty();

  out.open("SpecialOneMetreAlign.dat");
  out.precision(4);
  for (int i = 0; i <= 200; i++){
    p = (double)(i)/200;
    Atmp.empty();
    Atmp = Metre.GetAperture( p );
    out<<setw(10)<<p;
    out<<setw(10)<<Atmp.GetApert(1);
    out<<setw(10)<<Atmp.GetApert(2);
    out<<setw(10)<<Atmp.GetApert(3);
    out<<setw(10)<<Atmp.GetApert(4)<<endl;
  }
  out.close();
  */

  // More complicated aperture shapes
  OneMetreAlign SinMetre;
  double p;
  Aperture Atmp;
  for (int i = 0; i <= 12; i++){
    p = (double)(i) / 12.1;
    SinMetre.DefineApertureAlign(p, sin(7*p), sin(7*p), 1, 1, cos(7*p), cos(7*p)*cos(7*p));
  }
  SinMetre.status();
  
  ofstream out("SinMetre.dat");
  out.precision(4); 
  for (int i = 0; i < 100; i++){
    p = (double)(i)/100.1;
    Atmp.empty();
    Atmp = SinMetre.GetAperture( p );
    out<<setw(10)<<p;
    out<<setw(10)<<Atmp.GetApert(1);
    out<<setw(10)<<Atmp.GetApert(2);
    out<<setw(10)<<Atmp.GetApert(3);
    out<<setw(10)<<Atmp.GetApert(4);
    out<<setw(10)<<Atmp.GetApertAlignX();
    out<<setw(10)<<Atmp.GetApertAlignY();
    out<<setw(10)<<SinMetre.GetAlignX( p );
    out<<setw(10)<<SinMetre.GetAlignY( p )<<endl;
  }
  return 0;
}
